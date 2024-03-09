class Measurements:
    def __init__(self, pressure: float, hours_of_day:int, temperature:int):
        self.__pressure = pressure
        self.__hours_of_day = hours_of_day
        self.__temperature = temperature

    def get_pressure(self):
        return self.__pressure

    def get_hours_of_day(self):
        return self.__hours_of_day

    def get_temperature(self):
        return self.__temperature

    def set_pressure(self, pressure):
        self.__pressure = pressure

    def set_hours_of_day(self, hours_of_day):
        self.__hours_of_day = hours_of_day

    def set_temperature(self, temperature):
        self.__temperature = temperature

    def __str__(self):
        return "Pressure: " + str(self.__pressure) +"\n" + "Temperature:" + str(self.__temperature) + "\n" + "Hours of day: " + str(self.__hours_of_day)

    def __repr__(self):
        return str(self)
