class Data:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def set_data(cls, data):
        day, month, year = data
        return cls(day, month, year)

    @staticmethod
    def get_data(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 1 <= year <= 9999:
                    return "Date valid"
                else:
                    return "Incorrect year"
            else:
                return "Incorrect month"
        else:
            return "Incorrect day"


data_1 = [12, 11, 2020]
d_1 = Data.set_data(data_1)
print(d_1.month)
print(Data.get_data(11, 7, 1999))
