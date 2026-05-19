"""
Run1.py — Mission 5, 6, 7
Uses robot_base.py for all hardware, PID, and gyro settings.
"""

from robot_base import robot, hub, RAM, LAM, reset, straight, turn, turn_to, arc
from pybricks.tools import wait
from pybricks.parameters import Stop

# Reset encoders + heading at the start of every run
reset()

# Mission 9,10
straight(-10)
arc(-55, angle_deg=50 )
straight(550)
LAM.run_time(-1000,1800)
RAM.run_time(1500, 1000, Stop.HOLD) #make the drop the arm
straight(-130)
straight(15)
RAM.run_time(-1500, 1000, Stop.HOLD) #make the drop the arm
turn(-45)
straight(500)
