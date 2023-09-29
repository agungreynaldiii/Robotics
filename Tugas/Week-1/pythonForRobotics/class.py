'''
Nama    : Agung Reynaldi Avizena
NIM     : 1103204044
'''
# Mengimpor kelas RobotControl dari modul robot_control_class
from robot_control_class import RobotControl

# Mendefinisikan kelas MoveRobot
class MoveRobot:
    def __init__(self, motion, clockwise, speed, time):
        # Membuat instance dari kelas RobotControl dengan nama "summit"
        self.robotcontrol = RobotControl(robot_name="summit")
        self.motion = motion
        self.clockwise = clockwise
        self.speed = speed
        self.time = time
        self.time_turn = 7.0  # Estimasi waktu untuk melakukan rotasi 90 derajat

    # Metode untuk membuat robot melakukan gerakan persegi
    def do_square(self):
        i = 0
        while i < 4:
            # Memanggil metode move_straight untuk bergerak maju
            self.move_straight()
            
            # Memanggil metode turn untuk memutar robot
            self.turn()
            i += 1

    # Metode untuk membuat robot bergerak lurus
    def move_straight(self):
        # Memanggil metode move_straight_time dari kelas RobotControl
        self.robotcontrol.move_straight_time(self.motion, self.speed, self.time)

    # Metode untuk membuat robot berputar
    def turn(self):
        # Memanggil metode turn dari kelas RobotControl
        self.robotcontrol.turn(self.clockwise, self.speed, self.time_turn)

# Membuat instance dari MoveRobot dengan parameter tertentu
mr1 = MoveRobot('forward', 'clockwise', 0.3, 4)

# Memanggil metode do_square untuk membuat robot melakukan gerakan persegi
mr1.do_square()

# Membuat instance baru dengan parameter berbeda
mr2 = MoveRobot('forward', 'clockwise', 0.3, 8)

# Memanggil metode do_square lagi untuk membuat robot melakukan gerakan persegi dengan parameter baru
mr2.do_square()
