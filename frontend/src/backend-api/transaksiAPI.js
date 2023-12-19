import * as apiBase from './apiBase';

const TRANSAKSI_URL = apiBase.getURL(apiBase.TRANSAKSI);

export async function getTransaksi(token){
    const url = TRANSAKSI_URL + "/get";
    const data = {
        token: token
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

export async function payTransaksi(token){
    const url = TRANSAKSI_URL + "/pay";
    const data = {
        token: token
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