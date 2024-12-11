"""
This module contains common utility functions used in project
"""
from datetime import datetime
from dateutil.relativedelta import relativedelta


class date_utils:
    """
    This class contains date related utility functions.
    """

    def calculate_date_difference(self, date1_str, date2_str):
        # Parse the input strings into datetime objects
        date1 = datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.strptime(date2_str, "%Y-%m-%d")

        # Calculate the difference using relativedelta
        difference = relativedelta(date2, date1)

        # Extract years , months and days
        response = {'years': difference.years, 'months': difference.months, 'days': difference.days}

        return response


