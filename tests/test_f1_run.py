import pytest
import pandas as pd


@pytest.mark.parametrize("item, expected", [
    ('driver', ['Zaid Khalid', 'Mick Schumacher', 'Lewis Hamilton']),
    ('average_lap_time', ['02:00.002',
                          '02:15.002',
                          '02:30.002']),
    ('fastest_lap_time', ['01:00.001',
                          '01:15.001',
                          '01:30.001'])
])
def test_f1_run(run_f1_inputs: pd.DataFrame,
                item: str,
                expected: list) -> None:
    """
    Test the main function from f1_run to ensure it correctly processes F1
    race data.

    Args:
        run_f1_inputs (pd.DataFrame): DataFrame containing the processed F1
                                      race data.

        item (str): Column name to check.

        expected (list): Expected list of values for the specified column.
    """
    results = run_f1_inputs

    for i in range(0, 3):
        assert (results[item][i] == expected[i])
