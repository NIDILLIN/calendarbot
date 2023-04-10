import datetime
from datetime import timedelta


class Calculator:
    @classmethod
    def calc_diff(
            self, 
            first_date: datetime.date, 
            last_date: datetime.date
            ) -> int:
        delta = last_date - first_date
        return delta.days
    
    @classmethod
    def calc_last_date(
            self,
            first_date: datetime.date,
            days: int
            ) -> datetime.date:
        last_date = first_date + timedelta(days=days)
        return last_date