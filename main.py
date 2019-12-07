#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Satellite mission
class Robot:
    def __init__(self,leftMotor,rightMotor,lightSensor,gyroSensor):
        self.drivebase = DriveBase(left,rightMotor,56,105)
        self.lightSensor = lightSensor

    def driveForward(self,time):
        self.drivebase.drive_time(300,0,time*100)

    def driveTillBlack(self,speed)
        self.drivebase.drive(speed(100,0))
        while self.lightSensor.reflection() > 10:
            wait(10)
        self.drivebase.stop()
    #calibrate light sensor
    def calibrate()
        print("calibrate robot")
