import pytest
from src.pre_built.sorting import sort_by


@pytest.fixture
def jobs():
    return [
        {"title": "Job A", "min_salary": "2000", "max_salary": "10000",
            "date_posted": "2020-05-08"},
        {"title": "Job B", "min_salary": "1000", "max_salary": None,
            "date_posted": None},
        {"title": "Job C", "min_salary": None, "max_salary": "15000",
            "date_posted": "2021-05-08"},
    ]


def test_sort_by_criteria(jobs):
    """Testa se a função faz o ordenamento correto de acordo
    com a chave passada e se é lançado um
    ValueError ao usar um critério inválido"""
    sort_by(jobs, "min_salary")
    assert [j["title"] for j in jobs] == ["Job B", "Job A", "Job C"]

    sort_by(jobs, "max_salary")
    assert [j["title"] for j in jobs] == ["Job C", "Job A", "Job B"]

    sort_by(jobs, "date_posted")
    assert [j["title"] for j in jobs] == ["Job C", "Job A", "Job B"]

    with pytest.raises(ValueError):
        sort_by(jobs, "invalid_criteria")
