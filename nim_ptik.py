def nama(state):
    if state == -1:
        return "DEAD"
    return "q" + str(state)

def periksa(teks, tampil=True):
    state = 0                         
    if tampil:
        print("Input:", teks)

    for c in teks:                    
        lama = state

        if state == 0:                 
            if c == "K":
                state = 1
            else:
                state = -1

        elif state == 1:             
            if c == "3":
                state = 2
            else:
                state = -1

        elif state == 2:              
            if c == "5":
                state = 3
            else:
                state = -1

        elif state == 3:               
            if c == "1":
                state = 4
            elif c == "2":
                state = 5
            else:
                state = -1

        elif state == 4:              
            if c in "56789":
                state = 6
            else:
                state = -1

        elif state == 5:               
            if c in "0123456":
                state = 6
            else:
                state = -1

        elif state == 6:              
            if c == "0":
                state = 7
            elif c in "123456789":
                state = 8
            else:
                state = -1

        elif state == 7:             
            if c == "0":
                state = 9
            elif c in "123456789":
                state = 10
            else:
                state = -1

        elif state == 8:              
            if c in "0123456789":
                state = 10
            else:
                state = -1

        elif state == 9:               
            if c in "123456789":
                state = 11
            else:
                state = -1

        elif state == 10:            
            if c in "0123456789":
                state = 11
            else:
                state = -1

        else:                        
            state = -1               

        if tampil:
            print("  ", nama(lama), "--", c, "-->", nama(state))

        if state == -1:                
            break

    diterima = (state == 11)          
    if tampil:
        if diterima:
            print("  Hasil: VALID")
        else:
            print("  Hasil: TIDAK VALID")
        print()
    return diterima

while True:
        s = input("Masukkan NIM (kosongkan lalu Enter untuk keluar): ")
        if s == "":
            break
        periksa(s)