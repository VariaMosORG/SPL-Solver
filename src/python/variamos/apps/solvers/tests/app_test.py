import json
import os
from urllib.parse import urljoin

import requests


def get_url():
    host = os.environ.get("HOST", "http://142.93.61.243")
    port = os.environ.get("PORT", "8000")

    return f"{host}:{port}"


URL = get_url()


def get_solvers():
    solver_list_path = "/solvers"

    request_url = urljoin(URL, solver_list_path)
    req = requests.get(request_url)

    assert req.status_code == 200


def test_json_transformation():
    transform_request_path = "/transform/mx-graph-to-json"

    data = """
    <mxGraphModel>
        <root>
            <mxCell id="0"/>
            <mxCell id="feature" parent="0"/>
            <root label="Mobile Phone" type="root" id="30">
            <mxCell style="strokeWidth=3" vertex="1" parent="feature">
                <mxGeometry x="190" y="50" width="100" height="35" as="geometry"/>
            </mxCell>
            </root>
            <abstract label="Calls" type="abstract" id="31">
            <mxCell style="strokeWidth=2" vertex="1" parent="feature">
                <mxGeometry x="10" y="110" width="100" height="35" as="geometry"/>
            </mxCell>
            </abstract>
            <abstract label="GPS" type="abstract" id="34">
            <mxCell style="strokeWidth=2" vertex="1" parent="feature">
                <mxGeometry x="130" y="110" width="100" height="35" as="geometry"/>
            </mxCell>
            </abstract>
            <abstract label="Screen" type="abstract" id="35">
            <mxCell style="strokeWidth=2" vertex="1" parent="feature">
                <mxGeometry x="250" y="110" width="100" height="35" as="geometry"/>
            </mxCell>
            </abstract>
            <abstract label="Media" type="abstract" id="36">
            <mxCell style="strokeWidth=2" vertex="1" parent="feature">
                <mxGeometry x="370" y="110" width="100" height="35" as="geometry"/>
            </mxCell>
            </abstract>
            <concrete label="Camera" type="concrete" selected="false" id="37">
            <mxCell style="" vertex="1" parent="feature">
                <mxGeometry x="380" y="230" width="100" height="35" as="geometry"/>
            </mxCell>
            </concrete>
            <concrete label="MP3" type="concrete" selected="false" id="38">
            <mxCell style="" vertex="1" parent="feature">
                <mxGeometry x="500" y="230" width="100" height="35" as="geometry"/>
            </mxCell>
            </concrete>
            <bundle label="bundle" type="bundle" bundleType="OR" lowRange="1" highRange="1" id="39">
            <mxCell style="shape=ellipse" vertex="1" parent="feature">
                <mxGeometry x="400" y="170" width="35" height="35" as="geometry"/>
            </mxCell>
            </bundle>
            <concrete label="High Resolution" type="concrete" selected="false" id="40">
            <mxCell style="" vertex="1" parent="feature">
                <mxGeometry x="260" y="230" width="100" height="35" as="geometry"/>
            </mxCell>
            </concrete>
            <concrete label="Cololur" type="concrete" selected="false" id="41">
            <mxCell style="" vertex="1" parent="feature">
                <mxGeometry x="140" y="230" width="100" height="35" as="geometry"/>
            </mxCell>
            </concrete>
            <concrete label="Basic" type="concrete" selected="false" id="42">
            <mxCell style="" vertex="1" parent="feature">
                <mxGeometry x="20" y="230" width="100" height="35" as="geometry"/>
            </mxCell>
            </concrete>
            <bundle label="bundle" type="bundle" bundleType="RANGE" lowRange="1" highRange="1" id="43">
            <mxCell style="shape=ellipse" vertex="1" parent="feature">
                <mxGeometry x="290" y="170" width="35" height="35" as="geometry"/>
            </mxCell>
            </bundle>
            <rel_abstract_root type="relation" relType="mandatory" id="44">
            <mxCell edge="1" parent="feature" source="31" target="30">
                <mxGeometry relative="1" as="geometry"/>
            </mxCell>
            </rel_abstract_root>
            <rel_abstract_root type="relation" relType="optional" id="45">
            <mxCell edge="1" parent="feature" source="34" target="30">
                <mxGeometry relative="1" as="geometry"/>
            </mxCell>
            </rel_abstract_root>
            <rel_abstract_root type="relation" relType="mandatory" id="46">
            <mxCell edge="1" parent="feature" source="35" target="30">
                <mxGeometry relative="1" as="geometry"/>
            </mxCell>
            </rel_abstract_root>
            <rel_abstract_root type="relation" relType="optional" id="47">
            <mxCell edge="1" parent="feature" source="36" target="30">
                <mxGeometry relative="1" as="geometry"/>
            </mxCell>
            </rel_abstract_root>
            <rel_concrete_bundle type="relation" id="48">
            <mxCell edge="1" parent="feature" source="37" target="39">
                <mxGeometry relative="1" as="geometry"/>
            </mxCell>
            </rel_concrete_bundle>
            <rel_concrete_bundle type="relation" id="49">
            <mxCell edge="1" parent="feature" source="38" target="39">
                <mxGeometry relative="1" as="geometry"/>
            </mxCell>
            </rel_concrete_bundle>
            <rel_bundle_abstract type="relation" id="50">
            <mxCell edge="1" parent="feature" source="39" target="36">
                <mxGeometry relative="1" as="geometry"/>
            </mxCell>
            </rel_bundle_abstract>
            <rel_bundle_abstract type="relation" id="51">
            <mxCell edge="1" parent="feature" source="43" target="35">
                <mxGeometry relative="1" as="geometry"/>
            </mxCell>
            </rel_bundle_abstract>
            <rel_concrete_bundle type="relation" id="52">
            <mxCell edge="1" parent="feature" source="40" target="43">
                <mxGeometry relative="1" as="geometry"/>
            </mxCell>
            </rel_concrete_bundle>
            <rel_concrete_bundle type="relation" id="53">
            <mxCell edge="1" parent="feature" source="41" target="43">
                <mxGeometry relative="1" as="geometry"/>
            </mxCell>
            </rel_concrete_bundle>
            <rel_concrete_bundle type="relation" id="54">
            <mxCell edge="1" parent="feature" source="42" target="43">
                <mxGeometry relative="1" as="geometry"/>
            </mxCell>
            </rel_concrete_bundle>
            <rel_concrete_abstract type="relation" relType="excludes" id="55">
            <mxCell edge="1" parent="feature" source="42" target="34">
                <mxGeometry relative="1" as="geometry"/>
            </mxCell>
            </rel_concrete_abstract>
            <rel_concrete_concrete type="relation" relType="requires" id="56">
            <mxCell edge="1" parent="feature" source="37" target="40">
                <mxGeometry relative="1" as="geometry"/>
            </mxCell>
            </rel_concrete_concrete>
            <mxCell id="component" parent="0" visible="0"/>
            <mxCell id="binding_feature_component" parent="0" visible="0"/>
            <concrete label="Camera" type="concrete" selected="false" id="clon37">
            <mxCell style="fillColor=#DCDCDC;" vertex="1" parent="binding_feature_component">
                <mxGeometry x="380" y="230" width="100" height="35" as="geometry"/>
            </mxCell>
            </concrete>
            <concrete label="MP3" type="concrete" selected="false" id="clon38">
            <mxCell style="fillColor=#DCDCDC;" vertex="1" parent="binding_feature_component">
                <mxGeometry x="540" y="230" width="100" height="35" as="geometry"/>
            </mxCell>
            </concrete>
            <concrete label="High Resolution" type="concrete" selected="false" id="clon40">
            <mxCell style="fillColor=#DCDCDC;" vertex="1" parent="binding_feature_component">
                <mxGeometry x="310" y="220" width="100" height="35" as="geometry"/>
            </mxCell>
            </concrete>
            <concrete label="Cololur" type="concrete" selected="false" id="clon41">
            <mxCell style="fillColor=#DCDCDC;" vertex="1" parent="binding_feature_component">
                <mxGeometry x="160" y="230" width="100" height="35" as="geometry"/>
            </mxCell>
            </concrete>
            <concrete label="Basic" type="concrete" selected="false" id="clon42">
            <mxCell style="fillColor=#DCDCDC;" vertex="1" parent="binding_feature_component">
                <mxGeometry x="60" y="250" width="100" height="35" as="geometry"/>
            </mxCell>
            </concrete>
            <mxCell id="istar" parent="0" visible="0"/>
            <mxCell id="adap_architecture" parent="0" visible="0"/>
            <mxCell id="adaptation_state" parent="0" visible="0"/>
            <mxCell id="adaptation_hardware" parent="0" visible="0"/>
            <mxCell id="adaptation_binding_state_hardware" parent="0" visible="0"/>
            <mxCell id="control" parent="0" visible="0"/>
        </root>
    </mxGraphModel>
    """

    expected_dict = {
        "features": [
            {"id": 31, "name": "Calls"},
            {
                "id": 34,
                "name": "GPS",
                "constraints": [{"destination": 42, "constraint_type": "excludes"}],
            },
            {
                "id": 35,
                "name": "Screen",
                "constraints": [
                    {
                        "constraint_type": "group_cardinality",
                        "destination": [40, 41, 42],
                        "low_threshold": "1",
                        "high_threshold": "1",
                    }
                ],
            },
            {
                "id": 36,
                "name": "Media",
                "constraints": [{"constraint_type": "or", "destination": [37, 38]}],
            },
            {"id": 37, "name": "Camera"},
            {"id": 38, "name": "MP3"},
            {
                "id": 40,
                "name": "High Resolution",
                "constraints": [{"destination": 37, "constraint_type": "requires"}],
            },
            {"id": 41, "name": "Cololur"},
            {"id": 42, "name": "Basic"},
            {
                "id": 30,
                "name": "Mobile Phone",
                "constraints": [
                    {"destination": 30, "constraint_type": "root"},
                    {"destination": 31, "constraint_type": "mandatory"},
                    {"destination": 34, "constraint_type": "optional"},
                    {"destination": 35, "constraint_type": "mandatory"},
                    {"destination": 36, "constraint_type": "optional"},
                ],
            },
        ]
    }

    request_url = urljoin(URL, transform_request_path)
    req = requests.post(request_url, data=data)

    assert expected_dict == json.loads(req.json())


