import os

from flask import Flask, render_template, send_from_directory


app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 31536000

AFFILIATE_URL = "https://getnervecalm.com/dtc/?aff_id=263006"


@app.context_processor
def inject_site_settings():
    return {
        "affiliate_url": AFFILIATE_URL,
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
