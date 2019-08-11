import typing

import minizinc
from fastapi import APIRouter, Body, Request
from pydantic import BaseModel
from variamos.libs.feature_model import FeatureModel
from variamos.libs.mini_zinc import MZFMSolver

router = APIRouter()


class Constraint(BaseModel):
    destination: typing.Optional[typing.Union[int, list]]
    constraint_type: str


class Feature(BaseModel):
    id: int
    name: str
    constraints: typing.Optional[typing.List[Constraint]] = {}


class FM(BaseModel):
    name: typing.Optional[str]
    author: typing.Optional[str]
    description: typing.Optional[str]
    features: typing.List[Feature]


class Solve(BaseModel):
    feature_model: FM
    num_solutions: typing.Optional[int] = 1


class Validate(BaseModel):
    feature_model: FM


class Transform(BaseModel):
    mx_graph: str


class Solution(BaseModel):
    detail: typing.List[typing.Dict[str, int]]

    class Config:
        schema_extra = {
            "example": {
                "detail": [
                    {"feature_28": 1, "feature_29": 1, "feature_30": 1, "feature_27": 1}
                ]
            }
        }


class Validation(BaseModel):
    solution: bool
    name: str
    detail: typing.Optional[typing.List[str]]

    class Config:
        schema_extra = {
            "example": {
                "solution": False,
                "name": "Has dead features",
                "detail": None,
            }
        }


class Validations(BaseModel):
    validations: typing.List[Validation]

    class Config:
        schema_extra = {
            "example": {
                "validations": [
                    {
                        "solution": False,
                        "name": "Is void model",
                        "detail": None,
                    },
                    {
                        "solution": True,
                        "name": "Is fake product line",
                        "detail": None,
                    },
                    {
                        "solution": False,
                        "name": "Has dead features",
                        "detail": None,
                    },
                    {
                        "solution": False,
                        "name": "Has dead features",
                        "detail": None,
                    },
                    {
                        "solution": False,
                        "name": "Has fake optionals",
                        "detail": None,
                    },
                    {
                        "solution": False,
                        "name": "Has fake optionals",
                        "detail": None,
                    },
                ]
            }
        }


@router.post("/{solver_name}/get-solutions", response_model=Solution)
async def get_solutions(
    *,
    solver_name: str = "chuffed",
    request: Solve = Body(
        ...,
        example={
            "feature_model": {
                "name": "string",
                "author": "string",
                "description": "string",
                "features": [
                    {"id": 28, "name": "Index"},
                    {"id": 29, "name": "Product"},
                    {"id": 30, "name": "ProductStar"},
                    {
                        "constraints": [
                            {"destination": 27, "constraint_type": "root"},
                            {"constraint_type": "mandatory", "destination": 28},
                            {"constraint_type": "mandatory", "destination": 29},
                            {"constraint_type": "mandatory", "destination": 30},
                        ],
                        "id": 27,
                        "name": "MiniStores",
                    },
                ],
            },
            "num_solutions": 1,
        },
    )
) -> Solution:
    feature_model = FeatureModel.create_from_dict(request.feature_model.dict())

    solver = minizinc.Solver.lookup(solver_name)
    mz_fm_solver = MZFMSolver.from_feature_model(feature_model, solver=solver)

    return Solution(
        detail=mz_fm_solver.get_solutions(num_solutions=request.num_solutions)
    )


@router.post("/{solver_name}/get-all-solutions", response_model=Solution)
async def get_all_solutions(
    *,
    solver_name: str,
    request: Solve = Body(
        ...,
        example={
            "feature_model": {
                "name": "string",
                "author": "string",
                "description": "string",
                "features": [
                    {"id": 28, "name": "Index"},
                    {"id": 29, "name": "Product"},
                    {"id": 30, "name": "ProductStar"},
                    {
                        "constraints": [
                            {"destination": 27, "constraint_type": "root"},
                            {"constraint_type": "mandatory", "destination": 28},
                            {"constraint_type": "mandatory", "destination": 29},
                            {"constraint_type": "mandatory", "destination": 30},
                        ],
                        "id": 27,
                        "name": "MiniStores",
                    },
                ],
            },
        },
    )
) -> Solution:
    feature_model = FeatureModel.create_from_dict(request.feature_model.dict())

    solver = minizinc.Solver.lookup(solver_name)
    mz_fm_solver = MZFMSolver.from_feature_model(feature_model, solver=solver)

    return Solution(detail=mz_fm_solver.get_solutions(get_all_solutions=True))


