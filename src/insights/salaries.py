from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs"""
    max_salary_list = []
    try:
        jobs = read(path)
        for job in jobs:
            if job['max_salary'].isdigit():
                max_salary_list.append(int(job['max_salary']))
    except Exception as e:
        print(f"Error getting max salary: {e}")
    else:
        return max(max_salary_list)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs"""
    min_salary_list = []
    try:
        jobs = read(path)
        for job in jobs:
            if job['min_salary'] and job['min_salary'].isdigit():
                min_salary_list.append(int(job['min_salary']))
    except Exception as e:
        print(f"Error getting min salary: {e}")
    else:
        return min(min_salary_list)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job"""
    try:
        min_s = int(job["min_salary"])
        max_s = int(job["max_salary"])
        int_s = int(salary)

        if 'min_salary'not in job or 'max_salary' not in job:
            raise ValueError("'min_salary' or 'max_salary' doesn't exists")

        if type(min_s) != int or type(max_s) != int:
            raise ValueError("'min_salary' or 'max_salary' aren't valid int")

        if min_s > max_s:
            raise ValueError("'min_salary' is greather than 'max_salary'")

        if type(int_s) != int:
            raise ValueError("salary isn't a valid integer")

        return min_s <= int_s <= max_s
    except (KeyError, TypeError, ValueError) as e:
        print(f"Error matching salary range: {e}")
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range"""
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary) is True:
                filtered_jobs.append(job)
        except ValueError as e:
            print(e)
    return filtered_jobs
