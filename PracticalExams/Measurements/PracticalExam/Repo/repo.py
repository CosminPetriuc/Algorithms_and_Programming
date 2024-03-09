from Domain.domain import Measurements
class MeasurentsRepository:
    def __init__(self):
        self.__Measurement = []

    def PrintAll(self):
        return self.__Measurement

    def AddMeasurement(self, pressure, hours_of_day, temperature):

        '''Adds a new measurement to the list of measurements.
        Parameters:
        - pressure(float): The pressure measurement to be added.Should be between 0 and 10.
        - hours_of_day(int): The hours of the day when the measurement was taken.Should be between 0 and 23.
        - temperature(float): The temperature measurement to be added.Should be between 0 and 100.
        Raises:
        - ValueError: If any of the input parameters are invalid.
        '''
        if pressure < 0 or pressure > 10 and hours_of_day < 0 or hours_of_day > 23 and temperature < 0 or temperature > 100:
            raise ValueError("Invalid measurement")
        measurement = Measurements(pressure, hours_of_day, temperature)
        self.__Measurement.append(measurement)

    def DisplayMeasurementsHigher(self, value):
        '''Returns a list of all the measurements with the pressure higher than a given value.
        Parameters:
        - value(float): The value to compare the pressure to.
        '''
        return [measurement for measurement in self.__Measurement if measurement.get_pressure() > value]

    def DisplayTheAverage(self, hours_of_day):
        return [measurement for measurement in self.__Measurement if measurement.get_hours_of_day() == hours_of_day]

