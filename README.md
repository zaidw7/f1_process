# F1 Lap Time Analysis Process

This project analyzes lap times for F1 drivers. It includes scripts to convert time data, calculate average lap times, and determine the fastest laps for each driver. The output is the top 3 drivers with the fastest average lap time.

## Contents
- [Introduction](#introduction)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Structure](#structure)
- [Testing](#testing)
- [Contributing](#contributing)

## Introduction
The F1 Lap Time Analysis Process is designed to help Formula 1 enthusiasts and analysts process and analyze lap time data for various drivers. By converting, calculating, and comparing lap times, this tool helps identify the top performers in terms of average lap times.

## Setup

### Prerequisites
- Python 3.x
- `pip` package manager

## Installation

1. Create and navigate to the directory of the repository:
    ```bash
    mkdir -p /<path>/f1_process
    cd /<path>/f1_process
    ```

2. Clone the repository:
    ```sh
    git clone -b main git@github.com:zaidw7/f1_process.git .
    ```

3. Run the build script to create the virtual environment:
    ```sh
    bin/build.sh
    ```

## Usage

1. Ensure the input file is placed in the `data` folder. The expected format is a CSV file with columns for driver names and their respective lap times.

2. Run the main script:
    ```sh
    f1_model/f1_run.py
    ```

4. The script generates a log file in the `logs` folder and an output file with the top 3 drivers sorted by average lap time in the `data` folder.

## Structure

- `bin/`: Contains binary files and scripts for setup.
- `data/`: Contains input and output data files.
- `f1_model/`: Contains the main processing scripts.
- `logs/`: Contains log files generated during script execution.
- `tests/`: Contains test scripts to verify the functionality.
- `requirements.txt`: Lists the Python packages required for the project.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

