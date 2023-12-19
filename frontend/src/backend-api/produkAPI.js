import * as apiBase from './apiBase';

const PRODUK_URL = apiBase.getURL(apiBase.PRODUK);

export async function addProduk(token, judul, penulis, deskripsi, harga, kategori, gambar){
    const url = PRODUK_URL + "/add";
    const data = {
        token: token,
        judul: judul,
        penulis: penulis,
        deskripsi: deskripsi,
        harga: harga,
        kategori: kategori,
        gambar: gambar
    };
    const response = await fetch(url, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        'Accept': '*/*'
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    apiBase.handleResponseMessage(result);
    return result;
}

export async function editProduk(token, id, judul, penulis, deskripsi, harga, kategori, gambar){
    const url = PRODUK_URL + "/edit";
    const data = {
        token: token,
        id: id,
        judul: judul,
        penulis: penulis,
        deskripsi: deskripsi,
        harga: harga,
        kategori: kategori,
        gambar: gambar
    };
    const response = await fetch(url, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        'Accept': '*/*'
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    apiBase.handleResponseMessage(result);
    return result;
}

export async function deleteProduk(token, id){
    const url = PRODUK_URL + "/delete";
    const data = {
        token: token,
        id: id
    };
    const response = await fetch(url, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        'Accept': '*/*'
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    apiBase.handleResponseMessage(result);
    return result;
}

export async function getProduk(id){
    const url = PRODUK_URL + "/get/" + id;
    const response = await fetch(url, {
        method: 'GET',
        headers: {
        'Content-Type': 'application/json',
        'Accept': '*/*'
        }
    });

    const result = await response.json();
    apiBase.handleResponseMessage(result);
    return result;
}

export async function getProdukByKategori(kategori){
    const url = PRODUK_URL + "/get/kategori/" + kategori;
    const response = await fetch(url, {
        method: 'GET',
        headers: {
        'Content-Type': 'application/json',
        'Accept': '*/*'
        }
    });

    const result = await response.json();
    apiBase.handleResponseMessage(result);
    return result;
}

export async function getAllProduk(page, limit){
    const url = PRODUK_URL + "/get/all/" + page + "/" + limit;
    const response = await fetch(url, {
        method: 'GET',
        headers: {
        'Content-Type': 'application/json',
        'Accept': '*/*'
        }
    });

    const result = await response.json();
    apiBase.handleResponseMessage(result);
    return result;
}