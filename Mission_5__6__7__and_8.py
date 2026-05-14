"""
Run1.py — Mission 5, 6, 7
Uses robot_base.py for all hardware, PID, and gyro settings.
"""

from robot_base import robot, hub, RAM, LAM, reset, straight, turn, turn_to, arc
from pybricks.tools import wait
from pybricks.parameters import Stop

# Reset encoders + heading at the start of every run
reset()

# Mission 5, 6, 7




arc(-950, angle_deg=22 )
turn(25)
straight(350)

RAM.run_time(-1500, 1000, Stop.HOLD) #make the drop the arm 
straight(50)
RAM.run_time(1500, 1000, Stop.HOLD) #make the drop the arm 

straight(-15)
turn(-30)


straight(-61)
turn_to(-90)   # reads current heading, turns LEFT to reach 179°



straight(-172)
LAM.run_time(-1500, 1000) #make the drop the arm 
LAM.run_time(1500, 1000) #make the arm go up
LAM.run_time(-1500, 1000) #make the arm go down
LAM.run_time(1500, 1000) #make the arm go up

arc(-250, angle_deg=142 )
straight(300)