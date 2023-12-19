export const APP_URL = "http://127.0.0.1";
export const AUTH = "6543";
export const CART = "6544";
export const KATEGORI = "6545";
export const PRODUK = "6546";
export const TRANSAKSI = "6547";

export function getURL(port) {
  return APP_URL + ":" + port;
}

export function handleResponseMessage(response) {
    if (response.message == "Unauthorized") {
        throw new Error(response.message);
    }
    if (response.message == "Bad Request") {
        throw new Error(response.message);
    }
    if (response.message == "Not Found") {
        throw new Error(response.message);
    }
    if (response.message == "Internal Server Error") {
        throw new Error(response.message);
    }
}
