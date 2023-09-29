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

# Membuat kamus (dictionary) dengan beberapa titik dan nilai dari sensor laser
dict = {"P0": l[0], "P100": l[100], "P200": l[200], "P300": l[300], "P400": l[400], "P500": l[500], "P600": l[600], "P719": l[719]}

# Mencetak
print(dict)
