print("Susu     = Rp20.000")
print("Permen   = Rp500")
print("roti     = Rp15.000")
print("indomie  = Rp3.000")
print("vitamin  = Rp50.000")

Duid = int(input('Masukan Jumlah uag:'))
iStart = input("Ketik 'START' untuk memulai: ")

susu = 20000
permen = 500
roti = 15000
indomie = 3000
vitamin = 50000

if iStart.upper() == 'START':
    while True:
        beli = input("Apa barang yang akan beli?")
        if beli.upper() =='SUSU':
            if Duid >= susu:
                Duid -= susu
                print('sisa',Duid)
            else:
                print('tdk cukup')
        elif beli.upper() =='ROTI':
            if Duid >= roti:
                Duid -= roti
                print('sisa',Duid)
            else:
                print('tdk cukup')
        elif beli.upper() =='PERMEN':
            if Duid >= permen:
                Duid -= permen
                print('sisa',Duid)
            else:
                print('tdk cukup')
        elif beli.upper() =='VITAMIN':
            if Duid >= vitamin:
                Duid -= vitamin
                print('sisa',Duid)
            else:
                print('tdk cukup')
        elif beli.upper() =='INDOMIE':
            if Duid >= indomie:
                Duid -= indomie
                print('sisa',Duid)
            else:
                print('tdk cukup')
        elif beli.lower() == 'sudah':
            break
        else:
            print('barang tdk ada')