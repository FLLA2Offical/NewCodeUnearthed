from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port,Direction
from pybricks.robotics import DriveBase
from pybricks.tools import multitask, run_task, wait

#Team 69309 and 69310 starter code V2
hub = PrimeHub()
#Please make sure all the robot info in correct
leftWheel   = Motor(Port.A, Direction.COUNTERCLOCKWISE)
rightWheel  = Motor(Port.E, Direction.CLOCKWISE)
wheelsize   = 56
axletrackwidth = 100
#robot and robot initial settings
robot = DriveBase(leftWheel,rightWheel,wheelsize,axletrackwidth)
robot.settings(straight_speed=900,straight_acceleration=500,turn_rate=600,turn_acceleration=300)


#left attachment motor
LAM = Motor(Port.B, Direction.COUNTERCLOCKWISE)
#right attachment motor
RAM = Motor(Port.F,Direction.COUNTERCLOCKWISE)

#Turn on Gyro Sensor if the hub is good, turn off if it is bad
robot.use_gyro(True)
hub.imu.reset_heading(0)

async def main():
   if hub.imu.ready():
# Runs the main program from start to finish.
    await robot.straight(560)#Goes to M12 and do M15 (10 points)
    await robot.turn(10)
    await RAM.run_time(250,2000)#Smashes  into gears on M11
    await LAM.run_time(-1000,1500)#Turns gears on M11 (30 points)
    await RAM.run_time(-250,2000)#Swings arm back
    await multitask (robot.straight(-840), RAM.run_time(-1000,2000))#Returns to home, pulls back sand (20 points)








run_task(main())