import matplotlib.pyplot as plt


def show_charts(results):

    algorithms = []
    visited = []
    paths = []
    times = []
    memories = []


    for result in results:

        algorithms.append(result[0])
        visited.append(result[1])
        paths.append(result[2])
        times.append(result[3])
        memories.append(result[4])


    # =========================
    # Chart 1: Visited Nodes
    # =========================

    plt.figure(figsize=(8, 5))

    plt.bar(algorithms, visited)

    plt.title("Visited Nodes Comparison")
    plt.xlabel("Algorithm")
    plt.ylabel("Visited Nodes")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()



    # =========================
    # Chart 2: Path Length
    # =========================

    plt.figure(figsize=(8, 5))

    plt.bar(algorithms, paths)

    plt.title("Path Length Comparison")
    plt.xlabel("Algorithm")
    plt.ylabel("Path Length")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()



    # =========================
    # Chart 3: Execution Time
    # =========================

    plt.figure(figsize=(8, 5))

    plt.bar(algorithms, times)

    plt.title("Execution Time Comparison")
    plt.xlabel("Algorithm")
    plt.ylabel("Time (seconds)")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()



    # =========================
    # Chart 4: Memory Usage
    # =========================

    plt.figure(figsize=(8, 5))

    plt.bar(algorithms, memories)

    plt.title("Memory Usage Comparison")
    plt.xlabel("Algorithm")
    plt.ylabel("Memory")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()