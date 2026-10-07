# Lab 2 — Рандомайзер (Варіант 2)

Простий веб-застосунок на Flask, який показує випадкове число від 1 до 6.

## Локальний запуск

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Відкрийте http://127.0.0.1:5000

## Розгортання на Render.com

1. Створіть репозиторій на GitHub і залийте ці файли.
2. Зайдіть на [render.com](https://render.com) → New → Web Service.
3. Підключіть GitHub-репозиторій.
4. Налаштування:
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Додайте Environment Variable (опційно): `MY_TEST` = будь-яке значення.
6. Deploy.

Після деплою отримаєте публічне посилання типу `https://your-app.onrender.com`
