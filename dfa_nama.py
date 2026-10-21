huruf = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
angka = "0123456789"

def periksa(teks):
    state = "q0"
    print("Input:", teks)
    for c in teks:
        lama = state

        if state == "q0":
            if c in huruf or c == "_":
                state = "q1"
            else:
                state = "DEAD"
        elif state == "q1":
            if c in huruf or c in angka or c == "_":
                state = "q1"
            else:
                state = "DEAD"
        else:
            state = "DEAD"
        print(" ", lama, "--", c, "-->", state)

    if state == "q1":
        print("  Hasil: VALID")
    else:
        print("  Hasil: TIDAK VALID")
    print()
    
while True:
    s = input("Masukkan nama (kosongkan lalu Enter untuk keluar): ")
    if s == "":
        break
    periksa(s)
