from datetime import datetime


def get_days_from_today(date_string: str) -> int | str:
    """
    Calculates the number of days between today and a given date.

    Parameters:
        date_string (str): Date in 'YYYY-MM-DD' format.

    Returns:
        int: Number of days between today and the given date.
             The value can be negative if the date is in the future.
        str: Error message if the date format is invalid.
    """
    try:
        # Parse the input date string into a datetime object
        start_date = datetime.strptime(date_string, "%Y-%m-%d")

        # Get the current date and time
        today = datetime.today()

        # Calculate the difference between dates
        date_difference = today - start_date

        # Return the number of days as an integer
        return date_difference.days

    except ValueError:
        # Handle incorrect date format
        return "Invalid date format. Please use 'YYYY-MM-DD'."
