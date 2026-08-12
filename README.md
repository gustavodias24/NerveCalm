# NerveCalm Affiliate Landing Page

A responsive English-language NerveCalm affiliate landing page built with Python and Flask.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python index.py
```

Open `http://127.0.0.1:5000`.

All purchase buttons use the configured affiliate destination:

`https://getnervecalm.com/dtc/?aff_id=263006`

## Production

```bash
gunicorn index:app
```

Legal and affiliate disclosures are included at `/privacy`, `/terms`, and `/disclaimer`.

## Image assets

The project includes 15 AI-generated production images plus the supplied official product image, all optimized to WebP. The site includes a visible disclosure explaining that illustrative product, ingredient, lifestyle, and profile imagery may differ from the current retail packaging.
