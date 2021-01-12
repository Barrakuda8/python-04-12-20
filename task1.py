class Date:

    @classmethod
    def int_date(cls, date):
        date = date.split("-")
        return [int(date[0]), int(date[1]), int(date[2])]

    @staticmethod
    def check_date(date):
        day, month, year = date
        days_count = {(1, 3, 7, 8, 10, 12): 31, (4, 6, 9, 11): 30, 2: [28, 29], 5: 32}
        if 1 <= month <= 12:
            for key, value in days_count.items():
                if month in key:
                    if month == 2:
                        if year % 4 == 0:
                            value = value[1]
                        else:
                            value = value[0]
                    if 1 <= day <= value:
                        return day, month, year
                    else:
                        print(f"В данном месяце дней: {value}")
                    break
        else:
            print("Месяцев всего 12")

    def __init__(self, date):
        date = self.check_date(self.int_date(date))
        if date:
            self.day, self.month, self.year = date


date_a = Date("30-11-1997")
date_b = Date("31-11-1997")
date_c = Date("00-11-1997")
date_d = Date("30-13-1997")
date_e = Date("30-00-1997")
