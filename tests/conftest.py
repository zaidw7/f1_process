import pytest
import pandas as pd
import f1_functions
import f1_run
import tempfile
import os


@pytest.fixture(scope="module")
def run_f1_inputs() -> pd.DataFrame:
    """
    Fixture to create a temporary CSV file with F1 race data,
    run the main function from f1_run, and return the output.
    The temporary file is removed after the function runs.

    Returns:
        pd.DataFrame: The output from the f1_run.main function.
    """
    data = {'driver': ['Zaid Khalid', 'Zaid Khalid', 'Zaid Khalid',
                       'Mick Schumacher', 'Mick Schumacher', 'Mick Schumacher',
                       'Lewis Hamilton', 'Lewis Hamilton', 'Lewis Hamilton',
                       'Lando Norris', 'Lando Norris', 'Lando Norris'],
            'time': ['1:00.001', '2:00.002', '3:00.003',
                     '1:15.001', '2:15.002', '3:15.003',
                     '1:30.001', '2:30.002', '3:30.003',
                     '1:45.001', '2:45.002', '3:45.003']
            }

    path = tempfile.mktemp()
    pd.DataFrame(data).to_csv(path, index=False)
    run_out = f1_run.main(path)
    os.remove(path)

    return run_out


@pytest.fixture(scope="module")
def raw_inputs() -> pd.DataFrame:
    """
    Fixture to create a DataFrame with raw F1 race data.

    Returns:
        pd.DataFrame: DataFrame containing raw F1 race data.
    """
    data = {'driver': ['Zaid Khalid', 'Zaid Khalid', 'Zaid Khalid'],
            'time': ['1:00.001', '2:00.002', '3:00.003']
            }
    data_df = pd.DataFrame(data)

    return data_df


@pytest.fixture(scope="module")
def transformed_inputs() -> pd.DataFrame:
    """
    Fixture to create a DataFrame with raw F1 race data and transform it using
    the time_conversion function.

    Returns:
        pd.DataFrame: DataFrame containing transformed F1 race data.
    """
    data = {'driver': ['Zaid Khalid', 'Zaid Khalid', 'Zaid Khalid'],
            'time': ['1:00.001', '2:00.002', '3:00.003']}

    data_df = pd.DataFrame(data)
    transformed_data = f1_functions.time_conversion(data_df, 'time')

    return transformed_data


@pytest.fixture(scope="module")
def top_3_inputs() -> pd.DataFrame:
    """
    Fixture to create a DataFrame with the top 3 F1 drivers and their average
    lap times.

    Returns:
        pd.DataFrame: DataFrame containing the top 3 F1 drivers and their
                      average lap times.
    """
    data = {'driver': ['Zaid Khalid', 'Michael Schumacher', 'Lewis Hamilton',
                       'Lando Norris'],
            'average_lap_time': [pd.to_timedelta('00:02:00.002'),
                                 pd.to_timedelta('00:02:15.002'),
                                 pd.to_timedelta('00:02:30.002'),
                                 pd.to_timedelta('00:02:45.002')],
            'fastest_lap_time': [pd.to_timedelta('00:01:00.002'),
                                 pd.to_timedelta('00:01:15.002'),
                                 pd.to_timedelta('00:01:30.002'),
                                 pd.to_timedelta('00:01:45.002')]
            }
    data_df = pd.DataFrame(data)

    return data_df


@pytest.fixture(scope="module")
def incomplete_inputs() -> pd.DataFrame:
    """
    Fixture to create a DataFrame with incomplete F1 race data and transform it
    using the time_conversion function.

    Returns:
        pd.DataFrame: DataFrame containing transformed F1 race data with some
                      missing driver names.
    """
    data = {'driver': ['Zaid Khalid', 'Zaid Khalid', None],
            'time': ['1:00.001', '2:00.002', '3:00.003']}

    data_df = pd.DataFrame(data)
    incomplete_inputs = f1_functions.time_conversion(data_df, 'time')

    return incomplete_inputs


@pytest.fixture(scope="module")
def missing_inputs() -> pd.DataFrame:
    """
    Fixture to create a DataFrame with missing F1 race data.

    Returns:
        pd.DataFrame: DataFrame containing F1 race data with some missing
                      values.
    """
    data = {'driver': ['Zaid Khalid', '', 'Zaid Khalid'],
            'time': ['1:00.001', '2:00.002', '']}

    missing_inputs = pd.DataFrame(data)

    return missing_inputs


@pytest.fixture(scope="module")
def invalid_inputs() -> pd.DataFrame:
    """
    Fixture to create a DataFrame with invalid F1 race data.

    Returns:
        pd.DataFrame: DataFrame containing F1 race data with some invalid time
                      values.
    """
    data = {'driver': ['Zaid Khalid', 'Zaid Khalid', 'Zaid Khalid'],
            'time': ['1:00.001', '2:00.002', 'Zaid Khalid']}

    invalid_inputs = pd.DataFrame(data)

    return invalid_inputs
