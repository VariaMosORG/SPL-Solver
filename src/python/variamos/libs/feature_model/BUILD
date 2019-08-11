python_library(
    sources=[
        "__init__.py",
        "feature_model.py",
        "generator.py",
    ],
)


python_tests(
    name="feature_model_tests",
    sources=[
        "tests/constratints_test.py",
        "tests/generator_test.py",
    ],
    dependencies=[
        ":feature_model",
        "//src/python/variamos/libs/mx_graph:mx_graph",
    ],
    tags=["integration_tests"],
)
