import matplotlib.pyplot as plt
import os


# البيانات النهائية من تشغيل الخوارزميات

algorithms = [
    "BFS",
    "DFS",
    "Greedy",
    "A*",
    "UCS",
    "Bidirectional"
]

visited = [
    39,
    32,
    27,
    27,
    39,
    37
]

path = [
    20,
    20,
    24,
    20,
    20,
    20
]

time = [
    0.0052,
    0.0047,
    0.0032,
    0.0042,
    0.0048,
    0.0008
]

memory = [
    6.51,
    9.46,
    8.05,
    9.05,
    6.11,
    7.55
]


# مكان حفظ الصور
save_folder = "results"

if not os.path.exists(save_folder):
    os.makedirs(save_folder)



# -----------------------------
# 1) Visited Nodes
# -----------------------------

plt.figure(figsize=(8,5))

plt.bar(algorithms, visited)

plt.title("Visited Nodes Comparison")
plt.xlabel("Algorithm")
plt.ylabel("Visited Nodes")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    os.path.join(save_folder, "visited.png")
)

plt.close()



# -----------------------------
# 2) Path Length
# -----------------------------

plt.figure(figsize=(8,5))

plt.bar(algorithms, path)

plt.title("Path Length Comparison")
plt.xlabel("Algorithm")
plt.ylabel("Path Length")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    os.path.join(save_folder, "path.png")
)

plt.close()



# -----------------------------
# 3) Execution Time
# -----------------------------

plt.figure(figsize=(8,5))

plt.bar(algorithms, time)

plt.title("Execution Time Comparison")
plt.xlabel("Algorithm")
plt.ylabel("Time (seconds)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    os.path.join(save_folder, "time.png")
)

plt.close()



# -----------------------------
# 4) Memory Usage
# -----------------------------

plt.figure(figsize=(8,5))

plt.bar(algorithms, memory)

plt.title("Memory Usage Comparison")
plt.xlabel("Algorithm")
plt.ylabel("Memory")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    os.path.join(save_folder, "memory.png")
)

plt.close()



print("✅ All comparison charts saved successfully!")