def test_minizinc_solver_validation_operations():
    operations = (
        "/mini-zinc/gecode/is-void-model",
        "/mini-zinc/gecode/is-fake-product-line",
        "/mini-zinc/gecode/get-dead-features",
        "/mini-zinc/gecode/get-fake-optionals",
        "/mini-zinc/chuffed/is-void-model",
        "/mini-zinc/chuffed/is-fake-product-line",
        "/mini-zinc/chuffed/get-dead-features",
        "/mini-zinc/chuffed/get-fake-optionals",
        "/mini-zinc/gist/is-void-model",
        "/mini-zinc/gist/is-fake-product-line",
        "/mini-zinc/gist/get-dead-features",
        "/mini-zinc/gist/get-fake-optionals",
    )

    feature_model_dict = {
        "feature_model": {
            "features": [
                {"id": 31, "name": "Calls"},
                {
                    "id": 34,
                    "name": "GPS",
                    "constraints": [{"destination": 42, "constraint_type": "excludes"}],
                },
                {
                    "id": 35,
                    "name": "Screen",
                    "constraints": [
                        {
                            "constraint_type": "group_cardinality",
                            "destination": [40, 41, 42],
                            "low_threshold": "1",
                            "high_threshold": "1",
                        }
                    ],
                },
                {
                    "id": 36,
                    "name": "Media",
                    "constraints": [{"constraint_type": "or", "destination": [37, 38]}],
                },
                {"id": 37, "name": "Camera"},
                {"id": 38, "name": "MP3"},
                {
                    "id": 40,
                    "name": "High Resolution",
                    "constraints": [{"destination": 37, "constraint_type": "requires"}],
                },
                {"id": 41, "name": "Cololur"},
                {"id": 42, "name": "Basic"},
                {
                    "id": 30,
                    "name": "Mobile Phone",
                    "constraints": [
                        {"destination": 30, "constraint_type": "root"},
                        {"destination": 31, "constraint_type": "mandatory"},
                        {"destination": 34, "constraint_type": "optional"},
                        {"destination": 35, "constraint_type": "mandatory"},
                        {"destination": 36, "constraint_type": "optional"},
                    ],
                },
            ],
        },
    }

    for operation in operations:
        request_url = urljoin(URL, operation)
        req = requests.post(request_url, json=feature_model_dict)

        assert req.status_code == 200


