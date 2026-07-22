def analyze_results(results):

    if not results:
        return "No results available"


    # دعم حالة tuple القديمة
    if isinstance(results[0], tuple):

        results = [
            {
                "algorithm": r[0],
                "visited": r[1],
                "path": r[2],
                "time": r[3],
                "memory": r[4]
            }
            for r in results
        ]


    # الأسرع
    fastest = min(
        results,
        key=lambda x: x["time"]
    )


    # أقصر مسار
    shortest = min(
        results,
        key=lambda x: x["path"]
    )


    # أقل ذاكرة
    lowest_memory = min(
        results,
        key=lambda x: x["memory"]
    )


    # التوصية
    recommendation = (
        f"Use {fastest['algorithm']} Search.\n"
        f"It achieved the fastest execution time "
        f"while keeping an optimal path."
    )


    report = f"""

========== AI ANALYSIS ==========

Fastest Algorithm: {fastest['algorithm']}
Execution Time: {fastest['time']} seconds


Shortest Path: {shortest['algorithm']}
Path Length: {shortest['path']}


Lowest Memory Usage: {lowest_memory['algorithm']}
Memory: {lowest_memory['memory']} MB


========== AI Recommendation ==========

Recommendation:

{recommendation}


====================================
"""


    print(report)

    return report