from __future__ import annotations

import functools
import json
import typing

import minizinc
from variamos.libs.feature_model import (And, Cardinality, Excludes, Feature,
                                         FeatureModel, Mandatory, Optional, Or,
                                         Requires, Root, Xor,
                                         generate_feature_model)


def gen_variable(feature: Feature) -> str:
    return f"var 0..1: feature_{feature.id};\n"


@functools.singledispatch
def gen_constraint(constraint, source) -> str:
    pass


@gen_constraint.register
def _(constraint: Root, source: int):
    return f"constraint feature_{constraint.destination} = 1;\n"


@gen_constraint.register
def _(constraint: Mandatory, source: int):
    return f"constraint feature_{constraint.destination} = feature_{source};\n"


@gen_constraint.register
def _(constraint: Optional, source: int):
    return f"constraint feature_{source} >= feature_{constraint.destination};\n"


@gen_constraint.register
def _(constraint: Requires, source: int):
    return (
        f"constraint (1 - feature_{source}) + feature_{constraint.destination} > 0;\n"
    )


@gen_constraint.register
def _(constraint: Excludes, source: int):
    return f"constraint feature_{source} * feature_{constraint.destination} = 0;\n"


@gen_constraint.register
def _(constraint: And, source: int):
    destination_len = len(constraint.destination)
    new_constraint = Cardinality(
        low_threshold=destination_len,
        high_threshold=destination_len,
        destination=constraint.destination,
    )
    return gen_constraint(new_constraint, source)


@gen_constraint.register
def _(constraint: Or, source: int):
    destination_len = len(constraint.destination)
    new_constraint = Cardinality(
        low_threshold=1,
        high_threshold=destination_len,
        destination=constraint.destination,
    )
    return gen_constraint(new_constraint, source)


@gen_constraint.register
def _(constraint: Xor, source: int):
    destination_len = len(constraint.destination)
    new_constraint = Cardinality(
        low_threshold=1,
        high_threshold=destination_len - 1,
        destination=constraint.destination,
    )
    return gen_constraint(new_constraint, source)


@gen_constraint.register
def _(constraint: Cardinality, source: int):
    children_sum = " + ".join(
        [f"feature_{constraint}" for constraint in constraint.destination]
    )
    lower_bound = (
        f"constraint feature_{source} * {constraint.low_threshold} <= {children_sum};\n"
    )
    upper_bound = f"constraint {children_sum} <= feature_{source} * {constraint.high_threshold};\n"

    return "".join([lower_bound, upper_bound])


def get_solvers():
    solvers_json = minizinc.default_driver.run(["--solvers-json"]).stdout
    solvers = json.loads(solvers_json)

    return {solver["id"].split(".")[-1] for solver in solvers}


def get_operations_by_solver():
    solvers = get_solvers()
    feature_model = generate_feature_model(3)
    available_operations = {solver: [] for solver in solvers}

    for solver in solvers:
        mz_fm_solver = MZFMSolver.from_feature_model(
            feature_model=feature_model, solver=minizinc.Solver.lookup(solver)
        )

        try:
            mz_fm_solver.get_solutions(get_all_solutions=True)
            available_operations[solver].append("get-all-solutions")
        except Exception as e:
            pass

        try:
            mz_fm_solver.get_solutions(num_solutions=2)
            available_operations[solver].append("get-solutions")
        except Exception as e:
            pass

        try:
            mz_fm_solver.is_void_model()
            available_operations[solver].append("is-void-model")
        except Exception as e:
            pass

        try:
            mz_fm_solver.is_fake_product_line()
            available_operations[solver].append("is-fake-product-line")
        except Exception as e:
            pass

        try:
            mz_fm_solver.get_dead_features()
            available_operations[solver].append("get-dead-features")
        except Exception as e:
            pass

        try:
            mz_fm_solver.get_fake_optionals()
            available_operations[solver].append("get-fake-optionals")
        except Exception as e:
            pass

    all_operations = (
        "is-void-model",
        "is-fake-product-line",
        "get-dead-features",
        "get-fake-optionals",
    )

    for solver, operations in available_operations.items():
        if set(all_operations).issubset(operations):
            available_operations[solver].append("validate")

    return available_operations


class MZFMSolver:
    @classmethod
    def from_feature_model(
        cls,
        feature_model: FeatureModel,
        solver: minizinc.Solver = minizinc.Solver.lookup("gecode"),
    ) -> MZFMSolver:
        mini_zinc_vars = ""
        mini_zinc_const = ""

        optional_features = []
        for feature in feature_model.features:
            mini_zinc_vars = "".join([mini_zinc_vars, gen_variable(feature)])
            if feature.constraints:
                for constraint in feature.constraints:
                    mini_zinc_const = "".join(
                        [
                            mini_zinc_const,
                            gen_constraint(constraint, feature.id),
                        ]
                    )

                    if type(constraint) == Optional:
                        optional_features.append(f"feature_{constraint.destination}")

        feature_names = [f"feature_{feature.id}" for feature in feature_model.features]

        mini_zinc_str = "\n".join([mini_zinc_vars, mini_zinc_const, "solve satisfy;"])

        model = minizinc.Model()
        model.add_string(mini_zinc_str)

        return cls(
            model=model,
            feature_names=feature_names,
            optional_features=optional_features,
            solver=solver,
        )

    def __init__(
        self,
        model: minizinc.Model,
        feature_names: typing.List[str],
        optional_features: typing.Optional[typing.List[str]] = None,
        solver: minizinc.Solver = minizinc.Solver.lookup("gecode"),
    ):
        self.model = model
        self.solver = solver
        self.feature_names = feature_names
        self.optional_features = optional_features

    def get_solutions(
        self,
        num_solutions: int = 1,
        get_all_solutions: bool = False,
        selected_features: typing.Optional[typing.Tuple[str, int]] = None,
    ) -> typing.Optional[typing.Dict[str, int]]:
        instance = minizinc.Instance(self.solver, self.model)

        if selected_features:
            for feature_name, feature_value in selected_features:
                instance[feature_name] = feature_value

        if get_all_solutions:
            solutions = instance.solve(all_solutions=True).solution
        else:
            solutions = instance.solve(nr_solutions=num_solutions)

        if solutions:
            return [
                {
                    key: value
                    for key, value in solution.__dict__.items()
                    if key.startswith("feature")
                }
                for solution in solutions
            ]

        return None

    def is_void_model(self) -> bool:
        solution = self.get_solutions(num_solutions=1)

        if not solution:
            return True

        return False

    def is_fake_product_line(self) -> bool:
        solutions = self.get_solutions(num_solutions=2)
        solutions = solutions if solutions else []

        if not len(solutions) >= 2:
            return True

        return False

    def get_dead_features(self) -> typing.Optional[typing.List[str]]:
        dead_features = []

        for feature_name in self.feature_names:
            solution = self.get_solutions(
                num_solutions=1, selected_features=[(feature_name, 1)]
            )

            if not solution:
                dead_features.append(feature_name)

        if not dead_features:
            return None

        return dead_features

    def get_fake_optionals(self):
        fake_optionals = []

        for feature_name in self.optional_features:
            solution = self.get_solutions(
                num_solutions=1,
                selected_features=[(feature_name, 0)],
            )

            if not solution:
                fake_optionals.append(feature_name)

        if not fake_optionals:
            return None

        return fake_optionals
