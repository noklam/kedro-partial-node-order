from kedro.pipeline import Pipeline, node, pipeline


def dummy1():
    print("Executed: A")
    return "free"


def dummy2():
    print("Executed: B")
    return "free"


def two_inputs(a, b):
    print("Executed: Final")
    return "final"


def create_pipeline(**kwargs) -> Pipeline:
    node_a = node(
        func=dummy1,
        inputs=None,
        outputs="A",
        name="A",
    )
    node_b = node(
        func=dummy2,
        inputs=None,
        outputs="B",
        name="B",
    )
    final_node = node(
        func=two_inputs,
        inputs=["A", "B"],
        outputs="Final",
        name="final",
    )
    my_pipeline = pipeline(
        [node_a, node_b, final_node],
        # custom_order =[node_b, node_a]

    )
    return my_pipeline
