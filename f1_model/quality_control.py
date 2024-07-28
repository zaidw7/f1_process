from marshmallow import Schema, fields
import pandas as pd
from datetime import timedelta


class DQFailure(Exception):
    """
    Custom exception for data quality failures.

    Args:
        message (str): The error message to be displayed.
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)


class TimeValidator:
    """
    Validator for time values.

    Methods:
        validate_time(value): Validates that the value is a non-null timedelta
                              object.
    """
    @staticmethod
    def validate_time(value: any) -> timedelta:
        """
        Validates that the value is a non-null timedelta object.

        Args:
            value (any): The value to validate.

        Returns:
            timedelta: The validated timedelta object.

        Raises:
            DQFailure: If the value is None, NaN, or not a timedelta object.
        """
        if ((value is None or pd.isna(value)
             or not isinstance(value, timedelta))):
            raise DQFailure("Invalid time format: "
                            "value is None or NaN! or not a timedelta object!")
        return value


class NameValidator:
    """
    Validator for driver names.

    Methods:
        validate_driver(value): Validates that the value is a non-null,
                                non-empty string.
    """
    @staticmethod
    def validate_driver(value: any) -> str:
        """
        Validates that the value is a non-null, non-empty string.

        Args:
            value (any): The value to validate.

        Returns:
            str: The validated string.

        Raises:
            DQFailure: If the value is None, NaN, not a string, or is
                       empty/whitespace.
        """
        if ((value is None or pd.isna(value))
            or (not isinstance(value, str))
                or (value.strip() == "")):
            raise DQFailure("Invalid driver name: value is None or NaN"
                            "or not a string or is empty or whitespace!")
        return value


class DriverInputSchema(Schema):
    """
    Schema for validating driver input data.

    Fields:
        driver (fields.String): The name of the driver, validated by
                                NameValidator.

        time (fields.Field): The time value, validated by TimeValidator.
    """
    driver = fields.String(
        required=True,
        validate=NameValidator.validate_driver
    )

    time = fields.Field(
        required=True,
        validate=TimeValidator.validate_time
    )


def validity_and_completeness(data: pd.DataFrame,
                              schema_name: str) -> None:
    """
    Validates each row in the DataFrame against the specified schema.

    Args:
        data (pd.DataFrame): The DataFrame to validate.

        schema_name (str): The name of the schema to use for validation.

    Raises:
        DQFailure: If any row in the DataFrame fails validation.
    """
    schema = globals()[schema_name]()

    for idx, row in data.iterrows():
        row_dict = row.to_dict()
        errors = schema.validate(row_dict)

        if errors:
            keys = {key: row_dict.get(key) for key in ('driver',)}
            raise DQFailure(
                message=(f"Invalid or incomplete data for {keys}. \n"
                         f"As per {schema_name}: {errors}")
            )


def main(data: pd.DataFrame,
         schema_name: str) -> None:
    """
    Validates each row in a DataFrame against a specified Marshmallow schema.

    Args:
        data (pd.DataFrame): The DataFrame to validate.

        schema_name (str): The name of the schema to use for validation.

    Raises:
        DQFailure: If any row in the DataFrame fails validation.
    """
    validity_and_completeness(data, schema_name)
