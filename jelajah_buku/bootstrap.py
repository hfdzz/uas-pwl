import threading

def importAuth():
    import auth.main

def importCart():
    import cart.main

def importKategori():
    import kategori.main

def importProduk():
    import produk.main

def importTransaksi():
    import transaksi.main

if __name__ == '__main__':
    services = [importAuth, importCart, importKategori, importProduk, importTransaksi]
    threads = [
        threading.Thread(target=importAuth),
        threading.Thread(target=importCart),
        threading.Thread(target=importKategori),
        threading.Thread(target=importProduk),
        threading.Thread(target=importTransaksi)
    ]

    print("Starting services...")
    # WHY SO SLOW?
    for thread in threads:
        thread.start()
    
    while True:
        pass
