import csv


def export_results(results):

    if not results:
        print("No results to export")
        return


    file_path = "results/maze_results.csv"


    with open(
        file_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)


        writer.writerow(
            [
                "Algorithm",
                "Visited Nodes",
                "Path Length",
                "Time (sec)",
                "Memory (MB)"
            ]
        )


        for r in results:

            writer.writerow(
                [
                    r["algorithm"],
                    r["visited"],
                    r["path"],
                    r["time"],
                    r["memory"]
                ]
            )


    print(
        "Results exported successfully:"
        ,
        file_path
    )