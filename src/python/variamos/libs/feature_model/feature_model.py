from __future__ import annotations

import json
import typing
from dataclasses import dataclass


@dataclass
class Constraint:
    destination: typing.List[int]


@dataclass
class Root(Constraint):
    pass


@dataclass
class Mandatory(Constraint):
    pass


@dataclass
class Optional(Constraint):
    pass


@dataclass
class Requires(Constraint):
    pass


@dataclass
class Excludes(Constraint):
    pass


@dataclass
class And(Constraint):
    pass


@dataclass
class Or(Constraint):
    pass


@dataclass
class Xor(Constraint):
    pass


@dataclass
class Cardinality(Constraint):
    low_threshold: int
    high_threshold: int


constraint_class_map = {
    "root": Root,
    "mandatory": Mandatory,
    "optional": Optional,
    "requires": Requires,
    "excludes": Excludes,
    "and": And,
    "or": Or,
    "xor": Xor,
    "group_cardinality": Cardinality,
}

constraint_name_map = {
    Root: "root",
    Mandatory: "mandatory",
    Optional: "optional",
    Requires: "requires",
    Excludes: "excludes",
    And: "and",
    Or: "or",
    Xor: "xor",
    Cardinality: "group_cardinality",
}


@dataclass
class Feature:
    id: int
    name: str
    constraints: typing.Optional[typing.List[Constraint]]

    def add_constraint(self, constraint: Constraint):
        if not self.constraints:
            self.constraints = []

        self.constraints.append(constraint)


class FeatureModel:
    def __init__(
        self,
        name: typing.Optional[str],
        author: typing.Optional[str],
        description: typing.Optional[str],
        features: typing.List[Feature],
    ):
        self.name = name
        self.author = author
        self.description = description
        self.features = features

    @classmethod
    def create_from_dict(cls, data_dict: dict) -> FeatureModel:
        name = data_dict.get("name")
        author = data_dict.get("author")
        description = data_dict.get("description")

        features = []
        for feature_dict in data_dict["features"]:
            feature = Feature(
                id=feature_dict["id"],
                name=feature_dict["name"],
                constraints=None,
            )

            for constraint_dict in feature_dict.get("constraints", []):
                constraint_class_name = constraint_dict["constraint_type"]
                constraint_class = constraint_class_map[constraint_class_name]

                destination = constraint_dict["destination"]

                if constraint_class == Cardinality:
                    constraint = constraint_class(
                        low_threshold=constraint_dict["low_threshold"],
                        high_threshold=constraint_dict["high_threshold"],
                        destination=destination,
                    )

                    feature.add_constraint(constraint=constraint)
                    continue

                constraint = constraint_class(destination=destination)
                feature.add_constraint(constraint=constraint)

            features.append(feature)

        return cls(
            name=name,
            author=author,
            description=description,
            features=features,
        )

    def to_dict(self):
        data = {
            "name": self.name,
            "author": self.author,
            "description": self.description,
        }

        features = []

        for feature in self.features:
            feature_id = feature.id
            feature_name = feature.name
            constraints = []

            feature_data = {
                "id": feature_id,
                "name": feature_name,
            }

            feature_constarints = feature.constraints if feature.constraints else []
            for constraint in feature_constarints:
                constraint_type = constraint_name_map[type(constraint)]
                destination = constraint.destination

                constraint_data = {
                    "constraint_type": constraint_type,
                    "destination": destination,
                }

                if type(constraint) == Cardinality:
                    constraint_data["low_threshold"] = constraint.low_threshold
                    constraint_data["high_threshold"] = constraint.high_threshold

                constraints.append(constraint_data)

            if constraints:
                feature_data["constraints"] = constraints

            features.append(feature_data)

        data["features"] = features
        return data

    def to_json(self):
        return json.dumps(self.to_dict(), sort_keys=True)
