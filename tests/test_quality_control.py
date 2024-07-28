import pytest
import quality_control
import pandas as pd


def test_incomplete_input_dataset(incomplete_inputs: pd.DataFrame) -> None:
    """
    Test the validity and completeness of a dataset with incomplete inputs.

    Args:
        incomplete_inputs (pd.DataFrame): DataFrame containing incomplete F1
                                          race data.
    """
    with pytest.raises(quality_control.DQFailure):
        quality_control.validity_and_completeness(incomplete_inputs,
                                                  'DriverInputSchema')


def test_missing_input_dataset(missing_inputs: pd.DataFrame) -> None:
    """
    Test the validity and completeness of a dataset with missing inputs.

    Args:
        missing_inputs (pd.DataFrame): DataFrame containing F1 race data with
                                       missing values.
    """
    with pytest.raises(quality_control.DQFailure):
        quality_control.validity_and_completeness(missing_inputs,
                                                  'DriverInputSchema')


def test_invalid_input_dataset(invalid_inputs: pd.DataFrame) -> None:
    """
    Test the validity and completeness of a dataset with invalid inputs.

    Args:
        invalid_inputs (pd.DataFrame): DataFrame containing F1 race data with
                                       invalid time values.
    """
    with pytest.raises(quality_control.DQFailure):
        quality_control.validity_and_completeness(invalid_inputs,
                                                  'DriverInputSchema')


def test_valid_validate_driver() -> None:
    """
    Test the validation of a valid driver name.
    """
    valid_driver = 'Zaid Khalid'
    result = quality_control.NameValidator.validate_driver(valid_driver)
    assert result == valid_driver


def test_valid_validate_time() -> None:
    """
    Test the validation of a valid time value.
    """
    valid_time = pd.to_timedelta('00:01:00.001')
    result = quality_control.TimeValidator.validate_time(valid_time)
    assert result == valid_time


def test_invalid_validate_driver() -> None:
    """
    Test the validation of an invalid driver name.
    """
    invalid_driver = ''
    with pytest.raises(quality_control.DQFailure):
        quality_control.NameValidator.validate_driver(invalid_driver)


def test_invalid_validate_time() -> None:
    """
    Test the validation of an invalid time value.
    """
    invalid_time = '00:01:00.001'
    with pytest.raises(quality_control.DQFailure):
        quality_control.TimeValidator.validate_time(invalid_time)
