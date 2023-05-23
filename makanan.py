import os
from prettytable import PrettyTable


# ///////////// DIBAWAH BAGIAN EDIT MENU MAKANAN, MINUMAN,  MENU TAMBAHAN
makanan = [
    {
        'kode':'01', 
        'nama':'Steak Ayam', 
        'harga':'Rp. 25.000'},
    {
        'kode':'02', 
        'nama':'Steak Sirlon Sapi', 
        'harga':'Rp. 45.000'
    }, {
        'kode':'03', 
        'nama':'Steak Kambing', 
        'harga':'Rp. 45.000'
    }, {
        'kode':'04', 
        'nama':'Nasi Gurih', 
        'harga':'Rp. 15.000'
    }, {
        'kode':'05', 
        'nama':'Nasi Goreng', 
        'harga':'Rp. 25.000'
    }, {
        'kode':'06', 
        'nama':'Mie Ayam', 
        'harga':'Rp. 15.000'
    }, {
        'kode':'07', 
        'nama':'Dimsum Ayam', 
        'harga':'Rp. 15.000'
    }, {
        'kode':'08', 
        'nama':'Dimsum Sapi', 
        'harga':'Rp. 20.000'
    }, {
        'kode':'09', 
        'nama':'Dimsum Jamur', 
        'harga':'Rp. 15.000'
    }, {
        'kode':'10', 
        'nama':'Keripik Ubi', 
        'harga':'Rp. 5.000'
    }
]

minuman = [
    {
        'kode':'01', 
        'nama':'Jus Apel', 
        'harga':'Rp. 15.000'
    }, {
        'kode':'02', 
        'nama':'Jus Jeruk', 
        'harga':'Rp. 15.000'
    }, {
        'kode':'03', 
        'nama':'Jus Alpukat', 
        'harga':'Rp. 15.000'
    }, {
        'kode':'04', 
        'nama':'Jus Mangga', 
        'harga':'15.000'
    }, {
        'kode':'05', 
        'nama':'Cappucino', 
        'harga':'Rp. 15.000'
    }, {
        'kode':'06', 
        'nama':'Air Mineral', 
        'harga':'Rp. 10.000'
    }, {
        'kode':'07', 
        'nama':'Kopi Tubruk', 
        'harga':'Rp. 10.000'
    }
]

menu_tambahan = [
    {
        'kode':'A', 
        'nama':'Nasi Uduk', 
        'harga':'Rp. 5.000',
    }, {
        'kode':'B', 
        'nama':'Nasi Putih', 
        'harga':'Rp. 5.000'
    }, {
        'kode':'C', 
        'nama':'Kuah Soto', 
        'harga':'Rp. 5.000'
    }
]

# ///////////// DIATAS BAGIAN EDIT MENU MAKANAN, MINUMAN,  MENU TAMBAHAN

def neworder():
    print('\nMakanan:')
    # Membuat tabel untuk menampilkan list makanan
    table_makanan = PrettyTable(['Kode Makanan', 'Menu Makanan', 'Tarif'])
    for x in makanan:
        table_makanan.add_row([x['kode'], x['nama'], x['harga']])
    
    # Menampilkan Table Makanan
    print(table_makanan)

    print('\nMinuman:')
    # Membuat Tabel untuk menampilkan list minumab
    table_minuman = PrettyTable(['Kode Minuman', 'Minuman', 'Tarif'])
    for x in minuman:
        table_minuman.add_row([x['kode'], x['nama'], x['harga']])
    
    # Menampilkan Table Minuman
    print(table_minuman)

    print('\nMenu Tambahan Yang Dapat Ditambahkan:')
    # Membuat tabel untuk menampilkan list menu tambahan
    table_menu_tambahan = PrettyTable(['Kode Menu Tambahan', 'Menu Tambahan', 'Tarif'])
    for x in menu_tambahan:
        table_menu_tambahan.add_row([x['kode'], x['nama'], x['harga']])

    # Menampilkan Menu Tambahan
    print(table_menu_tambahan)

    # Input Pelanggan
    makan = input('\nKode Makanan: ')
    minum = input('Kode Minuman: ')
    tambahan = input('Kode Menu Tambahan ( Ketik - Jika Tidak Ada ): ')
    tanya = input('\nApakah Selesai (y/n): ')
    if tanya.lower() == 'y':
        pass
    else:
        main()

def main():
    os.system('clear')
    # Banner
    print('''
 .---.   .--.  .----..----.     .--.  .----.  .---. .----. 
/  ___} / {} \ | {_  | {_      / {} \ | {}  }/  ___}| {}  \\
\\     }/  /\\  \\| |   | {__    /  /\\  \\| {}  }\\     }|     /
 `---' `-'  `-'`-'   `----'   `-'  `-'`----'  `---' `----' 
    ''')

    #Menu Utama
    print('01. Tambah Pembayaran')

    opsi = input('\nPilih Opsi: ')
    nama = input('Nama Pelanggan: ')
    if '1' in opsi:
        neworder()

if __name__ == '__main__':
    main()
