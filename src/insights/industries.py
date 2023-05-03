from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them"""
    unique_industries = []
    try:
        jobs = read(path)
        for job in jobs:
            if job['industry'] and job['industry'] not in unique_industries:
                unique_industries.append(job['industry'])
    except KeyError:
        print(f"Chave inexistente em {job}: {job['industry']}")
    else:
        return unique_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry"""
    filtered_ind = [job for job in jobs if job['industry'] == industry]
    return filtered_ind
