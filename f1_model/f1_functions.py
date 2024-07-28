import pandas as pd
from datetime import timedelta


def time_conversion(data: pd.DataFrame,
                    column_to_convert: str) -> pd.DataFrame:
    """
    Convert string columns in a dataframe to timedelta.

    Args:
        data (pd.DataFrame): A dataframe containing data for drivers and lap
                             times.

        column_to_convert (str): Name of the string column to convert.

    Returns:
        pd.DataFrame: The dataframe with the converted column.
    """
    data[column_to_convert] = '00:' + data[column_to_convert]
    data[column_to_convert] = pd.to_timedelta(data[column_to_convert])

    return data


def average_time_per_driver(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the average lap time for each driver in the dataset.

    Args:
        data (pd.DataFrame): A dataframe containing data for drivers and lap
                             times.

    Returns:
        pd.DataFrame: A dataframe with the average lap time for each driver.
    """
    average_data = (data.groupby('driver')['time']
                    .mean()
                    .reset_index(name='average_lap_time'))

    return average_data


def best_lap_per_driver(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the fastest lap time for each driver in the dataset.

    Args:
        data (pd.DataFrame): A dataframe containing data for drivers and lap
                             times.

    Returns:
        pd.DataFrame: A dataframe with the fastest lap time for each driver.
    """
    best_lap_data = (
        data.loc[data.groupby('driver')['time']
                 .idxmin()]
            .reset_index(drop=True)
            .rename(columns={'time': 'fastest_lap_time'}))
    return best_lap_data


def top_3_drivers_by_average_time(f1_drivers: pd.DataFrame) -> pd.DataFrame:
    """
    Sort drivers by average lap time and return the top 3 drivers in ascending
    order.

    Args:
        f1_drivers (pd.DataFrame): A dataframe containing data for drivers
                                   and average/fastest lap times.

    Returns:
        pd.DataFrame: A dataframe with the top 3 drivers sorted by average lap
                      time.
    """
    sorted_avg_times = (
        f1_drivers
        .sort_values(by=['average_lap_time', 'fastest_lap_time'])
        .reset_index(drop=True))
    return sorted_avg_times.head(3)


def format_timedelta(delta: timedelta) -> str:
    """
    Format timedelta data types to MM:SS.SSS string format.

    Args:
        delta (timedelta): A timedelta value.

    Returns:
        str: The formatted time as a string.
    """
    total_seconds = int(delta.total_seconds())
    minutes, seconds = divmod(total_seconds, 60)
    milliseconds = delta.microseconds // 1000
    time = f"{minutes:02}:{seconds:02}.{milliseconds:03}"

    return time
