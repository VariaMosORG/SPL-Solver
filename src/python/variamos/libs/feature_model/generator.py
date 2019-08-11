import collections
import math
import random
import uuid

from .feature_model import *

PERCENTAGE = 100
AUTHOR = "VariaMos"
DESCRIPTION = "Randomly generated 3-CNF model"


# TODO: Generate cardinality, requires, excludes.
def generate_feature_model(
    num_features: int,
    branching_factor_min: int = 2,
    branching_factor_max: int = 10,
    mandatory_odds: float = 0.25,
    optional_odds: float = 0.25,
    or_odds: float = 0.25,
    xor_odds: float = 0.25,
    cross_tree_constraints: int = 0,
):
    MODEL_NAME = str(uuid.uuid1())

    selection_array = (
        [Mandatory] * (math.ceil(mandatory_odds * PERCENTAGE))
        + [Optional] * (math.ceil(optional_odds * PERCENTAGE))
        + [Or] * (math.ceil(or_odds * PERCENTAGE))
        + [Xor] * (math.ceil(xor_odds * PERCENTAGE))
    )

    get_constraint = lambda: random.choice(selection_array)
    get_branching_factor = lambda: random.randint(
        branching_factor_min, branching_factor_max
    )

    features = {1: Feature(id=1, name=str(uuid.uuid1()), constraints=[])}

    last_feature_id = 1
    not_visited = [1]

    while not_visited:
        not_visited_feature_id = not_visited.pop(0)
        branching_factor = get_branching_factor()

        father_feature = features[not_visited_feature_id]

        constraints = []
        for _ in range(branching_factor):
            constraints.append(get_constraint())

        counter = collections.Counter(constraints)
        num_mandatory = counter.get(Mandatory, 0)
        num_optional = counter.get(Optional, 0)
        num_or = counter.get(Or, 0)
        num_xor = counter.get(Xor, 0)

        for _ in range(num_mandatory):
            last_feature_id += 1
            features[last_feature_id] = Feature(
                id=last_feature_id, name=str(uuid.uuid1()), constraints=[]
            )

            constraint = Mandatory(destination=last_feature_id)
            father_feature.add_constraint(constraint)
            not_visited.append(last_feature_id)

        for _ in range(num_optional):
            last_feature_id += 1
            features[last_feature_id] = Feature(
                id=last_feature_id, name=str(uuid.uuid1()), constraints=[]
            )

            constraint = Optional(destination=last_feature_id)
            father_feature.add_constraint(constraint)
            not_visited.append(last_feature_id)

        or_feature_ids = []
        for _ in range(num_or):
            last_feature_id += 1
            features[last_feature_id] = Feature(
                id=last_feature_id, name=str(uuid.uuid1()), constraints=[]
            )

            or_feature_ids.append(last_feature_id)
            not_visited.append(last_feature_id)

        if or_feature_ids:
            constraint = Or(destination=or_feature_ids)
            father_feature.add_constraint(constraint)

        xor_feature_ids = []
        for _ in range(num_xor):
            last_feature_id += 1
            features[last_feature_id] = Feature(
                id=last_feature_id, name=str(uuid.uuid1()), constraints=[]
            )

            xor_feature_ids.append(last_feature_id)
            not_visited.append(last_feature_id)

        if xor_feature_ids:
            constraint = Xor(destination=xor_feature_ids)
            father_feature.add_constraint(constraint)

        if last_feature_id >= num_features:
            feature_model = FeatureModel(
                name=MODEL_NAME,
                author=AUTHOR,
                description=DESCRIPTION,
                features=list(features.values()),
            )

            break

    max_id = len(feature_model.features)
    options = [Requires, Excludes]
    get_feature_id = lambda: random.randint(0, max_id - 1)
    for _ in range(cross_tree_constraints):
        source_id = get_feature_id()
        destination_id = get_feature_id()

        source_feature = feature_model.features[source_id]
        destination_feature = feature_model.features[destination_id]

        constraint_class = random.choice(options)
        constraint = constraint_class(destination=destination_feature.id)

        source_feature.add_constraint(constraint)

    return feature_model
