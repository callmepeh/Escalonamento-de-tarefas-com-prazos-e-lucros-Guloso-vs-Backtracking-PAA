import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot():
    sns.set_theme(style="whitegrid")
    base_dir = os.path.dirname(os.path.dirname(__file__))
    csv_path = os.path.join(base_dir, "results", "raw", "benchmark.csv")
    graphs_dir = os.path.join(base_dir, "results", "graphs")
    os.makedirs(graphs_dir, exist_ok=True)

    if not os.path.exists(csv_path):
        print(f"Erro: Arquivo {csv_path} não encontrado.")
        return

    df = pd.read_csv(csv_path)

    # 1. Tempo de Execução
    plt.figure(figsize=(10, 6))
    # Separar dados reais de backtracking dos dados de referência
    df_bt_real = df[df['n'] <= 22]
    df_bt_ref = df[df['n'] > 22]
    
    plt.plot(df["n"], df["time_greedy"], marker='o', label="Guloso (Heurística Prazo)", linewidth=2)
    plt.plot(df_bt_real["n"], df_bt_real["time_backtracking"], marker='s', label="Backtracking (Real)", linewidth=2, color='orange')
    if not df_bt_ref.empty:
        plt.plot(df_bt_ref["n"], df_bt_ref["time_backtracking"], marker='x', label="Referência Ótima (Simulada)", linestyle='--', color='gray')
    
    plt.yscale('log')
    plt.title("Tempo de Execução: Guloso vs Backtracking (Escala Log)", fontsize=14)
    plt.xlabel("Tamanho da Entrada (n)", fontsize=12)
    plt.ylabel("Tempo (segundos)", fontsize=12)
    plt.legend()
    plt.savefig(os.path.join(graphs_dir, "tempo_execucao.png"), dpi=300)
    plt.close()

    # 2. Consumo de Memória
    plt.figure(figsize=(10, 6))
    plt.plot(df["n"], df["memory_greedy_kb"], marker='o', label="Guloso", linewidth=2, color='green')
    plt.plot(df_bt_real["n"], df_bt_real["memory_backtracking_kb"], marker='s', label="Backtracking", linewidth=2, color='red')
    plt.title("Consumo de Memória de Pico", fontsize=14)
    plt.xlabel("Tamanho da Entrada (n)", fontsize=12)
    plt.ylabel("Memória (KB)", fontsize=12)
    plt.legend()
    plt.savefig(os.path.join(graphs_dir, "consumo_memoria.png"), dpi=300)
    plt.close()

    # 3. Qualidade da Solução
    plt.figure(figsize=(10, 6))
    plt.plot(df["n"], df["profit_greedy"], marker='o', label="Guloso (Heurística Prazo)", linewidth=2, color='blue')
    plt.plot(df["n"], df["profit_backtracking"], marker='s', label="Solução Ótima", linewidth=2, color='orange', linestyle='--')
    plt.title("Qualidade da Solução: Lucro Total", fontsize=14)
    plt.xlabel("Tamanho da Entrada (n)", fontsize=12)
    plt.ylabel("Lucro Total", fontsize=12)
    plt.legend()
    plt.savefig(os.path.join(graphs_dir, "qualidade_solucao.png"), dpi=300)
    plt.close()

    # 4. Diferença Percentual
    df['diff_percent'] = ((df['profit_backtracking'] - df['profit_greedy']) / df['profit_backtracking']) * 100
    plt.figure(figsize=(10, 6))
    sns.barplot(x="n", y="diff_percent", data=df, palette="Reds_d")
    plt.title("Perda de Qualidade do Guloso (Heurística Prazo) vs Ótimo", fontsize=14)
    plt.xlabel("Tamanho da Entrada (n)", fontsize=12)
    plt.ylabel("Diferença de Lucro (%)", fontsize=12)
    plt.savefig(os.path.join(graphs_dir, "diferenca_qualidade.png"), dpi=300)
    plt.close()

    print(f"✅ Gráficos atualizados em: {graphs_dir}")

if __name__ == "__main__":
    plot()
