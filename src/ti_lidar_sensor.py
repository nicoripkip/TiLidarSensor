import rospy
import math
import smbus
import json


SPEED_OF_LIGHT = 299792458
I2C_MAX_CHUNK_LIMIT = 32
I2C_START_REGISTER = 0x59
I2C_BLOCK_LENGTH = 9


class LidarSensor:
    def __init__(self, slave_address):
        self.slave_address = slave_address
        
        # default values
        self.measured_time = 0
        self.frequency = 0
        self.angle = 0

        # calculates values
        self.data_raw = None
        self.distance = 0
        self.diameter = 0


    #
    # TF-Luna distance calculation
    # d = (c / 2) * (1 / 2 * pi * f) * d_phi
    #    
    def calculate_distance():
        self.distance = (SPEED_OF_LIGHT / 2) * (1 / 2*math.pi*self.frequency) * self.measured_time


    def calculate_diameter():
        self.diameter = 2 * self.distance * math.tan(self.angle)


    def get_distance():
        return self.distance


    def get_raw_data():
        return self.data_raw

    #
    # TF-Luna communication protocol:
    # - I2C
    #
    def read_data(bus, slave_address):
        buff = {}

        try:
            bus.write_byte(slave_address, 0x01)
            block = bus.read_i2c_block_data(slave, I2C_START_REGISTER, I2C_BLOCK_LENGTH)
            
            if block[0] == 0x59 and block[1] == 0x59:
                buff = {
                    "distance": block[2] + block[3] * 256,
                    "strength": block[4] + block[5] * 256,
                    "temperature": block[6] + block[7] * 256
                }
            else:
                rospy.logerror("Can't read the data")

        except Exception as e:
            rospy.logerror(f"{e}")

        return buff


    def send_data(bus, slave_address, buff):
        pass


    def get_firmware_version():
        pass
