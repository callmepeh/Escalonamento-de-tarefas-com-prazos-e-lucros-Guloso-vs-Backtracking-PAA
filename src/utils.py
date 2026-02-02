import random
import time
import tracemalloc
import csv


def generate_jobs(n, seed=None):
    if seed is not None:
        random.seed(seed)

    jobs = []
    for i in range(1, n + 1):
        deadline = random.randint(1, n)
        profit = random.randint(10, 100)
        jobs.append((i, deadline, profit))

    return jobs


def measure(func, jobs):
    tracemalloc.start()
    start = time.perf_counter()

    result = func(jobs)

    end = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return result, end - start, peak / 1024


import os
import csv

def save_csv(path, rows):
    # cria as pastas automaticamente
    os.makedirs(os.path.dirname(path), exist_ok=True)

    keys = rows[0].keys()

    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)