@router.post("/{solver_name}/is-void-model", response_model=Validation)
async def is_void_model(
    *,
    solver_name: str,
    request: Validate = Body(
        ...,
        example={
            "feature_model": {
                "name": "string",
                "author": "string",
                "description": "string",
                "features": [
                    {"id": 28, "name": "Index"},
                    {"id": 29, "name": "Product"},
                    {"id": 30, "name": "ProductStar"},
                    {
                        "constraints": [
                            {"destination": 27, "constraint_type": "root"},
                            {"constraint_type": "mandatory", "destination": 28},
                            {"constraint_type": "mandatory", "destination": 29},
                            {"constraint_type": "mandatory", "destination": 30},
                        ],
                        "id": 27,
                        "name": "MiniStores",
                    },
                ],
            },
        },
    )
) -> Validation:
    feature_model = FeatureModel.create_from_dict(request.feature_model.dict())

    solver = minizinc.Solver.lookup(solver_name)
    mz_fm_solver = MZFMSolver.from_feature_model(feature_model, solver=solver)

    return Validation(name="Is void model", solution=mz_fm_solver.is_void_model())


@router.post("/{solver_name}/is-fake-product-line", response_model=Validation)
async def is_fake_product_line(
    *,
    solver_name: str,
    request: Validate = Body(
        ...,
        example={
            "feature_model": {
                "name": "string",
                "author": "string",
                "description": "string",
                "features": [
                    {"id": 28, "name": "Index"},
                    {"id": 29, "name": "Product"},
                    {"id": 30, "name": "ProductStar"},
                    {
                        "constraints": [
                            {"destination": 27, "constraint_type": "root"},
                            {"constraint_type": "mandatory", "destination": 28},
                            {"constraint_type": "mandatory", "destination": 29},
                            {"constraint_type": "mandatory", "destination": 30},
                        ],
                        "id": 27,
                        "name": "MiniStores",
                    },
                ],
            },
        },
    )
) -> Validation:
    feature_model = FeatureModel.create_from_dict(request.feature_model.dict())

    solver = minizinc.Solver.lookup(solver_name)
    mz_fm_solver = MZFMSolver.from_feature_model(feature_model, solver=solver)

    return Validation(
        name="Is fake product line", solution=mz_fm_solver.is_fake_product_line()
    )


@router.post("/{solver_name}/get-dead-features", response_model=Validation)
async def get_dead_features(
    *,
    solver_name: str,
    request: Validate = Body(
        ...,
        example={
            "feature_model": {
                "name": "string",
                "author": "string",
                "description": "string",
                "features": [
                    {"id": 28, "name": "Index"},
                    {"id": 29, "name": "Product"},
                    {"id": 30, "name": "ProductStar"},
                    {
                        "constraints": [
                            {"destination": 27, "constraint_type": "root"},
                            {"constraint_type": "mandatory", "destination": 28},
                            {"constraint_type": "mandatory", "destination": 29},
                            {"constraint_type": "mandatory", "destination": 30},
                        ],
                        "id": 27,
                        "name": "MiniStores",
                    },
                ],
            },
        },
    )
) -> Validation:
    feature_model = FeatureModel.create_from_dict(request.feature_model.dict())

    solver = minizinc.Solver.lookup(solver_name)
    mz_fm_solver = MZFMSolver.from_feature_model(feature_model, solver=solver)

    dead_features = mz_fm_solver.get_dead_features()

    return Validation(
        name="Has dead features",
        solution=bool(dead_features),
        detail=dead_features,
    )


