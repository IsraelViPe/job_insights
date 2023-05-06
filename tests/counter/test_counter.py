from src.pre_built.counter import count_ocurrences


def test_counter():
    """Conta a ocorrência da palavra 'back' no arquivo mockado"""
    assert count_ocurrences('tests/mocks/jobs.csv', 'Back') == 1
    assert count_ocurrences('tests/mocks/jobs.csv', 'back') == 1
