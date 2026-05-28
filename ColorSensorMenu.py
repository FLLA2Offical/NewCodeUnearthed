from pybricks.pupdevices import ColorSensor, Motor
from pybricks.parameters import Port, Color, Direction, Button
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait


# Hub & devices
hub = PrimeHub()
sensor = ColorSensor(Port.C)


# --------------------------------------------------
# Wait for RIGHT button press
# --------------------------------------------------
def wait_for_right_button():
    while Button.RIGHT not in hub.buttons.pressed():
        wait(20)

    while Button.RIGHT in hub.buttons.pressed():
        wait(20)


# --------------------------------------------------
# Wait for LEFT button press
# --------------------------------------------------
def wait_for_left_button():
    while Button.LEFT not in hub.buttons.pressed():
        wait(20)

    while Button.LEFT in hub.buttons.pressed():
        wait(20)


# --------------------------------------------------
# Color detection + safe run
# --------------------------------------------------
def check_color_and_run():

    detected = sensor.color()

    if detected == Color.BLUE:
        hub.light.on(Color.BLUE)
        hub.display.number(12)

        # choose run with button
        if Button.RIGHT in hub.buttons.pressed():
            wait_for_right_button()
            import Run_1

        elif Button.LEFT in hub.buttons.pressed():
            wait_for_left_button()
            import Run_2


    elif detected == Color.RED:
        hub.light.on(Color.RED)
        hub.display.number(3)
        wait_for_right_button()
        import Run_3


    elif detected == Color.GREEN:
        hub.light.on(Color.GREEN)
        hub.display.number(4)
        wait_for_right_button()
        import Run_4


    elif detected == Color.YELLOW:
        hub.light.on(Color.YELLOW)
        hub.display.number(5)
        wait_for_right_button()
        import Run_5


# --------------------------------------------------
# Main loop
# --------------------------------------------------
while True:
    check_color_and_run()
    wait(100)
