print("~~~~ Table Matetamtika Nich ~~~~")
print("Pilihan Model Matematika")
print("1. Perkalian")
print("2. Pembagian")


k=int(input("Masukan model matematika yang diinginkan 1/2:"))
t=int(input("Menampilkan table matematika dari angka:"))
if k==1:
    
    dikalikan=[0,1,2,3,4,5,6,7,8,9,10]
    for i in range(1,11):
        rumus=i*t
        print(t,  "x", dikalikan[i], "=", rumus)
elif k==2:
    dibagikan=[50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65]
    for i in range(50,66):
        rumusp=i/t
        print(i,  ":",t, "=", rumusp)
elif k > 2:
    print("Pilihan tidak tersedia, jangan ngasal!")