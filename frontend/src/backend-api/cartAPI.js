import * as apiBase from './apiBase';

const CART_URL = apiBase.getURL(apiBase.CART);

export async function addToCart(token, idProduk) {
    const url = CART_URL + "/add";
    const data = {
        token: token,
        id: idProduk
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


export async function removeFromCart(token, idProduk) {
    const url = CART_URL + "/remove";
    const data = {
        token: token,
        id: idProduk
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

export async function getCart(token) {
    const url = CART_URL + "/get";
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