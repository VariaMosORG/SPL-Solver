python_library(
    sources=[
        "__init__.py",
        "mx_graph.py",
    ],
    dependencies=["//external:lxml"]
)

python_tests(
    name="mx_graph_tests",
    sources=[
        "tests/mx_graph_tests.py"
    ],
    dependencies=[":mx_graph"],
    tags=["integration_tests"],
)
