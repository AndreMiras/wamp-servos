#!/usr/bin/env python2
from __future__ import print_function
from __future__ import unicode_literals
import time
import serial


device = "/dev/ttyACM0"
baud_rates = [9600, 19200, 38400, 57600, 115200, 128000]
PULSE_WIDTH_MIN = 500
PULSE_WIDTH_MAX = 2500


def serial_conf():
    baud_rates.sort()
    # use the highest baud rate
    baud = baud_rates[-1]
    ser = serial.Serial(device, baud)
    time.sleep(0.5)
    return ser


def send_command(ser, command):
    servo_end_command = "\r\n"
    print("command:", command)
    full_command = (command + servo_end_command).encode()
    ser.write(full_command)


def prepare_move_one(servo_num, servo_pos, servo_speed):
    """
    Prepares "move_one" command.
    Used for moving one servo at a time.
    """
    servo_channel = "#" + str(servo_num)
    servo_position = "P" + str(servo_pos)
    servo_time_execution = "T" + str(servo_speed)
    servo_command = servo_channel + servo_position + servo_time_execution
    return servo_command


def move_one(ser, servo_num, servo_pos, servo_speed):
    """
    Moves one servo at a time.
    """
    servo_command = prepare_move_one(servo_num, servo_pos, servo_speed)
    send_command(ser, servo_command)


def main():
    """
    Moves the first servo from its minimum positon to its maximum one.
    """
    ser = serial_conf()
    servo_num = 1
    servo_speed = 500
    step = 100
    for servo_pos in range(PULSE_WIDTH_MIN, PULSE_WIDTH_MAX+1, step):
        move_one(ser, servo_num, servo_pos, servo_speed)
        # waits for for the first order to finish
        # before processing the next one
        time.sleep(servo_speed / 1000.0)


if __name__ == "__main__":
    main()
