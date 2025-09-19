class Distance:
    units = {
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{round(self.value,2)} {self.unit}"

    def __add__(self, other):
        self_m = self.value * Distance.units[self.unit]
        other_m = other.value * Distance.units[other.unit]
        total = self_m + other_m
        return Distance(total, "m")

    def __sub__(self, other):
        self_m = self.value * Distance.units[self.unit]
        other_m = other.value * Distance.units[other.unit]
        total = self_m - other_m
        return Distance(total, "m")

    def convert(self, unit):
        value_in_m = self.value * Distance.units[self.unit]
        return value_in_m / Distance.units[unit]