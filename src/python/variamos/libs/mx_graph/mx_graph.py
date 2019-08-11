import io
import typing

from lxml import etree

FEATURE_CLON_SUFIX = "clon"


# TODO: Create function to transform from JSON to MXGraph.
class MXGraph:
    @classmethod
    def parse_file(cls, mx_graph: typing.IO) -> dict:
        xml_tree = etree.parse(mx_graph)
        mx_graph_data = MXGraph()
        return mx_graph_data.parse(xml_tree)

    @classmethod
    def parse_string(cls, mx_graph: str) -> dict:
        file = io.StringIO(mx_graph)
        return cls.parse_file(file)

    def parse(self, xml_tree: etree._ElementTree) -> dict:
        root = self.parse_root(xml_tree)

        features = self.parse_features(xml_tree)
        feature_relations = self.parse_feature_relations(xml_tree)

        bundles = self.parse_bundles(xml_tree)
        bundle_relations = self.parse_bundle_relations(xml_tree)

        features[root["id"]] = root
        features[root["id"]]["constraints"] = [
            {"destination": root["id"], "constraint_type": "root"}
        ]

        for feature_id in features.keys():
            for feature_relation in feature_relations.get(feature_id, []):
                if not features[feature_id].get("constraints", []):
                    features[feature_id]["constraints"] = []

                features[feature_id]["constraints"].append(feature_relation)

        # TODO: Can be simplified by spliting the parse_bundle_relations
        #    into tow separate functions, one for source and other for destination.
        source_bundle_relations_temp = {
            key: value
            for key, value in bundle_relations.items()
            if key in features.keys()
        }

        source_bundle_relations = {}
        for source_id, boundles in source_bundle_relations_temp.items():
            for bundle in boundles:
                bundle_id = bundle["destination"]
                source_bundle_relations[bundle_id] = source_id

        destination_bundle_relations_temp = {
            key: value
            for key, value in bundle_relations.items()
            if key not in features.keys()
        }

        destination_bundle_relations = {}
        for bundle_id, bundle_features in destination_bundle_relations_temp.items():
            for feature in bundle_features:
                feature_id = feature["destination"]
                if not destination_bundle_relations.get(bundle_id):
                    destination_bundle_relations[bundle_id] = []

                destination_bundle_relations[bundle_id].append(feature_id)

        for bundle_id, bundle in bundles.items():
            feature_id = source_bundle_relations[bundle_id]
            destinations = destination_bundle_relations[bundle_id]

            if not features[feature_id].get("constraints"):
                features[feature_id]["constraints"] = []

            constraint = {
                "constraint_type": bundle["bundle_type"],
                "destination": destinations,
            }

            if bundle.get("low_threshold") and bundle.get("high_threshold"):
                constraint["low_threshold"] = bundle["low_threshold"]
                constraint["high_threshold"] = bundle["high_threshold"]

            features[feature_id]["constraints"].append(constraint)

        feature_model = {"features": list(features.values())}

        return feature_model

    def parse_root(self, xml_tree: etree._ElementTree) -> dict:
        xpath = "//root"

        for root in xml_tree.xpath(xpath):
            root_dict = dict(root.items())
            if root_dict:
                return {
                    "id": int(root_dict["id"]),
                    "name": root_dict["label"],
                }

        raise ValueError()

    def parse_features(self, xml_tree: etree._ElementTree) -> dict:
        xpath = """
        //concrete |
        //abstract
        """

        features = {}
        for feature in xml_tree.xpath(xpath):
            feature_dict = dict(feature.items())
            if feature_dict and not FEATURE_CLON_SUFIX in feature_dict["id"]:
                feature_id = int(feature_dict["id"])
                features[feature_id] = {
                    "id": feature_id,
                    "name": feature_dict["label"],
                }

        return features

    def parse_feature_relations(self, xml_tree: etree._ElementTree) -> dict:
        relation_xpath = """
        //rel_concrete_root |
        //rel_abstract_root |
        //rel_concrete_abstract |
        //rel_concrete_concrete |
        //rel_abstract_concrete |
        //rel_abstract_abstract
        """

        source_xpaht = ".//mxCell"

        relations = {}
        for relation in xml_tree.xpath(relation_xpath):
            relation_dict = dict(relation.items())
            relation_source_dict = dict(relation.find(source_xpaht).items())
            if relation_dict and relation_source_dict:

                # Account for inverted direction in requires relations
                if relation_dict["relType"] == "requires":
                    source_id = int(relation_source_dict["source"])
                    destination_id = int(relation_source_dict["target"])
                else:
                    source_id = int(relation_source_dict["target"])
                    destination_id = int(relation_source_dict["source"])

                if not relations.get(source_id):
                    relations[source_id] = []

                relations[source_id].append(
                    {
                        "destination": destination_id,
                        "constraint_type": relation_dict["relType"],
                    }
                )

        return relations

    def parse_bundles(self, xml_tree: etree._ElementTree) -> dict:
        xpath = "//bundle"

        bundles = {}
        for bundle in xml_tree.xpath(xpath):
            bundle_dict = dict(bundle.items())
            if bundle_dict:
                bundle_id = int(bundle_dict["id"])
                bundle_type = bundle_dict["bundleType"].lower()

                if bundle_type == "range":
                    bundles[bundle_id] = {
                        "id": int(bundle_id),
                        "bundle_type": "group_cardinality",
                        "low_threshold": bundle_dict["lowRange"],
                        "high_threshold": bundle_dict["highRange"],
                    }
                else:
                    bundles[bundle_id] = {
                        "id": int(bundle_id),
                        "bundle_type": bundle_type,
                    }

        return bundles

    def parse_bundle_relations(self, xml_tree: etree._ElementTree) -> list:
        relation_xpath = """
        //rel_abstract_bundle |
        //rel_bundle_abstract |
        //rel_concrete_bundle |
        //rel_bundle_concrete
        """

        source_xpaht = ".//mxCell"

        relations = {}
        for relation in xml_tree.xpath(relation_xpath):
            relation_dict = dict(relation.items())
            relation_source_dict = dict(relation.find(source_xpaht).items())

            if relation_dict and relation_source_dict:
                source_id = int(relation_source_dict["target"])

                if not relations.get(source_id):
                    relations[source_id] = []

                relations[source_id].append(
                    {
                        "destination": int(relation_source_dict["source"]),
                    }
                )

        return relations
