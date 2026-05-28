"""
Run1.py — Mission 5, 6, 7
Uses robot_base.py for all hardware, PID, and gyro settings.
"""

from robot_base import robot, hub, RAM, LAM, reset, straight, turn, arc
from pybricks.tools import wait
from pybricks.parameters import Stop

# Reset encoders + heading at the start of every run
reset()

# Mission 3,4

straight(800)
turn(180)
straight(-100)
straight(125)
turn(-90)
straight(175)
wait(100)
turn(45)
straight(-100)
turn(-45)
straight(-100)
straight(25)
LAM.run_time(-200, 600) #make the claw open
LAM.run_time(200, 500)
LAM.run_time(-200, 500)
RAM.run_time(1500, 1500) #make the arm go down
turn(-10)
straight(180)
straight(-15)
LAM.run_time(150, 1020, Stop.HOLD) #make the claw close
wait(100)
turn(-10)
RAM.run_time(-1500, 1005, Stop.HOLD) #make the arm go up
wait(100)
turn(5)
straight(-130)
turn(50)
RAM.run_time(1500, 1000) #make the arm go down
straight(400)
RAM.run_time(-1500, 1005, Stop.HOLD) #make the arm go up
arc(240, -120)
straight(-600)
