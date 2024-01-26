

import math


SPEED_OF_LIGHT = 299792458


class LidarSensor:
    def __init__(self, slave_address):
        self.slave_address = slave_address
        self.measured_time = 0
        self.frequency = 0

    #
    # TF-Luna distance calculation
    # d = (c / 2) * (1 / 2 * pi * f) * d_phi
    #    
    def get_distance():
        return (SPEED_OF_LIGHT / 2) * (1 / 2*math.pi*self.frequency) * self.measured_time


    def get_raw_data():
        pass

    #
    # TF-Luna communication protocol:
    # - I2C
    #
    def read_sensor():
        pass
