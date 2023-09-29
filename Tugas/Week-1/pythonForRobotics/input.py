'''
Nama    : Agung Reynaldi Avizena
NIM     : 1103204044
'''
# name = input("What's your name? ")

# print("Nice to meet you, " + name) #menampilkan output
# age = input("What's your age? ") #meminta input

# age2 = int(age) + 1 #menambahkan input dengan + 1

# print("So next year you will be %d years old!" %age2) #menampilkan output

# from robot_control_class import RobotControl

# num = int(input("Select a number between 0 and 719: "))

# rc = RobotControl()
# a = rc.get_laser(num)

# print ("The laser value received is: ", a)

# Meminta pengguna untuk memasukkan film favorit mereka
film = input("Apa film favorit Anda? ")

# Memeriksa input dan memberikan respon yang berbeda berdasarkan film yang dipilih
if film == "Avengers Endgame" or film == "Titanic":
    print("Pilihan yang bagus!") # Jika input adalah "Avengers Endgame" atau "Titanic"
elif film == "Star Wars":
    print("Juga pilihan yang bagus!") # Jika input adalah "Star Wars"
else:
    print("Anda memang spesimen yang menarik") # Untuk input lainnya
