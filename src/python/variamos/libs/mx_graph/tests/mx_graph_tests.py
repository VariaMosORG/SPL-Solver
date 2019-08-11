import io

from variamos.libs.mx_graph import MXGraph


def test_ministore_model():
    mx_graph_str = """
    <mxGraphModel>
    <root>
        <mxCell id="0"/>
        <mxCell id="feature" parent="0"/>
        <root label="MiniStores" type="root" id="27">
        <mxCell style="strokeWidth=3" parent="feature" vertex="1">
            <mxGeometry x="336" y="47.5" width="100" height="35" as="geometry"/>
        </mxCell>
        </root>
        <concrete label="Index" type="concrete" selected="true" id="28">
        <mxCell style="" parent="feature" vertex="1">
            <mxGeometry x="192" y="154" width="100" height="35" as="geometry"/>
        </mxCell>
        </concrete>
        <concrete label="Product" type="concrete" selected="true" id="29">
        <mxCell style="" parent="feature" vertex="1">
            <mxGeometry x="337.5" y="152" width="100" height="35" as="geometry"/>
        </mxCell>
        </concrete>
        <concrete label="ProductStar" type="concrete" selected="true" id="30">
        <mxCell style="" parent="feature" vertex="1">
            <mxGeometry x="490" y="150" width="100" height="35" as="geometry"/>
        </mxCell>
        </concrete>
        <rel_concrete_root type="relation" relType="mandatory" id="31">
        <mxCell parent="feature" source="28" target="27" edge="1">
            <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        </rel_concrete_root>
        <rel_concrete_root type="relation" relType="mandatory" id="32">
        <mxCell parent="feature" source="29" target="27" edge="1">
            <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        </rel_concrete_root>
        <rel_concrete_root type="relation" relType="mandatory" id="33">
        <mxCell parent="feature" source="30" target="27" edge="1">
            <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        </rel_concrete_root>
        <mxCell id="component" parent="0" visible="0"/>
        <component label="Index" type="component" id="8">
        <mxCell style="shape=component" parent="component" vertex="1">
            <mxGeometry x="240" y="50" width="100" height="40" as="geometry"/>
        </mxCell>
        </component>
        <component label="Product" type="component" id="9">
        <mxCell style="shape=component" parent="component" vertex="1">
            <mxGeometry x="390" y="50" width="100" height="40" as="geometry"/>
        </mxCell>
        </component>
        <component label="ProductStar" type="component" id="10">
        <mxCell style="shape=component" parent="component" vertex="1">
            <mxGeometry x="540" y="50" width="100" height="40" as="geometry"/>
        </mxCell>
        </component>
        <file label="Product-Model" type="file" filename="Product.java" destination="src/Product.java" id="11">
        <mxCell style="shape=file" parent="component" vertex="1">
            <mxGeometry x="390" y="140" width="100" height="40" as="geometry"/>
        </mxCell>
        </file>
        <file label="Index-Control" type="file" filename="Index.java" destination="src/Index.java" id="12">
        <mxCell style="shape=file" parent="component" vertex="1">
            <mxGeometry x="100" y="80" width="100" height="40" as="geometry"/>
        </mxCell>
        </file>
        <file label="Index-Custom" type="file" filename="customization.json" destination="" id="13">
        <mxCell style="shape=file" parent="component" vertex="1">
            <mxGeometry x="230" y="140" width="100" height="40" as="geometry"/>
        </mxCell>
        </file>
        <file label="ProductStar-AlterIndex" type="file" filename="alterIndex.frag" destination="" id="14">
        <mxCell style="shape=file" parent="component" vertex="1">
            <mxGeometry x="530" y="140" width="100" height="40" as="geometry"/>
        </mxCell>
        </file>
        <file label="ProductStar-AlterProduct" type="file" filename="alterProduct.frag" destination="" id="15">
        <mxCell style="shape=file" parent="component" vertex="1">
            <mxGeometry x="672" y="139.5" width="100" height="40" as="geometry"/>
        </mxCell>
        </file>
        <rel_file_component type="relation" id="16">
        <mxCell parent="component" source="12" target="8" edge="1">
            <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        </rel_file_component>
        <rel_file_component type="relation" id="17">
        <mxCell parent="component" source="13" target="8" edge="1">
            <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        </rel_file_component>
        <rel_file_component type="relation" id="18">
        <mxCell parent="component" source="11" target="9" edge="1">
            <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        </rel_file_component>
        <rel_file_component type="relation" id="19">
        <mxCell parent="component" source="14" target="10" edge="1">
            <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        </rel_file_component>
        <rel_file_component type="relation" id="20">
        <mxCell parent="component" source="15" target="10" edge="1">
            <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        </rel_file_component>
        <mxCell id="binding_feature_component" parent="0" visible="0"/>
        <component label="Index" type="component" id="clon8">
        <mxCell style="shape=component;fillColor=#DCDCDC;" parent="binding_feature_component" vertex="1">
            <mxGeometry x="240" y="50" width="100" height="40" as="geometry"/>
        </mxCell>
        </component>
        <component label="Product" type="component" id="clon9">
        <mxCell style="shape=component;fillColor=#DCDCDC;" parent="binding_feature_component" vertex="1">
            <mxGeometry x="410" y="50" width="100" height="40" as="geometry"/>
        </mxCell>
        </component>
        <component label="ProductStar" type="component" id="clon10">
        <mxCell style="shape=component;fillColor=#DCDCDC;" parent="binding_feature_component" vertex="1">
            <mxGeometry x="570" y="50" width="100" height="40" as="geometry"/>
        </mxCell>
        </component>
        <concrete label="Index" type="concrete" selected="true" id="clon28">
        <mxCell style="fillColor=#DCDCDC;" parent="binding_feature_component" vertex="1">
            <mxGeometry x="242" y="168" width="100" height="35" as="geometry"/>
        </mxCell>
        </concrete>
        <concrete label="Product" type="concrete" selected="true" id="clon29">
        <mxCell style="fillColor=#DCDCDC;" parent="binding_feature_component" vertex="1">
            <mxGeometry x="412" y="168" width="100" height="35" as="geometry"/>
        </mxCell>
        </concrete>
        <concrete label="ProductStar" type="concrete" selected="true" id="clon30">
        <mxCell style="fillColor=#DCDCDC;" parent="binding_feature_component" vertex="1">
            <mxGeometry x="572" y="170" width="100" height="35" as="geometry"/>
        </mxCell>
        </concrete>
        <rel_concrete_component type="relation" id="34">
        <mxCell parent="binding_feature_component" source="clon28" target="clon8" edge="1">
            <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        </rel_concrete_component>
        <rel_concrete_component type="relation" id="35">
        <mxCell parent="binding_feature_component" source="clon29" target="clon9" edge="1">
            <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        </rel_concrete_component>
        <rel_concrete_component type="relation" id="36">
        <mxCell parent="binding_feature_component" source="clon30" target="clon10" edge="1">
            <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        </rel_concrete_component>
        <mxCell id="istar" parent="0" visible="0"/>
        <mxCell id="classdiag" parent="0" visible="0"/>
        <mxCell id="adap_architecture" parent="0" visible="0"/>
        <mxCell id="adaptation_state" parent="0" visible="0"/>
        <mxCell id="adaptation_hardware" parent="0" visible="0"/>
        <mxCell id="adaptation_binding_state_hardware" parent="0" visible="0"/>
        <mxCell id="control" parent="0" visible="0"/>
    </root>
    </mxGraphModel>
    """

    mx_graph = MXGraph.parse_string(mx_graph_str)

    expected_dict = {
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
        ]
    }

    assert mx_graph == expected_dict


