import os

from greedy import job_scheduling_greedy
from backtracking import job_scheduling_backtracking_bb
from utils import generate_jobs, measure, save_csv


def benchmark():
    print("=== BENCHMARK ESCALONAMENTO DE TAREFAS ===")

    # =============================
    # caminhos absolutos (FIX BUG)
    # =============================
    base_dir = os.path.dirname(os.path.dirname(__file__))

    results_dir = os.path.join(base_dir, "results")
    raw_dir = os.path.join(results_dir, "raw")

    os.makedirs(raw_dir, exist_ok=True)

    csv_path = os.path.join(raw_dir, "benchmark.csv")

    # tamanhos de teste
    ns = [5, 7, 9, 11, 13, 15, 17, 19]

    rows = []

    for n in ns:
        print(f"\nRodando para n = {n}")

        jobs = generate_jobs(n, seed=42)

        # =============================
        # GULOSO
        # =============================
        (g_result, g_time, g_mem) = measure(job_scheduling_greedy, jobs)
        (_, profit_g) = g_result

        print(f"Greedy -> lucro={profit_g} | tempo={g_time:.6f}s | mem={g_mem:.2f}KB")

        # =============================
        # BACKTRACKING
        # =============================
        # limite de segurança (exponencial)
        if n <= 19:
            (b_result, b_time, b_mem) = measure(job_scheduling_backtracking_bb, jobs)
            (_, profit_b) = b_result

            print(f"Backtracking -> lucro={profit_b} | tempo={b_time:.6f}s | mem={b_mem:.2f}KB")
        else:
            profit_b = None
            b_time = None
            b_mem = None

        rows.append({
            "n": n,
            "profit_greedy": profit_g,
            "profit_backtracking": profit_b,
            "time_greedy": g_time,
            "time_backtracking": b_time,
            "memory_greedy_kb": g_mem,
            "memory_backtracking_kb": b_mem
        })

    # =============================
    # salva csv
    # =============================
    save_csv(csv_path, rows)

    print("\n=================================")
    print("✅ Benchmark finalizado com sucesso!")
    print(f"Arquivo salvo em:\n{csv_path}")
    print("=================================")


if __name__ == "__main__":
    benchmark()
