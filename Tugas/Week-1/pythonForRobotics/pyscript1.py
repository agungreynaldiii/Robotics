'''
Nama    : Agung Reynaldi Avizena
NIM     : 1103204044
'''
# Mengimpor kelas RobotControl dari modul robot_control_class
from robot_control_class import RobotControl

# Membuat instance dari kelas RobotControl
rc = RobotControl()

# Mendapatkan nilai dari sensor laser pada sudut 360 derajat
a = rc.get_laser(360)

# Mencetak jarak yang diukur
print("The distance measured is:", a, "m.")