def test_cellphone_model():
    mx_graph_str = """
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

    mx_graph = MXGraph.parse_string(mx_graph_str)

    expected_dict = {
        "features": [
            {"id": 31, "name": "Calls"},
            {
                "constraints": [{"constraint_type": "excludes", "destination": 42}],
                "id": 34,
                "name": "GPS",
            },
            {
                "constraints": [
                    {
                        "constraint_type": "group_cardinality",
                        "destination": [40, 41, 42],
                        "high_threshold": "1",
                        "low_threshold": "1",
                    }
                ],
                "id": 35,
                "name": "Screen",
            },
            {
                "constraints": [{"constraint_type": "or", "destination": [37, 38]}],
                "id": 36,
                "name": "Media",
            },
            {
                "constraints": [{"constraint_type": "requires", "destination": 40}],
                "id": 37,
                "name": "Camera",
            },
            {"id": 38, "name": "MP3"},
            {"id": 40, "name": "High Resolution"},
            {"id": 41, "name": "Cololur"},
            {"id": 42, "name": "Basic"},
            {
                "constraints": [
                    {"constraint_type": "root", "destination": 30},
                    {"constraint_type": "mandatory", "destination": 31},
                    {"constraint_type": "optional", "destination": 34},
                    {"constraint_type": "mandatory", "destination": 35},
                    {"constraint_type": "optional", "destination": 36},
                ],
                "id": 30,
                "name": "Mobile Phone",
            },
        ]
    }

    assert mx_graph == expected_dict


def test_fake_optional():
    mx_graph_str = """
        <mxGraphModel>
            <root>
                <mxCell id="0"/>
                <mxCell id="feature" parent="0"/>
                <root label="root" type="root" id="1">
                <mxCell style="strokeWidth=3" vertex="1" parent="feature">
                    <mxGeometry x="210" y="30" width="100" height="35" as="geometry"/>
                </mxCell>
                </root>
                <concrete label="concrete" type="concrete" selected="false" id="2">
                <mxCell style="" vertex="1" parent="feature">
                    <mxGeometry x="60" y="190" width="100" height="35" as="geometry"/>
                </mxCell>
                </concrete>
                <concrete label="concrete" type="concrete" selected="false" id="3">
                <mxCell style="" vertex="1" parent="feature">
                    <mxGeometry x="360" y="150" width="100" height="35" as="geometry"/>
                </mxCell>
                </concrete>
                <rel_concrete_root type="relation" relType="mandatory" id="0.3">
                <mxCell edge="1" parent="feature" source="2" target="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                </rel_concrete_root>
                <rel_concrete_root type="relation" relType="optional" id="0.4">
                <mxCell edge="1" parent="feature" source="3" target="1">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                </rel_concrete_root>
                <rel_concrete_concrete type="relation" relType="requires" id="0.5">
                <mxCell edge="1" parent="feature" source="2" target="3">
                    <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                </rel_concrete_concrete>
            </root>
        </mxGraphModel>
    """

    mx_graph = MXGraph.parse_string(mx_graph_str)

    expected_dict = {
        "features": [
            {
                "id": 2,
                "name": "concrete",
                "constraints": [{"destination": 3, "constraint_type": "requires"}],
            },
            {"id": 3, "name": "concrete"},
            {
                "id": 1,
                "name": "root",
                "constraints": [
                    {"destination": 1, "constraint_type": "root"},
                    {"destination": 2, "constraint_type": "mandatory"},
                    {"destination": 3, "constraint_type": "optional"},
                ],
            },
        ]
    }

    assert mx_graph == expected_dict
