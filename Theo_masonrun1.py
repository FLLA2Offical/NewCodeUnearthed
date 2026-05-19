from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port,Direction
from pybricks.robotics import DriveBase
from pybricks.tools import multitask, run_task, wait


hub = PrimeHub()
leftWheel   = Motor(Port.B, Direction.COUNTERCLOCKWISE)
rightWheel  = Motor(Port.D, Direction.CLOCKWISE)
wheelsize   = 56
axletrackwidth = 100
#robot and robot initial settings
robot = DriveBase(leftWheel,rightWheel,wheelsize,axletrackwidth)
robot.settings(straight_speed=700,straight_acceleration=400,turn_rate=400,turn_acceleration=200 )

#left attachment motor
LAM = Motor(Port.F, Direction.COUNTERCLOCKWISE)
#right attachment motor
RAM = Motor(Port.A,Direction.COUNTERCLOCKWISE)

#Turn on Gyro Sensor if the hub is good, turn off if it is bad
robot.use_gyro(True)
hub.imu.reset_heading(0)

async def main():
   if hub.imu.ready():
        await robot.straight(650)
        await robot.straight(-280)
        await robot.straight(230)
        await wait(650)
        await LAM.run_time(1000,1050)
        await LAM.run_time(-400,1050)
        await robot.straight(300)
        await robot.straight(-100)
        await robot.turn(-45)
        await robot.straight(180)
        await robot.straight(-200)
        await robot.turn(45)
        await robot.straight(-700)


# Runs the main program from start to finish.
run_task(main())

