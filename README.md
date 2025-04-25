# Sonic Cleaner

FastAPI で動く音声クリーニング API（雛形）

## セットアップ

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
