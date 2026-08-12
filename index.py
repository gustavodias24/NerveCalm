import os
from urllib.parse import quote_plus

from flask import Flask, render_template, send_from_directory


app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 31536000

AFFILIATE_URL = "https://getnervecalm.com/dtc/?aff_id=263006"


def build_whatsapp_url() -> str:
    """Build a direct WhatsApp link when a number is configured.

    Without a number, WhatsApp opens its share/contact picker so the button
    remains useful and no fake contact is published.
    """

    number = "".join(filter(str.isdigit, os.getenv("WHATSAPP_NUMBER", "")))
    message = quote_plus(
        os.getenv(
            "WHATSAPP_MESSAGE",
            "Hi! I would like to learn more about NerveCalm.",
        )
    )
    if number:
        return f"https://wa.me/{number}?text={message}"
    return f"https://wa.me/?text={message}"


@app.context_processor
def inject_site_settings():
    return {
        "affiliate_url": AFFILIATE_URL,
        "whatsapp_url": build_whatsapp_url(),
    }


@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
    return response


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/privacy")
def privacy():
    return render_template("legal.html", page="privacy")


@app.get("/terms")
def terms():
    return render_template("legal.html", page="terms")


@app.get("/disclaimer")
def disclaimer():
    return render_template("legal.html", page="disclaimer")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/robots.txt")
def robots():
    return send_from_directory(app.static_folder, "robots.txt", mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=False)