@router.post("/{solver_name}/get-fake-optionals", response_model=Validation)
async def get_fake_optional_features(
    *,
    solver_name: str,
    request: Validate = Body(
        ...,
        example={
            "feature_model": {
                "name": "string",
                "author": "string",
                "description": "string",
                "features": [
                    {"id": 28, "name": "Index"},
                    {"id": 29, "name": "Product"},
                    {"id": 30, "name": "ProductStar"},
                    {
                        "constraints": [
                            {"destination": 27, "constraint_type": "root"},
                            {"constraint_type": "mandatory", "destination": 28},
                            {"constraint_type": "mandatory", "destination": 29},
                            {"constraint_type": "mandatory", "destination": 30},
                        ],
                        "id": 27,
                        "name": "MiniStores",
                    },
                ],
            },
        },
    )
) -> Validation:
    feature_model = FeatureModel.create_from_dict(request.feature_model.dict())

    solver = minizinc.Solver.lookup(solver_name)
    mz_fm_solver = MZFMSolver.from_feature_model(feature_model, solver=solver)

    fake_optionals = mz_fm_solver.get_fake_optionals()

    return Validation(
        name="Has fake optionals",
        solution=bool(fake_optionals),
        detail=fake_optionals,
    )

"""
@router.post("/{solver_name}/validate", response_model=Validations)
async def validate_feature_model(
    *,
    solver_name: str,
    request: Validate = Body(
        ...,
        example={
            "feature_model": {
                "name": "string",
                "author": "string",
                "description": "string",
                "features": [
                    {"id": 28, "name": "Index"},
                    {"id": 29, "name": "Product"},
                    {"id": 30, "name": "ProductStar"},
                    {
                        "constraints": [
                            {"destination": 27, "constraint_type": "root"},
                            {"constraint_type": "mandatory", "destination": 28},
                            {"constraint_type": "mandatory", "destination": 29},
                            {"constraint_type": "mandatory", "destination": 30},
                        ],
                        "id": 27,
                        "name": "MiniStores",
                    },
                ],
            },
        },
    )
) -> Validations:
    feature_model = FeatureModel.create_from_dict(request.feature_model.dict())

    solver = minizinc.Solver.lookup(solver_name)
    mz_fm_solver = MZFMSolver.from_feature_model(feature_model, solver=solver)

    is_void = Validation(name="Is void model", solution=mz_fm_solver.is_void_model())
    is_fake_product_line = Validation(
        name="Is fake product line", solution=mz_fm_solver.is_fake_product_line()
    )

    dead_features = mz_fm_solver.get_dead_features()
    dead_features = Validation(
        name="Has dead features",
        solution=bool(dead_features),
        detail=dead_features,
    )

    fake_optionals = mz_fm_solver.get_fake_optionals()
    fake_optionals = Validation(
        name="Has fake optionals",
        solution=bool(fake_optionals),
        detail=fake_optionals,
    )

    return Validations(
        validations=[
            is_void,
            is_fake_product_line,
            dead_features,
            dead_features,
            fake_optionals,
            fake_optionals,
        ]
    )
"""

from variamos.libs.mx_graph import MXGraph

@router.post("/{solver_name}/validate", response_model=Validations)
async def validate_feature_model(*, solver_name: str, request: Request) -> Validations:
    mx_graph = await request.body()

    feature_model = MXGraph.parse_string(mx_graph.decode("utf-8"))
    feature_model = FeatureModel.create_from_dict(feature_model)

    solver = minizinc.Solver.lookup(solver_name)
    mz_fm_solver = MZFMSolver.from_feature_model(feature_model, solver=solver)

    is_void = Validation(name="Is void model", solution=mz_fm_solver.is_void_model())
    is_fake_product_line = Validation(
        name="Is fake product line", solution=mz_fm_solver.is_fake_product_line()
    )

    dead_features = mz_fm_solver.get_dead_features()
    dead_features = Validation(
        name="Has dead features",
        solution=bool(dead_features),
        detail=dead_features,
    )

    fake_optionals = mz_fm_solver.get_fake_optionals()
    fake_optionals = Validation(
        name="Has fake optionals",
        solution=bool(fake_optionals),
        detail=fake_optionals,
    )

    return Validations(
        validations=[
            is_void,
            is_fake_product_line,
            dead_features,
            fake_optionals,
        ]
    )

