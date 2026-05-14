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
arc(-160, angle_deg=45 )
straight(400)
LAM.run_time(-1000,10000)
RAM.run_time(1500, 1000, Stop.HOLD) #make the drop the arm
straight(-120)
straight(15)
RAM.run_time(-1500, 1000, Stop.HOLD) #make the drop the arm
