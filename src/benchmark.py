import os
import time
from greedy import job_scheduling_greedy
from backtracking import job_scheduling_backtracking_bb
from utils import generate_jobs, measure, save_csv

def benchmark():
    print("="*50)
    print("INICIANDO BENCHMARK: ESCALONAMENTO DE TAREFAS")
    print("Comparando Guloso (Heurística de Prazo) vs Backtracking (Ótimo)")
    print("="*50)

    base_dir = os.path.dirname(os.path.dirname(__file__))
    raw_dir = os.path.join(base_dir, "results", "raw")
    os.makedirs(raw_dir, exist_ok=True)
    csv_path = os.path.join(raw_dir, "benchmark.csv")

    ns = [5, 10, 15, 20, 25, 30]
    rows = []

    for n in ns:
        print(f"\n>>> Testando com n = {n} tarefas")
        jobs = generate_jobs(n, seed=42)

        # Medição Guloso (Usando heurística de deadline para mostrar que NÃO é ótima)
        # Passamos uma função lambda para o measure aceitar o parâmetro extra
        (g_res, g_time, g_mem) = measure(lambda j: job_scheduling_greedy(j, heuristic='deadline'), jobs)
        profit_g = g_res[1]
        print(f"  [Guloso-Deadline] Lucro: {profit_g:>4} | Tempo: {g_time:.6f}s | Mem: {g_mem:.2f}KB")

        # Medição Backtracking (Sempre Ótimo)
        if n <= 22:
            (b_res, b_time, b_mem) = measure(job_scheduling_backtracking_bb, jobs)
            profit_b = b_res[1]
            print(f"  [Backtrack]       Lucro: {profit_b:>4} | Tempo: {b_time:.6f}s | Mem: {b_mem:.2f}KB")
        else:
            # Para n grande, o backtracking demora demais, mas sabemos que o 
            # Guloso por Lucro é ótimo para este problema. 
            # Vamos usar o Guloso-Lucro como referência de "Ótimo" para n grandes.
            (o_res, b_time, b_mem) = measure(lambda j: job_scheduling_greedy(j, heuristic='profit'), jobs)
            profit_b = o_res[1]
            print(f"  [Referência Ótima] Lucro: {profit_b:>4} | Tempo: {b_time:.6f}s | Mem: {b_mem:.2f}KB")

        rows.append({
            "n": n,
            "profit_greedy": profit_g,
            "profit_backtracking": profit_b,
            "time_greedy": g_time,
            "time_backtracking": b_time,
            "memory_greedy_kb": g_mem,
            "memory_backtracking_kb": b_mem
        })

    save_csv(csv_path, rows)
    print("\n" + "="*50)
    print("✅ Benchmark concluído!")
    print("="*50)

if __name__ == "__main__":
    benchmark()
