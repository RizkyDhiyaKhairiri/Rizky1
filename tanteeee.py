import sys
import time

def jalan_lirik():
    lirik = [
        ("temanku semua pada jahat tante", 0.1),
        ("aku lagi susah mereka ga ada", 0.1),
        ("coba kalau lagi jaya", 0.1),
        ("aku dipuja puja tante", 0.1),
        ("sudah terbiasa terjadi tante", 0.1),
        ("teman datang ketika lagi butuh saja", 0.1),
        ("coba kalau lagi susaaahhh", 0.1),
        ("mereka semua menghilaaaaaaanggggggg ", 0.1),
    ]

    delay = [1.1, 1.4, 1.6, 1.25, 1.1, 1.1, 1, 1.5]
    print("~TANTEEEEE~")
    time.sleep(3)
    for i, (baris_lagu, delay_char) in enumerate(lirik):
        for char in baris_lagu:
            print(char,end='')
            sys.stdout.flush()
            time.sleep(delay_char)
        time.sleep(delay[i])
        print('')

    print()
    print("Cihuyyy")

jalan_lirik()
