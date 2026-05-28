"""

Uses robot_base.py for all hardware, PID, and gyro settings.
"""

from robot_base import robot, hub, RAM, LAM, reset, straight, turn, arc
from pybricks.tools import wait
from pybricks.parameters import Stop

# Reset encoders + heading at the start of every run
reset()

# Mission 3,4

straight(600)
turn(180)
straight(-300)
straight(20)
turn(-90)
LAM.run_time(-200, 500) #make the claw open
RAM.run_time(1500, 1500) #make the arm go down
turn(-5)
straight(180)
straight(-15)
LAM.run_time(200, 920, Stop.HOLD) #make the claw close
RAM.run_time(-1500, 1005, Stop.HOLD) #make the arm go up
straight(-130)
turn(44)
RAM.run_time(1500, 1000) #make the arm go down
straight(400)
RAM.run_time(-1500, 1005, Stop.HOLD) #make the arm go up
arc(240, -120)
straight(-600)
