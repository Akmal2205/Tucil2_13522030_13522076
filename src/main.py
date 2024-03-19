import mBruteForce
import mDivideAndConquer
import BonusNTitikDNC

def main() :
    print("Selamat Datang Pada Hasil Pengerjaan Tugas Kecil Pembuatan Kurva Bezier Kami")
    print("Silahkan pilih algoritma yang diinginkan")

    print("1. Algoritma Brute Force dengan 3 titik")
    print("2. Algoritma Divide and Conquer dengan 3 titik")
    print("3. Algoritma Divide and Conquer dengan n titik (n >= 3)")

    pilihan = input("Masukkan Pilihan Anda : ")

    while pilihan != '1' and pilihan != '2' and pilihan != '3' :
        print("Masukkan tidak valid! Silahkan ulangi kembali")
        pilihan = input("Masukkan Pilihan Anda : ")
    
    if pilihan == '1' :
        mBruteForce.mainbf()
    elif pilihan == '2' :
        mDivideAndConquer.maindnc()
    elif pilihan == '3' :
        BonusNTitikDNC.mainNTitikDNC()

    print("Terima Kasih :D")

main()