alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digit = "0123456789"

def cek_nama(nama_input):
    posisi = "q0"
    print("Input:", nama_input)

    for karakter in nama_input:
        posisi_awal = posisi

        if posisi == "q0":
            if karakter in alphabet or karakter == "_":
                posisi = "q1"
            else:
                posisi = "DEAD"

        elif posisi == "q1":
            if karakter in alphabet or karakter in digit or karakter == "_":
                posisi = "q1"
            else:
                posisi = "DEAD"

        else:
            posisi = "DEAD"

        print(" ", posisi_awal, "--", karakter, "-->", posisi)

    if posisi == "q1":
        print("  Hasil: VALID")
    else:
        print("  Hasil: TIDAK VALID")
        
    print()

while True:
    masukan = input("Masukkan nama (Enter untuk keluar): ")

    if masukan == "":
        break

    cek_nama(masukan)
