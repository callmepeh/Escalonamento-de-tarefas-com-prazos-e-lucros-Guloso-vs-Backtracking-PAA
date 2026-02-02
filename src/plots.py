import os
import pandas as pd
import matplotlib.pyplot as plt


def plot():
    # pega a raiz do projeto automaticamente
    base_dir = os.path.dirname(os.path.dirname(__file__))

    csv_path = os.path.join(base_dir, "results", "raw", "benchmark.csv")
    graphs_dir = os.path.join(base_dir, "results", "graphs")

    os.makedirs(graphs_dir, exist_ok=True)

    df = pd.read_csv(csv_path)

    # ===== tempo =====
    plt.figure()
    plt.plot(df["n"], df["time_greedy"], label="Greedy")
    plt.plot(df["n"], df["time_backtracking"], label="Backtracking")
    plt.xlabel("n")
    plt.ylabel("Tempo (s)")
    plt.legend()
    plt.savefig(os.path.join(graphs_dir, "tempo.png"))

    # ===== memória =====
    plt.figure()
    plt.plot(df["n"], df["memory_greedy_kb"], label="Greedy")
    plt.plot(df["n"], df["memory_backtracking_kb"], label="Backtracking")
    plt.xlabel("n")
    plt.ylabel("Memória (KB)")
    plt.legend()
    plt.savefig(os.path.join(graphs_dir, "memoria.png"))

    print("✅ Gráficos criados com sucesso em results/graphs/")


if __name__ == "__main__":
    plot()
