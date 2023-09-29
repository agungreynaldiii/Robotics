'''
Nama    : Agung Reynaldi Avizena
NIM     : 1103204044
'''

#methods 1
# from robot_control_class import RobotControl
# import time

# robotcontrol = RobotControl(robot_name="summit")

# def move_x_seconds(secs):
#     robotcontrol.move_straight()
#     time.sleep(secs)
#     robotcontrol.stop_robot()


# move_x_seconds(5)

#methods 2
# from robot_control_class import RobotControl

# robotcontrol = RobotControl(robot_name="summit")

# def get_laser_values(a,b,c):
#     r1 = robotcontrol.get_laser_summit(a)
#     r2 = robotcontrol.get_laser_summit(b)
#     r3 = robotcontrol.get_laser_summit(c)

#     return [r1, r2, r3]

# l = get_laser_values(0, 500, 1000)

# print ("Reading 1: ", l[0])
# print ("Reading 2: ", l[1])
# print ("Reading 3: ", l[2])

#methods 3
# from robot_control_class import RobotControl

# robotcontrol = RobotControl(robot_name="summit")

# robotcontrol.move_straight_time("forward", 0.3, 5)
# robotcontrol.turn("clockwise", 0.3, 7)

#methods 4
from robot_control_class import RobotControl

robotcontrol = RobotControl(robot_name="summit")

robotcontrol.turn("counter-clockwise", 0.3, 4)
robotcontrol.move_straight_time("forward", 0.3, 6)
robotcontrol.turn("counter-clockwise", 0.3, 4)
robotcontrol.move_straight_time("forward", 0.3, 7)