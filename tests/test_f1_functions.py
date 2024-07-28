import pandas as pd
import f1_functions
import pytest


@pytest.mark.parametrize("item, expected", [
    ('driver', ['Zaid Khalid', 'Zaid Khalid', 'Zaid Khalid']),
    ('time', [pd.to_timedelta('00:01:00.001'),
              pd.to_timedelta('00:02:00.002'),
              pd.to_timedelta('00:03:00.003')])
              ])
def test_time_conversion(transformed_inputs: pd.DataFrame,
                         item: str,
                         expected: list) -> None:
    """
    Test the time_conversion function to ensure it correctly converts time
    strings to timedeltas.

    Args:
        transformed_inputs (pd.DataFrame): DataFrame containing transformed F1
                                           race data.

        item (str): Column name to check.

        expected (list): Expected list of values for the specified column.
    """
    for i in range(0, 2):
        assert transformed_inputs[item][i] == expected[i]


@pytest.mark.parametrize("item, expected", [
    ('driver', ['Zaid Khalid']),
    ('average_lap_time', [pd.to_timedelta('00:02:00.002')])
    ])
def test_average_time_per_driver(transformed_inputs: pd.DataFrame,
                                 item: str,
                                 expected: list) -> None:
    """
    Test the average_time_per_driver function to ensure it correctly calculates
    the average lap time per driver.

    Args:
        transformed_inputs (pd.DataFrame): DataFrame containing transformed F1
                                           race data.

        item (str): Column name to check.

        expected (list): Expected list of values for the specified column.
    """
    results = f1_functions.average_time_per_driver(transformed_inputs)
    assert results[item][0] == expected[0]


@pytest.mark.parametrize("item, expected", [
    ('driver', ['Zaid Khalid']),
    ('fastest_lap_time', [pd.to_timedelta('00:01:00.001')])
    ])
def test_best_lap_per_driver(transformed_inputs: pd.DataFrame,
                             item: str,
                             expected: list) -> None:
    """
    Test the best_lap_per_driver function to ensure it correctly identifies the
    best lap time per driver.

    Args:
        transformed_inputs (pd.DataFrame): DataFrame containing transformed F1
                                           race data.

        item (str): Column name to check.

        expected (list): Expected list of values for the specified column.
    """
    results = f1_functions.best_lap_per_driver(transformed_inputs)
    assert results[item][0] == expected[0]


@pytest.mark.parametrize("item, expected", [
    ('driver', ['Zaid Khalid', 'Michael Schumacher', 'Lewis Hamilton']),
    ('average_lap_time', [pd.to_timedelta('00:02:00.002'),
                          pd.to_timedelta('00:02:15.002'),
                          pd.to_timedelta('00:02:30.002')]),
    ('fastest_lap_time', [pd.to_timedelta('00:01:00.002'),
                          pd.to_timedelta('00:01:15.002'),
                          pd.to_timedelta('00:01:30.002')])
    ])
def test_top_3_drivers_by_average_time(top_3_inputs: pd.DataFrame,
                                       item: str,
                                       expected: list) -> None:
    """
    Test the top_3_drivers_by_average_time function to ensure it correctly
    identifies the top 3 drivers by average lap time.

    Args:
        top_3_inputs (pd.DataFrame): DataFrame containing F1 race data for the
                                     top 3 drivers.

        item (str): Column name to check.

        expected (list): Expected list of values for the specified column.
    """
    results = f1_functions.top_3_drivers_by_average_time(top_3_inputs)
    for i in range(0, 3):
        assert results[item][i] == expected[i]


@pytest.mark.parametrize("item, expected", [
    (pd.to_timedelta('00:01:00.001'), '01:00.001'),
    (pd.to_timedelta('00:02:00.002'), '02:00.002')
    ])
def test_format_timedelta(item: pd.Timedelta,
                          expected: str) -> None:
    """
    Test the format_timedelta function to ensure it correctly formats timedelta
    objects to strings.

    Args:
        item (pd.Timedelta): Timedelta object to format.

        expected (str): Expected formatted string.
    """
    result = f1_functions.format_timedelta(item)
    assert result == expected
