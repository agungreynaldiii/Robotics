'''
Nama    : Agung Reynaldi Avizena
NIM     : 1103204044
'''
# Mengimpor kelas RobotControl dari modul robot_control_class
from robot_control_class import RobotControl

# Membuat instance dari kelas RobotControl
robotcontrol = RobotControl()

# Mendapatkan nilai dari sensor laser pada sudut 360 derajat
a = robotcontrol.get_laser(360)

# Memeriksa apakah nilai sensor laser kurang dari 1
if a < 1:
    # Jika ya, maka hentikan robot
    robotcontrol.stop_robot()
else:
    # Jika tidak, maka gerakkan robot maju
    robotcontrol.move_straight()

# Mencetak nilai sensor laser
print("The laser value received was:", a)
