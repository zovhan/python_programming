for i in range ("a"):
    nama = (input("masukan nama siswa / siswi: "))
    tugas1 = float (input("masukan tugas nilai ke 1 anda: "))
    tugas2 = float (input("masukan tugas nilai ke 2 anda: "))
    tugas3 = float (input("masukan tugas nilai ke 3 anda: "))

b = 3

all =tugas1 + tugas2 + tugas3

avv = all // b

if  avv >=70:
    print("selamat kamu lulus")
   
elif avv >= 50 and avv <=69:
   print ("anda harus perbaikan")

elif avv <50:
   print ("anda tidak lulus")

else:

    print("anda tidak lulus,jangan lupa belajar lagi ya")
print("selamat", nama, "nilai rata rata kamu = ", avv, "semangat belajarnya ya")