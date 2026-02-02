best_profit = 0
best_schedule = None


def backtrack_bb(jobs, idx, schedule, used, current_profit, remaining_profit):
    global best_profit, best_schedule

    # PODA (BOUND)
    if current_profit + remaining_profit <= best_profit:
        return

    if idx == len(jobs):
        if current_profit > best_profit:
            best_profit = current_profit
            best_schedule = schedule.copy()
        return

    job_id, deadline, profit = jobs[idx]

    # tenta colocar
    for t in range(deadline - 1, -1, -1):
        if not used[t]:
            used[t] = True
            schedule[t] = job_id

            backtrack_bb(
                jobs,
                idx + 1,
                schedule,
                used,
                current_profit + profit,
                remaining_profit - profit
            )

            used[t] = False
            schedule[t] = None
            break

    # pula
    backtrack_bb(
        jobs,
        idx + 1,
        schedule,
        used,
        current_profit,
        remaining_profit - profit
    )


def job_scheduling_backtracking_bb(jobs):
    global best_profit, best_schedule

    best_profit = 0

    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)

    t = max(job[1] for job in jobs)

    schedule = [None] * t
    used = [False] * t

    total_profit = sum(job[2] for job in jobs)

    backtrack_bb(jobs, 0, schedule, used, 0, total_profit)

    return best_schedule, best_profit
