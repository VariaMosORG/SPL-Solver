from variamos.libs.feature_model import generate_feature_model


def test_feature_model_generation():
    num_features = 100
    branching_factor_min = 2
    branching_factor_max = 10
    cross_tree_constraints = 5

    feature_model = generate_feature_model(
        num_features=num_features,
        branching_factor_min=branching_factor_min,
        branching_factor_max=branching_factor_max,
        cross_tree_constraints=cross_tree_constraints,
    )

    assert num_features <= len(feature_model.features)
