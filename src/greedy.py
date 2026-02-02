def job_scheduling_greedy(jobs):
    """
    jobs: lista de tuplas (id, deadline, profit)
    retorna: (schedule, lucro_total)
    """

    if not jobs:
        return [], 0

    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)

    t = max(job[1] for job in jobs)

    schedule = [None] * t
    slot = [False] * t
    lucro_total = 0

    for job_id, deadline, profit in jobs:
        for j in range(min(t, deadline) - 1, -1, -1):
            if not slot[j]:
                slot[j] = True
                schedule[j] = job_id
                lucro_total += profit
                break

    return schedule, lucro_total
