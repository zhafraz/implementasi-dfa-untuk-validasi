angka = "0123456789"

def periksa(teks):
    state = "q0"                    
    print("Input:", teks)

    for c in teks:                   
        lama = state

        if state == "q0":
            if c in angka:
                state = "q1"
            else:
                state = "DEAD"

        elif state == "q1":
            if c in angka:
                state = "q1"
            elif c == ".":
                state = "q2"
            elif c == "E" or c == "e":
                state = "q4"
            else:
                state = "DEAD"

        elif state == "q2":
            if c in angka:
                state = "q3"
            else:
                state = "DEAD"

        elif state == "q3":
            if c in angka:
                state = "q3"
            elif c == "E" or c == "e":
                state = "q4"
            else:
                state = "DEAD"

        elif state == "q4":
            if c == "+" or c == "-":
                state = "q5"
            elif c in angka:
                state = "q6"
            else:
                state = "DEAD"

        elif state == "q5":
            if c in angka:
                state = "q6"
            else:
                state = "DEAD"

        elif state == "q6":
            if c in angka:
                state = "q6"
            else:
                state = "DEAD"

        else:                       
            state = "DEAD"

        print("  ", lama, "--", c, "-->", state)

    if state == "q6":
        print("  Hasil: VALID")
    else:
        print("  Hasil: TIDAK VALID")
    print()

while True:
    s = input("Masukkan angka (kosongkan lalu Enter untuk keluar): ")
    if s == "":
        break
    periksa(s)