from greedy import job_scheduling_greedy
from backtracking import job_scheduling_backtracking_bb
from utils import generate_jobs


def main():
    jobs = generate_jobs(6, seed=1)

    print("Jobs:", jobs)

    s1, p1 = job_scheduling_greedy(jobs)
    print("\nGreedy:", s1, "lucro:", p1)

    s2, p2 = job_scheduling_backtracking_bb(jobs)
    print("Backtracking:", s2, "lucro:", p2)


if __name__ == "__main__":
    main()
