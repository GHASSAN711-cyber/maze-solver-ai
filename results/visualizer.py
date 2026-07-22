import matplotlib.pyplot as plt


def show_charts(results):

    if not results:
        print("No results available")
        return


    algorithms = [
        r["algorithm"]
        for r in results
    ]

    visited = [
        r["visited"]
        for r in results
    ]

    times = [
        r["time"]
        for r in results
    ]

    memory = [
        r["memory"]
        for r in results
    ]


    # ==========================
    # Visited Nodes
    # ==========================

    plt.figure(figsize=(8, 5))

    plt.bar(
        algorithms,
        visited
    )

    plt.title(
        "Visited Nodes Comparison"
    )

    plt.xlabel(
        "Algorithm"
    )

    plt.ylabel(
        "Visited Nodes"
    )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()

    plt.show()



    # ==========================
    # Execution Time
    # ==========================

    plt.figure(figsize=(8, 5))

    plt.bar(
        algorithms,
        times
    )

    plt.title(
        "Execution Time Comparison"
    )

    plt.xlabel(
        "Algorithm"
    )

    plt.ylabel(
        "Time (seconds)"
    )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()

    plt.show()



    # ==========================
    # Memory Usage
    # ==========================

    plt.figure(figsize=(8, 5))

    plt.bar(
        algorithms,
        memory
    )

    plt.title(
        "Memory Usage Comparison"
    )

    plt.xlabel(
        "Algorithm"
    )

    plt.ylabel(
        "Memory (MB)"
    )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()

    plt.show()