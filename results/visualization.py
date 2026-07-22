import matplotlib.pyplot as plt


def show_charts(results):

    if not results:
        print("No results available")
        return


    algorithms = []
    visited = []
    paths = []
    times = []
    memory = []


    # قراءة النتائج
    for r in results:

        if isinstance(r, dict):

            algorithms.append(r["algorithm"])
            visited.append(r["visited"])
            paths.append(r["path"])
            times.append(r["time"])
            memory.append(r["memory"])


        elif isinstance(r, tuple):

            algorithms.append(r[0])
            visited.append(r[1])
            paths.append(r[2])
            times.append(r[3])
            memory.append(r[4])


    # ===============================
    # Chart 1: Visited Nodes
    # ===============================

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



    # ===============================
    # Chart 2: Path Length
    # ===============================

    plt.figure(figsize=(8, 5))

    plt.bar(
        algorithms,
        paths
    )

    plt.title(
        "Path Length Comparison"
    )

    plt.xlabel(
        "Algorithm"
    )

    plt.ylabel(
        "Path Length"
    )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()

    plt.show()



    # ===============================
    # Chart 3: Execution Time
    # ===============================

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



    # ===============================
    # Chart 4: Memory Usage
    # ===============================

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