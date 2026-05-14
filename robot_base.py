"""
robot_base.py — Single source of truth for robot setup and motion.
Based on official Pybricks v2.20.0 robotics documentation.

HOW TO USE IN A RUN FILE:
    from robot_base import robot, hub, RAM, LAM, straight, turn, arc, reset
    reset()
    straight(500)
    turn(90)
"""

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Stop
from pybricks.tools import wait

# ─────────────────────────────────────────────
# ROBOT PHYSICAL CONSTANTS
#
# HOW TO CALIBRATE (from official docs):
#   wheel_diameter: Run straight(1000) and measure actual distance.
#     - Traveled too short → decrease WHEEL_DIAMETER_MM
#     - Traveled too far   → increase WHEEL_DIAMETER_MM
#
#   axle_track: FIRST fix wheel_diameter above. Then run turn(360).
#     - Turned too little  → increase AXLE_TRACK_MM
#     - Turned too far     → decrease AXLE_TRACK_MM
# ─────────────────────────────────────────────
WHEEL_DIAMETER_MM = 56      # mm — measure or check tyre sidewall (e.g. "62.4 x 20" = 62.4mm dia)
AXLE_TRACK_MM     = 100     # mm — distance between the two wheel ground contact points

# ─────────────────────────────────────────────
# HARDWARE INIT
# ─────────────────────────────────────────────
hub = PrimeHub()

left_motor  = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E, Direction.CLOCKWISE)
RAM = Motor(Port.F)   # Right Attachment Motor
LAM = Motor(Port.B)   # Left Attachment Motor

robot = DriveBase(left_motor, right_motor, WHEEL_DIAMETER_MM, AXLE_TRACK_MM)

# ─────────────────────────────────────────────
# MOTION SETTINGS
# straight_acceleration can be a single value or a tuple (accel, decel)
# e.g. straight_acceleration=(400, 600) to ramp up slowly but brake fast
# ─────────────────────────────────────────────
robot.settings(
    straight_speed=600,         # mm/s
    straight_acceleration=400,  # mm/s²
    turn_rate=400,              # deg/s
    turn_acceleration=300,      # deg/s²
)

# ─────────────────────────────────────────────
# GYRO
# From docs: "Choose True to use the gyro sensor for turning and
# driving straight." Without this, heading uses encoders only.
#
# NOTE: If the hub is not mounted flat, set top_side and front_side
# in PrimeHub() so the correct rotation axis is used.
# ─────────────────────────────────────────────
robot.use_gyro(True)

# ─────────────────────────────────────────────
# PID TUNING
# distance_control and heading_control have the same methods as
# Motor control (pid, limits, target_tolerances, stall_tolerances).
# See: code.pybricks.com/static/docs/v2.20.0/pupdevices/motor.html
#
# DISTANCE CONTROL — accuracy of straight moves
#   kp: position error gain. Increase if robot consistently stops short.
#   ki: accumulated error gain. Increase if robot never quite reaches target.
#   kd: speed error gain (uses estimated speed, not raw encoder difference).
#        Increase if robot oscillates or overshoots at end of move.
#
# HEADING CONTROL — how straight the robot drives
#   kp: Increase if robot drifts. Too high = weaving.
#   ki: Removes persistent left/right heading bias. Keep small.
#   kd: Prevents overcorrection. Increase if robot swings side to side.
# ─────────────────────────────────────────────
# robot.distance_control.pid(
#     kp=2000,
#     ki=100,
#     kd=200,
# )

# robot.heading_control.pid(
#     kp=1400,
#     ki=60,
#     kd=500,
# )

# ─────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────

def reset():
    """
    Call at the very start of every run.

    From official docs: robot.reset() resets estimated distance and angle,
    calls stop(), and — when use_gyro(True) is set — also resets the gyro
    heading to the given angle (default 0). So we only need one call here.
    """
    robot.reset()   # stops motors + resets distance/angle + resets gyro heading to 0