def test_get_all_solution():
    operations = (
        "/mini-zinc/gecode/get-all-solutions",
        "/mini-zinc/chuffed/get-all-solutions",
        "/mini-zinc/gist/get-all-solutions",
    )

    feature_model_dict = {
        "feature_model": {
            "features": [
                {"id": 31, "name": "Calls"},
                {
                    "id": 34,
                    "name": "GPS",
                    "constraints": [{"destination": 42, "constraint_type": "excludes"}],
                },
                {
                    "id": 35,
                    "name": "Screen",
                    "constraints": [
                        {
                            "constraint_type": "group_cardinality",
                            "destination": [40, 41, 42],
                            "low_threshold": "1",
                            "high_threshold": "1",
                        }
                    ],
                },
                {
                    "id": 36,
                    "name": "Media",
                    "constraints": [{"constraint_type": "or", "destination": [37, 38]}],
                },
                {"id": 37, "name": "Camera"},
                {"id": 38, "name": "MP3"},
                {
                    "id": 40,
                    "name": "High Resolution",
                    "constraints": [{"destination": 37, "constraint_type": "requires"}],
                },
                {"id": 41, "name": "Cololur"},
                {"id": 42, "name": "Basic"},
                {
                    "id": 30,
                    "name": "Mobile Phone",
                    "constraints": [
                        {"destination": 30, "constraint_type": "root"},
                        {"destination": 31, "constraint_type": "mandatory"},
                        {"destination": 34, "constraint_type": "optional"},
                        {"destination": 35, "constraint_type": "mandatory"},
                        {"destination": 36, "constraint_type": "optional"},
                    ],
                },
            ],
        },
    }

    for operation in operations:
        request_url = urljoin(URL, operation)
        req = requests.post(request_url, json=feature_model_dict)

        assert req.status_code == 200


