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
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
