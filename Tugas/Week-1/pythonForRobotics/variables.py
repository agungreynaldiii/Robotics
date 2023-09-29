'''
Nama    : Agung Reynaldi Avizena
NIM     : 1103204044
'''
# Mengimpor kelas RobotControl dari modul robot_control_class
from robot_control_class import RobotControl

# Membuat instance dari kelas RobotControl
robotcontrol = RobotControl()

# Mendapatkan nilai dari sensor laser pada sudut 0 derajat
laser1 = robotcontrol.get_laser(0)
print("The laser value received at 0 degrees is:", laser1)

# Mendapatkan nilai dari sensor laser pada sudut 360 derajat
laser2 = robotcontrol.get_laser(360)
print("The laser value received at 360 degrees is:", laser2)

# Mendapatkan nilai dari sensor laser pada sudut 719 derajat
laser3 = robotcontrol.get_laser(719)
print("The laser value received at 719 degrees is:", laser3)