def test_get_solution():
    operations = (
        "/mini-zinc/chuffed/get-solutions",
        "/mini-zinc/gist/get-solutions",
        "/mini-zinc/gecode/get-solutions",
    )

    feature_model_dict = {
        "feature_model": {
            "features": [
                {"id": 31, "name": "Calls"},
                {
                    "id": 34,
                    "name": "GPS",
                    "constraints": [{"destination": 42, "constraint_type": "excludes"}],
                },
                {
                    "id": 35,
                    "name": "Screen",
                    "constraints": [
                        {
                            "constraint_type": "group_cardinality",
                            "destination": [40, 41, 42],
                            "low_threshold": "1",
                            "high_threshold": "1",
                        }
                    ],
                },
                {
                    "id": 36,
                    "name": "Media",
                    "constraints": [{"constraint_type": "or", "destination": [37, 38]}],
                },
                {"id": 37, "name": "Camera"},
                {"id": 38, "name": "MP3"},
                {
                    "id": 40,
                    "name": "High Resolution",
                    "constraints": [{"destination": 37, "constraint_type": "requires"}],
                },
                {"id": 41, "name": "Cololur"},
                {"id": 42, "name": "Basic"},
                {
                    "id": 30,
                    "name": "Mobile Phone",
                    "constraints": [
                        {"destination": 30, "constraint_type": "root"},
                        {"destination": 31, "constraint_type": "mandatory"},
                        {"destination": 34, "constraint_type": "optional"},
                        {"destination": 35, "constraint_type": "mandatory"},
                        {"destination": 36, "constraint_type": "optional"},
                    ],
                },
            ],
        },
        "num_solutions": 2,
    }

    for operation in operations:
        request_url = urljoin(URL, operation)
        req = requests.post(request_url, json=feature_model_dict)

        assert req.status_code == 200
