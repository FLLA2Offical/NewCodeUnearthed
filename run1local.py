from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port,Direction
from pybricks.robotics import DriveBase
from pybricks.tools import multitask, run_task, wait

hub = PrimeHub()
leftWheel   = Motor(Port.A, Direction.COUNTERCLOCKWISE)
rightWheel  = Motor(Port.E, Direction.CLOCKWISE)
wheelsize   = 55
axletrackwidth = 96
#robot and robot initial settings
robot = DriveBase(leftWheel,rightWheel,wheelsize,axletrackwidth)
robot.settings(straight_speed=410,straight_acceleration=700,turn_rate=400,turn_acceleration=700 )

#left attachment motor
LAM = Motor(Port.B, Direction.COUNTERCLOCKWISE)
#right attachment motor
RAM = Motor(Port.F,Direction.CLOCKWISE)

#Turn on Gyro Sensor if the hub is good, turn off if it is bad
robot.use_gyro(True)
hub.imu.reset_heading(0)

async def main():
    if hub.imu.ready():
        #await LAM.run_time(1000,3000)
        #await robot.straight(-10)
        #await robot.straight(10)
        await robot.straight(580)
        wait(500)
        await robot.straight(70)
        await robot.straight(-120)
        await robot.straight(100)
        await robot.straight(-20)
        await robot.straight(-10)
        await robot.straight(-15)
        await LAM.run_time(-500,1000)
        await robot.straight(-10)
        await robot.turn(-35)
        await robot.straight(100)
        await robot.turn(3)
        await robot.straight(100)
        await RAM.run_time(-500,1000)
        await robot.straight(-270)
        await robot.turn(33)
        await robot.straight(-600)
        await robot.turn(-33)


run_task(main())