heksa = "0123456789abcdefABCDEF"
transisi = {
    "q1": "q2",
    "q2": "q3",
    "q3": "q4",
    "q4": "q5",
    "q5": "q6",
    "q6": "q7"
}

def cek(kode):
    state = "q0"
    print("Input:", kode)

    for huruf in kode:
        awal = state

        if state == "q0":
            if huruf == "#":
                state = "q1"
            else:
                state = "DEAD"

        elif state in transisi:
            if huruf in heksa:
                state = transisi[state]
            else:
                state = "DEAD"

        else:
            state = "DEAD"

        print(" ", awal, "--", huruf, "-->", state)

    if state == "q7":
        print("Hasil: VALID")
    else:
        print("Hasil: TIDAK VALID")

    print()

while True:
    input_kode = input("Masukkan kode (Enter untuk keluar): ")

    if input_kode == "":
        break

    cek(input_kode)
