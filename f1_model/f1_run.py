#!/usr/bin/env python3

import pandas as pd
import f1_functions
import quality_control as dq
import os
from dotenv import load_dotenv
import logging
from datetime import datetime, timedelta
import time


def main(custom_input_path: str = None) -> pd.DataFrame:
    """
    Executes the F1 driver statistics model. Returns an output of the top 3
    drivers in ascending order for average lap times, includes the drivers'
    fastest lap time. Writes the output to a CSV.

    Args:
        custom_input_path (string): An optional parameter to run a specific CSV
                                    instead of the default inputs

    Returns:
        pd.Dataframe: A dataframe with the top 3 drivers sorted by average lap
                      time.

    """
    # Setup parameters
    current_directory = os.path.dirname(os.path.realpath(__file__))
    env_path = os.path.join(current_directory, "..", "bin", ".env")
    load_dotenv(dotenv_path=env_path)
    home = os.getenv("F1HOME")

    # Input and log paths
    input_path = custom_input_path or f"{home}/data/f1_drivers_input.csv"
    log_directory = f"{home}/logs"
    logfile = (f"{log_directory}/f1_drivers_"
               f"{datetime.today().strftime('%Y%m%d_%H%M%S')}.log")
    output_path = f"{home}/data/top_3_drivers.csv"
    column_to_transform = 'time'
    columns_to_format = ['average_lap_time', 'fastest_lap_time']

    logging.basicConfig(
        format="%(asctime)s %(message)s",
        filename=logfile,
        level="INFO"
    )
    logging.getLogger().addHandler(logging.StreamHandler())
    start = time.time()

    logging.info("Starting F1 drivers analysis execution")
    logging.info(f"Reading input CSV {input_path}")

    inputs = pd.read_csv(input_path)

    logging.info("Transforming Inputs...")
    transformed_inputs = f1_functions.time_conversion(inputs,
                                                      column_to_transform)

    logging.info("Validating Inputs...")
    dq.main(transformed_inputs, 'DriverInputSchema')

    logging.info("Calculating average lap time per driver...")
    avg_time_df = f1_functions.average_time_per_driver(transformed_inputs)

    logging.info("Calculating best lap time per driver...")
    best_lap_time_df = f1_functions.best_lap_per_driver(transformed_inputs)

    logging.info("Extracting top 3 drivers by average time")
    f1_assets = pd.merge(avg_time_df, best_lap_time_df, on='driver')
    top_3_drivers = f1_functions.top_3_drivers_by_average_time(f1_assets)

    logging.info(f"Exporting top 3 drivers data to CSV: {output_path}")

    for column in columns_to_format:
        top_3_drivers[column] = (
            top_3_drivers[column].apply(f1_functions.format_timedelta))

    top_3_drivers.to_csv(output_path, index=False)

    logging.info("Run completed in: "
                 f"{timedelta(seconds=int(time.time() - start))}")
    return top_3_drivers


if __name__ == "__main__":
    main()  # pragma: no cover
