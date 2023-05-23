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

# Membuat tabel akhir
result = PrettyTable(['Nama Pelanggan', 'Barang', 'Total Tarif'])



def neworder(nama):
    data_makanan = {}
    data_minuman = {}
    data_menu_tambahan = {}
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

    # Pengecekan data makanan
    for x in makanan:
        if x['kode'] == makan:
            data_makanan.update({'nama':x['nama'], 'harga':x['harga'].replace('Rp. ', '').split('.')[0]})
            break
    if len(data_makanan) == 0:
        data_makanan.update({'nama':'-', 'harga':'0'})

    # Pengecekan data kinuman
    for x in minuman:
        if x['kode'] == minum:
            data_minuman.update({'nama':x['nama'], 'harga':x['harga'].replace('Rp. ', '').split('.')[0]})
            break
    if len(data_minuman) == 0:
        data_minuman.update({'nama':'-', 'harga':'0'})

    # Pengecekan data menu tambahan
    for x in menu_tambahan:
        if x['kode'] == tambahan.upper():
            data_menu_tambahan.update({'nama':x['nama'], 'harga':x['harga'].replace('Rp. ', '').split('.')[0]})
            break
    if len(data_menu_tambahan) == 0:
        data_menu_tambahan.update({'nama':'-', 'harga':'0'})

    # Menghitung total harga
    ttl_harga = f"Rp. {int(data_makanan['harga']) + int(data_minuman['harga']) + int(data_menu_tambahan['harga'])}.000"

    # Menambahkan value tabel akhir
    result.add_row([nama, data_makanan['nama']+', '+data_minuman['nama']+', '+ data_menu_tambahan['nama'], ttl_harga])
    if tanya.lower() == 'n':
        print(result)
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
        neworder(nama)
    else:
        main()

if __name__ == '__main__':
    main()
