from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents"""
    result = []
    try:
        with open(path, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')

            for row in reader:
                result.append(dict(row))
    except FileNotFoundError:
        raise FileNotFoundError("Arquivo não encontrado: " + path)
    else:
        return result


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them"""
    unique_job_types = []
    try:
        job_list = read(path)
        for job in job_list:
            if job['job_type'] not in unique_job_types:
                unique_job_types.append(job['job_type'])
    except KeyError:
        print(f"Chave inexistente em {job}: {job['job_type']}")
    else:
        return unique_job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type"""
    filtered_jobs = []
    try:
        job_types = get_unique_job_types('data/jobs.csv')
        if job_type not in job_types:
            raise Exception(f"Invalid job_type: {job_type}. "
                            f"Allowed values are: {', '.join(job_types)}")

        filtered_jobs = [job for job in jobs if job['job_type'] == job_type]
    except Exception as e:
        print(f"Error filtering jobs: {e}")
    return filtered_jobs
