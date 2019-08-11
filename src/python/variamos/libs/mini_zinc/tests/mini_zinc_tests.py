import minizinc
from variamos.libs.feature_model import *
from variamos.libs.mini_zinc import MZFMSolver, get_solvers


def test_get_solvers():
    solvers = get_solvers()

    assert "scip" in solvers


def test_mini_store_model():
    feature_model = FeatureModel(
        name=None,
        author=None,
        description=None,
        features=[
            Feature(id=28, name="Index", constraints=None),
            Feature(id=29, name="Product", constraints=None),
            Feature(id=30, name="ProductStar", constraints=None),
            Feature(
                id=27,
                name="MiniStores",
                constraints=[
                    Root(destination=27),
                    Mandatory(destination=28),
                    Mandatory(destination=29),
                    Mandatory(destination=30),
                ],
            ),
        ],
    )

    mz = MZFMSolver.from_feature_model(feature_model)
    solutions = mz.get_solutions(get_all_solutions=True)

    assert len(solutions) == 1
    assert mz.is_void_model() == False
    assert mz.is_fake_product_line() == True
    assert mz.get_dead_features() == None
    assert mz.get_fake_optionals() == None


def test_mobile_phone_model():
    feature_model = FeatureModel(
        name=None,
        author=None,
        description=None,
        features=[
            Feature(id=31, name="Calls", constraints=None),
            Feature(id=34, name="GPS", constraints=[Excludes(destination=42)]),
            Feature(
                id=35,
                name="Screen",
                constraints=[
                    Cardinality(
                        destination=[40, 41, 42], low_threshold="1", high_threshold="1"
                    )
                ],
            ),
            Feature(id=36, name="Media", constraints=[Or(destination=[37, 38])]),
            Feature(id=37, name="Camera", constraints=None),
            Feature(id=38, name="MP3", constraints=None),
            Feature(
                id=40, name="High Resolution", constraints=[Requires(destination=37)]
            ),
            Feature(id=41, name="Cololur", constraints=None),
            Feature(id=42, name="Basic", constraints=None),
            Feature(
                id=30,
                name="Mobile Phone",
                constraints=[
                    Root(destination=30),
                    Mandatory(destination=31),
                    Optional(destination=34),
                    Mandatory(destination=35),
                    Optional(destination=36),
                ],
            ),
        ],
    )

    mz = MZFMSolver.from_feature_model(feature_model)
    solutions = mz.get_solutions(get_all_solutions=True)

    assert len(solutions) == 6
    assert mz.is_void_model() == False
    assert mz.is_fake_product_line() == False
    assert mz.get_dead_features() == ["feature_34", "feature_42"]
    assert mz.get_fake_optionals() == None


def test_fake_optionals():
    feature_model = FeatureModel(
        name=None,
        author=None,
        description=None,
        features=[
            Feature(
                id=1,
                name="root",
                constraints=[
                    Root(destination=1),
                    Mandatory(destination=3),
                    Optional(destination=4),
                ],
            ),
            Feature(id=3, name="feature_3", constraints=[Mandatory(destination=4)]),
            Feature(id=4, name="feature_5", constraints=None),
        ],
    )

    mz = MZFMSolver.from_feature_model(feature_model)

    assert mz.get_fake_optionals() == ["feature_3"]
