'''
Nama    : Agung Reynaldi Avizena
NIM     : 1103204044
'''
# Mengimpor kelas RobotControl dari modul robot_control_class
from robot_control_class import RobotControl

# Membuat instance dari kelas RobotControl
rc = RobotControl()

# Mendapatkan data dari sensor laser pada seluruh titik
l = rc.get_laser_full()

# Mencetak nilai sensor laser pada posisi tertentu
print("Position 0:", l[0])
print("Position 360:", l[360])
print("Position 719:", l[719])
