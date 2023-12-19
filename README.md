# Website Jelajah Buku

## Kelompok :
- Yusril Iskandar Harahap  119140223
- Yusuf Hafidz             120140234
- Joy Arta BR Sitinjak     120140101
- Ferawati Manurung        120140196
- Hafiz Amrullah           119140177

## Deskripsi
Website e-commerce yang dibuat ini ialah situs toko buku bernama: Jelajah Buku yang dibuat untuk mengakomodir kebutuhan pengguna akan buku bacaan. Disini pengguna dapat melakukan pembelian buku secara online dengan mudah dan praktis.

## Komponen Utama Arsitektur Website

- Pengembangan Front End dengan bahasa pemrograman React
    Halaman dari website terdiri atas Halaman Beranda, Halaman Login, Detail Produk, Transaksi, Cart.
- Pengembangan Back End dengan menggunakan Framework Pyramid Python
    Terdiri atas endpoint pengguna (auth), kategori, cart, produk, dan transaksi
    Untuk penjelasan lebih lanjut mengenai arsitektur aplikasi website dapat dilihat pada gambar dibawah ini.
    ![WhatsApp Image 2023-12-18 at 20 02 56_f0001067](https://github.com/hfdzz/uas-pwl/assets/100962621/ce8bf1a5-5a11-4a2f-a6cb-8e285be80d9a)

      - Microservice auth: bertanggung jawab untuk autentikasi pengguna.
      - Microservice cart: bertanggung jawab untuk mengelola keranjang belanja pengguna.
      - Microservice kategori: bertanggung jawab untuk mengelola kategori produk.
      - Microservice produk: bertanggung jawab untuk mengelola produk.
      - Microservice transaksi: bertanggung jawab untuk mengelola transaksi.

    ![WhatsApp Image 2023-12-18 at 20 02 57_b17c5e54](https://github.com/hfdzz/uas-pwl/assets/100962621/92f2dbe3-2e97-4b1a-b735-945518d2b34d)

  Setiap microservice di atas saling terhubung dan berinteraksi satu sama lain melalui protokol komunikasi. Ketika pengguna ingin membeli produk, microservice cart       akan mengirimkan request ke microservice produk untuk memeriksa ketersediaan produk. Jika produk tersedia, microservice cart akan mengirimkan request ke                microservice transaksi untuk memproses transaksi. Setelah transaksi berhasil diproses, microservice transaksi akan mengirimkan notifikasi ke microservice cart          untuk menghapus produk dari keranjang belanja pengguna.

  
