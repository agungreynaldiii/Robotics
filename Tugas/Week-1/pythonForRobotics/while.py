'''
Nama    : Agung Reynaldi Avizena
NIM     : 1103204044
Tugas ke - a
'''
# Mengimpor kelas RobotControl dari modul robot_control_class
from robot_control_class import RobotControl

# Membuat instance dari kelas RobotControl
robotcontrol = RobotControl()

# Mendapatkan data dari sensor laser pada sudut 360 derajat
a = robotcontrol.get_laser(360)

# Looping untuk terus bergerak ke depan selama jarak ke tembok masih lebih dari 1 meter
while a > 1:
    # Memerintahkan robot untuk bergerak ke depan
    robotcontrol.move_straight()
    
    # Mendapatkan data laser kembali setelah bergerak
    a = robotcontrol.get_laser(360)
    
    # Mencetak jarak ke tembok saat ini
    print ("Current distance to wall: %f" % a)

# Menghentikan robot setelah loop selesai
robotcontrol.stop_robot()

# Menampilkan pesan bahwa robot telah berhenti karena jarak ke tembok sudah kurang dari atau sama dengan 1 meter
print ("Wall is at %f meters! Stop the robot!" % a)
