import typing
from enum import Enum
from pathlib import Path
from urllib.parse import urljoin

from fastapi import APIRouter
from pydantic import BaseModel
from variamos.libs.mini_zinc import get_operations_by_solver, get_solvers

MINI_ZINC_API_PREFIX = "/mini-zinc/"

# NOTE: Should update every time new solvers are added
#    this can be done by running get_operations_by_solver()
#    function from the variamos.libs.mini_zinc module
VALID_OPERATIONS = {
    "chuffed": [
        "get-all-solutions",
        "get-solutions",
        "is-void-model",
        "is-fake-product-line",
        "get-dead-features",
        "get-fake-optionals",
        "validate",
    ],
    "coin-bc": [],
    "cplex": [],
    "findmus": [],
    "gecode": [
        "get-all-solutions",
        "get-solutions",
        "is-void-model",
        "is-fake-product-line",
        "get-dead-features",
        "get-fake-optionals",
        "validate",
    ],
    "gist": [
        "get-all-solutions",
        "get-solutions",
        "is-void-model",
        "is-fake-product-line",
        "get-dead-features",
        "get-fake-optionals",
        "validate",
    ],
    "globalizer": [],
    "gurobi": [],
    "scip": [],
    "xpress": [],
}


router = APIRouter()


class Representation(str, Enum):
    minizinc = "minizinc"


class Solver(BaseModel):
    name: str
    url: Path
    representation: Representation
    operations: typing.List[str]


class SolverList(BaseModel):
    solvers: typing.List[Solver]

    class Config:
        schema_extra = {
            "example": {
                "solvers": [
                    {
                        "name": "findmus",
                        "operations": [],
                        "representation": "minizinc",
                        "url": "/mini-zinc/findmus",
                    },
                    {
                        "name": "scip",
                        "operations": [],
                        "representation": "minizinc",
                        "url": "/mini-zinc/scip",
                    },
                    {
                        "name": "gist",
                        "operations": [
                            "is-void-model",
                            "is-fake-product-line",
                            "get-dead-features",
                            "get-fake-optionals",
                            "get-all-solutions",
                            "get-solutions",
                        ],
                        "representation": "minizinc",
                        "url": "/mini-zinc/gist",
                    },
                    {
                        "name": "gecode",
                        "operations": [
                            "is-void-model",
                            "is-fake-product-line",
                            "get-dead-features",
                            "get-fake-optionals",
                            "get-all-solutions",
                            "get-solutions",
                        ],
                        "representation": "minizinc",
                        "url": "/mini-zinc/gecode",
                    },
                    {
                        "name": "xpress",
                        "operations": [],
                        "representation": "minizinc",
                        "url": "/mini-zinc/xpress",
                    },
                    {
                        "name": "gurobi",
                        "operations": [],
                        "representation": "minizinc",
                        "url": "/mini-zinc/gurobi",
                    },
                    {
                        "name": "chuffed",
                        "operations": [
                            "is-void-model",
                            "is-fake-product-line",
                            "get-dead-features",
                            "get-fake-optionals",
                            "get-all-solutions",
                            "get-solutions",
                        ],
                        "representation": "minizinc",
                        "url": "/mini-zinc/chuffed",
                    },
                    {
                        "name": "globalizer",
                        "operations": [],
                        "representation": "minizinc",
                        "url": "/mini-zinc/globalizer",
                    },
                    {
                        "name": "cplex",
                        "operations": [],
                        "representation": "minizinc",
                        "url": "/mini-zinc/cplex",
                    },
                    {
                        "name": "coin-bc",
                        "operations": [],
                        "representation": "minizinc",
                        "url": "/mini-zinc/coin-bc",
                    },
                ]
            }
        }


@router.get("/", response_model=SolverList)
async def read_users() -> typing.List[Solver]:
    return SolverList(
        solvers=[
            Solver(
                name=solver_name,
                url=urljoin(MINI_ZINC_API_PREFIX, solver_name),
                representation=Representation.minizinc,
                operations=VALID_OPERATIONS.get(solver_name, []),
            )
            for solver_name in get_solvers()
        ]
    )
