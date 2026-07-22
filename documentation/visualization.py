import os
import matplotlib.pyplot as plt


def create_charts(results):

    folder = "documentation/charts"

    if not os.path.exists(folder):
        os.makedirs(folder)


    algorithms = []
    times = []
    visited = []
    memories = []


    for r in results:

        if isinstance(r, tuple):

            algorithms.append(r[0])
            visited.append(r[1])
            times.append(r[3])
            memories.append(r[4])


        else:

            algorithms.append(r["algorithm"])
            visited.append(r["visited"])
            times.append(r["time"])
            memories.append(r["memory"])



    # ==========================
    # Execution Time Chart
    # ==========================

    plt.figure(figsize=(8,4))

    plt.bar(
        algorithms,
        times
    )

    plt.title(
        "Algorithm Execution Time"
    )

    plt.ylabel(
        "Seconds"
    )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()


    plt.savefig(
        f"{folder}/execution_time.png"
    )

    plt.close()



    # ==========================
    # Visited Nodes Chart
    # ==========================

    plt.figure(figsize=(8,4))

    plt.bar(
        algorithms,
        visited
    )

    plt.title(
        "Visited Nodes Comparison"
    )

    plt.ylabel(
        "Nodes"
    )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()


    plt.savefig(
        f"{folder}/visited_nodes.png"
    )

    plt.close()



    # ==========================
    # Memory Chart
    # ==========================

    plt.figure(figsize=(8,4))

    plt.bar(
        algorithms,
        memories
    )

    plt.title(
        "Memory Usage Comparison"
    )

    plt.ylabel(
        "MB"
    )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()


    plt.savefig(
        f"{folder}/memory_usage.png"
    )

    plt.close()



    print(
        "Charts Created Successfully"
    )