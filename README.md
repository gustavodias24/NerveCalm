# NerveCalm Affiliate Landing Page

A responsive English-language NerveCalm affiliate landing page built with Python and Flask.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

## WhatsApp configuration

The floating button opens WhatsApp's share/contact picker by default. To send visitors directly to a specific number, set `WHATSAPP_NUMBER` in international format with digits only:

```bash
export WHATSAPP_NUMBER=15551234567
```

All purchase buttons use the configured affiliate destination:

`https://getnervecalm.com/dtc/?aff_id=263006`

## Production

```bash
gunicorn app:app
```

Legal and affiliate disclosures are included at `/privacy`, `/terms`, and `/disclaimer`.

## Image assets

The 15 production images in `static/img/` were generated specifically for this project and optimized to WebP. The site includes a visible disclosure that product, ingredient, lifestyle, and profile imagery is AI-generated for illustration.
