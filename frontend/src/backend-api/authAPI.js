import * as apiBase from './apiBase';

const AUTH_URL = apiBase.getURL(apiBase.AUTH);

export async function authWithEmailAndPassword(email, password) {
    const url = AUTH_URL + "/auth";
    const data = {
        email: email,
        password: password,
        token: ''
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

    // set token to local storage
    localStorage.setItem('token', result.token);

    return result;
}

export async function authWithToken(token) {
    const url = AUTH_URL + "/auth";
    const data = {
        email: '',
        password: '',
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

export async function registerUser(email, password, nama) {
    const url = AUTH_URL + "/register";
    const data = {
        email: email,
        password: password,
        nama: nama
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

    // set token to local storage
    localStorage.setItem('token', result.token);

    return result;
}

export async function logoutUser(token) {
    const url = AUTH_URL + "/logout";
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

    // remove token from local storage
    localStorage.removeItem('token');

    return result;
}

export async function getUserData(user_id) {
    const url = AUTH_URL + "/get_auth";
    const data = {
        id: user_id
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