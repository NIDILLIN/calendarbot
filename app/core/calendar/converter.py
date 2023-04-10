import datetime


class Converter:
    @classmethod
    def convert(self, string: str) -> datetime.date:
        "21.04.2023"
        "21 04 2023"
        "21.04.23"

        if '.' in string:
            symbols = string.split('.')
        else:
            symbols = string.split(' ')

        numbers = [int(num) 
                   for num in symbols]
        
        day = numbers[0]
        month = numbers[1]
        year = numbers[2]
        if year < 2000:
            year += 2000

        return datetime.date(year, month, day)
    
    @classmethod
    def normalize(self, date: datetime.date) -> str:
        day = date.day
        month = date.month
        year = date.year
        if day < 10:
            day = f'0{day}'
        if month < 10:
            month = f'0{month}'
        return f'{day}.{month}.{year}'

    