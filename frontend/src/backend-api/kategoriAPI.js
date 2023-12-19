import * as apiBase from './apiBase';

const KATEGORI_URL = apiBase.getURL(apiBase.KATEGORI);

export async function getKategori(idKategori) {
    const url = KATEGORI_URL + "/kategori/" + idKategori;
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