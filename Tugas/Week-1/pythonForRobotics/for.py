'''
Nama    : Agung Reynaldi Avizena
NIM     : 1103204044
'''

# Mengimpor kelas RobotControl dari modul robot_control_class
from robot_control_class import RobotControl

# Membuat instance dari kelas RobotControl
robotcontrol = RobotControl()

# Mendapatkan data dari sensor laser pada seluruh titik
l = robotcontrol.get_laser_full()

# Inisialisasi variabel 'maxim' sebagai 0 untuk menyimpan nilai tertinggi
maxim = 0

# Iterasi melalui setiap nilai dalam daftar 'l'
for value in l:
    # Memeriksa apakah nilai saat ini lebih besar dari nilai tertinggi yang telah ditemukan sebelumnya
    if value > maxim:
        # Jika ya, maka perbarui nilai tertinggi
        maxim = value

# Mencetak nilai tertinggi yang ditemukan
print("The higher value in the list is:", maxim)
