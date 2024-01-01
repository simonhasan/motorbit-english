from microbit import *


class MOTORBIT(object):
    """Motor:bit driver class
    """

    def __init__(self):
        i2c.init()
        self.__left_io = pin8
        self.__left_pwm = pin1
        self.__right_io = pin12
        self.__right_pwm = pin2

    def set_motors_speed(self, m1_speed: int, m2_speed: int):
        """Set the speed of the left and right motors, in the range of -100 to 100
        :param m1_speed: Left speed -100 to 100
        :param m2_speed: Right speed -100 t0 100
        :return: none
        """
        if m1_speed > 100 or m1_speed < -100:
            raise ValueError('speed error,-100~100')
        if m2_speed > 100 or m2_speed < -100:
            raise ValueError('speed error,-100~100')
        if m1_speed > 0:
            self.__left_io.write_digital(0)
            self.__left_pwm.write_analog(m1_speed * 1023 / 100)
        else:
            self.__left_io.write_digital(1)
            self.__left_pwm.write_analog(-m1_speed * 1023 / 100)
        if m2_speed > 0:
            self.__right_io.write_digital(1)
            self.__right_pwm.write_analog(m2_speed * 1023 / 100)
        else:
            self.__right_io.write_digital(0)
            self.__right_pwm.write_analog(-m2_speed * 1023 / 100)


if __name__ == '__main__':
    tp = MOTORBIT()

    tp.set_motors_speed(1, 100)