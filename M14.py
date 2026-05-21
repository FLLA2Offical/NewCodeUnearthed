
"""
Mission 14-Forum
Uses robot_base.py for all hardware, PID, and gyro settings.
"""

from robot_base import robot, hub, RAM, LAM, reset, straight, turn, turn_to, arc
from pybricks.tools import wait
from pybricks.parameters import Stop

# Reset encoders + heading at the start of every run
reset()
straight(-10), #LAM.run_time(1000,1000)
arc(-1000, angle_deg=45)
turn_to(-90)
straight(650)
arc(-250, angle_deg=55)
straight(15)
LAM.run_time(-1000,1000)
arc(-250, angle_deg=-55)
