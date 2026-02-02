def job_scheduling_greedy(jobs, heuristic='profit'):
    """
    jobs: lista de tuplas (id, deadline, profit)
    heuristic: 'profit' (ótimo) ou 'deadline' (não-ótimo)
    retorna: (schedule, lucro_total)
    """
    if not jobs:
        return [], 0

    # Heurística padrão: ordenar por lucro decrescente (ÓTIMA)
    if heuristic == 'profit':
        jobs_sorted = sorted(jobs, key=lambda x: x[2], reverse=True)
    # Heurística alternativa: ordenar por deadline crescente (NÃO-ÓTIMA)
    else:
        jobs_sorted = sorted(jobs, key=lambda x: x[1])

    t = max(job[1] for job in jobs)
    schedule = [None] * t
    slot = [False] * t
    lucro_total = 0

    for job_id, deadline, profit in jobs_sorted:
        # Tenta encaixar no último slot disponível antes do deadline
        for j in range(min(t, deadline) - 1, -1, -1):
            if not slot[j]:
                slot[j] = True
                schedule[j] = job_id
                lucro_total += profit
                break

    return schedule, lucro_total
