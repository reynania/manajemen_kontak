"Program Manajemen Kontak"

kontak1 = {'nama' : "Reyna", 'HP' : '082310385614', 'email' : 'reynabethaniaberutu@gmail.com'}
kontak2 = {'nama' : "gtw", 'HP' : '+62', 'email' : 'gatauu@gmail.com'}
kontak = [kontak1, kontak2]

while True:
    print("\nMenu Kontak")
    print("1. Lihat Semua Kontak")
    print("2. Tambah Kontak Baru")
    print("3. Hapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input("\nMasukkan pilihan menu kontak (1,2,3,4): ")

    if pilihan == '1':
        # lihat semua kontak
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("Kontak masih kosong!")

    elif pilihan == '2':
        # tambah kontak
        nama = input("Masukkan nama kontak yang baru: ")
        HP = input("Masukkan nomor hp kontak yang baru: ")
        email = input("Masukkan email kontak yang baru: ")
        kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
        kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan!")

    elif pilihan == '3':
        # hapus kontak
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("Kontak masih kosong!")
            continue

        i_hapus = int(input("Masukkan nomor kontak yang akan dihapus: "))
        del kontak[i_hapus-1]
        print("Kontak yang dimaksud sudah dihapus.")

    elif pilihan == '4':
        # keluar dari kontak
        break
    else:
        print("Anda salah memasukkan pilihan.")

