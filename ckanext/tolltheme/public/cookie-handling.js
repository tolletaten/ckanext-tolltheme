const COOKIES_ACCEPTED_KEY = "cookies-accepted";

function setCookiesAccepted() {
    // Expires in ten years from current time.
    const expires = new Date(Date.now() + 10 * 365 * 24 * 3600000);
    document.cookie = `${COOKIES_ACCEPTED_KEY}=true;expires=${expires.toUTCString()};path=/`;
    showCookiesMessage(false);
}

function getCookiesAccepted() {
    return document.cookie.split(";").reduce((accumulator, entry) => {
        const [key, value] = entry.split("=");
        if (key.trim() === COOKIES_ACCEPTED_KEY) {
            return value.trim();
        }
        return accumulator;
    }, null);
}

function showCookiesMessage(show) {
    document.getElementById("cookies-message-container").style.display = show ? "block" : "none";
}

if (getCookiesAccepted() !== "true") {
    showCookiesMessage(true);
}
