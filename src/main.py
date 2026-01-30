from backtracking import job_sequencing

#ID, Deadline, Lucro
jobs = [
    ('A', 2, 100),
    ('B', 1, 19),
    ('C', 2, 27),
    ('D', 1, 25),
    ('E', 3, 15)
]

agenda, lucro = job_sequencing(jobs, 3)

print(f"Sequencia de tarefas: {agenda}")
print(f"Lucro maximo atingido: {lucro}")