def straight(distance_mm, then=Stop.HOLD):
    """
    Drive straight. Positive = forward, negative = backward.
    then=Stop.HOLD holds position after stopping (default).
    then=Stop.COAST lets motors spin free — use on last move of a run.
    """
    robot.straight(distance_mm, then=then)


def turn(angle_deg, then=Stop.HOLD):
    """
    Turn in place. Positive = right (clockwise), negative = left (counterclockwise).
    then=Stop.COAST on your last turn so the wheels don't fight you when picking up.
    """
    robot.turn(angle_deg, then=then)


def turn_to(target_heading, direction=-1, then=Stop.HOLD):
    """
    Turn to a specific absolute heading using the gyro.

    Args:
        target_heading : the heading you want to reach (degrees)
        direction      : -1 = turn LEFT (default), +1 = turn RIGHT
        then           : Stop behavior after turning

    How it works:
        Reads hub.imu.heading(), computes delta to target,
        then forces the turn in the requested direction.

    Examples:
        turn_to(179)        # turn LEFT to reach heading 179°
        turn_to(90, 1)      # turn RIGHT to reach heading 90°
        turn_to(0)          # turn LEFT back to starting heading
    """
    current = hub.imu.heading()
    delta = target_heading - current

    if direction == -1:
        # Force LEFT (counterclockwise = negative)
        # If delta is already negative we're good; if positive, subtract 360
        if delta > 0:
            delta -= 360
    else:
        # Force RIGHT (clockwise = positive)
        # If delta is already positive we're good; if negative, add 360
        if delta < 0:
            delta += 360

    robot.turn(delta, then=then)


def arc(radius_mm, angle_deg=None, distance_mm=None, then=Stop.HOLD):
    """
    Drive a curved arc (partial circle). From official docs:
      radius > 0 → curves RIGHT.  radius < 0 → curves LEFT.
      Specify either angle_deg OR distance_mm (not both).
        angle_deg   : how far to travel around the circle in degrees.
        distance_mm : how far to travel, measured at center of robot.
      Positive angle/distance = forward. Negative = reverse.

    Examples:
      arc(200, angle_deg=90)      # curve right, quarter circle, radius 200mm
      arc(-150, angle_deg=-45)    # curve left in reverse
      arc(300, distance_mm=400)   # curve right, 400mm along the arc
    """
    robot.arc(radius_mm, angle=angle_deg, distance=distance_mm, then=then)


# ─────────────────────────────────────────────
# CALIBRATION & TUNING GUIDE (from official docs)
#
# STEP 1 — WHEEL DIAMETER (do this first):
#   robot.straight(1000)
#   Measure actual distance traveled.
#   Adjust WHEEL_DIAMETER_MM proportionally:
#     new = old * (1000 / actual_distance)
#
# STEP 2 — AXLE TRACK (do this after wheel diameter is correct):
#   robot.turn(360)
#   Robot should end up facing the same direction.
#     Turned too little → increase AXLE_TRACK_MM
#     Turned too far    → decrease AXLE_TRACK_MM
#
# STEP 3 — HEADING PID (if robot drifts while driving straight):
#   Increase heading_control kp in small steps (e.g. 1400 → 1600 → 1800)
#   If it starts weaving, increase kd.
#
# STEP 4 — DISTANCE PID (if robot overshoots or oscillates at end of move):
#   Decrease distance_control kp. Increase kd to dampen oscillation.
#
# STEP 5 — GYRO NOTE (from docs):
#   "The gyro in each hub is a bit different, which can cause it to be a
#   few degrees off for big turns, or many small turns in the same direction.
#   For example, you may need to use turn(357) or turn(362) on your robot
#   to make a full turn."
#   → If your 90° turn consistently lands at 87°, use turn(93) to compensate.
#
# STEP 6 — LAST MOVE IN A RUN:
#   Use then=Stop.COAST on your final straight/turn so the robot doesn't
#   actively hold position after stopping (wheels won't fight you).
# ─────────────────────────────────────────────
