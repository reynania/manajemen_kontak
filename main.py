"Program Manajemen Kontak"
import kontak

def main():
    kontak_kantor = kontak.Kontak()
    kontak_keluarga = kontak.Kontak()

    while True:
        print("\nMenu Kontak")
        print("1. Lihat Semua Kontak")
        print("2. Tambah Kontak Baru")
        print("3. Hapus Kontak")
        print("4. Keluar dari Kontak")

        pilihan = input("\nMasukkan pilihan menu kontak (1,2,3,4): ")

        if pilihan == '1':
            kontak_keluarga.melihat_kontak()

        elif pilihan == '2':
            kontak_keluarga.menambah_kontak()

        elif pilihan == '3':
            kontak_keluarga.menghapus_kontak()

        elif pilihan == '4':
            # keluar dari kontak
            kontak_keluarga.keluar_kontak()
            break
        else:
            print("Anda salah memasukkan pilihan.")

if __name__ == "__main__":
    main()