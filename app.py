import os
import random
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def randomizer():
    number = random.randint(1, 6)
    env_var = os.environ.get('MY_TEST', 'fallback')
    current_time = datetime.now().strftime('%H:%M:%S')
    
    return f"""
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Рандомайзер</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }}
            .container {{
                text-align: center;
                background: rgba(255, 255, 255, 0.15);
                padding: 40px 60px;
                border-radius: 20px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
                backdrop-filter: blur(10px);
            }}
            h1 {{
                margin-bottom: 10px;
                font-size: 2rem;
            }}
            .number {{
                font-size: 6rem;
                font-weight: bold;
                margin: 20px 0;
                text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.3);
            }}
            .info {{
                font-size: 0.9rem;
                opacity: 0.8;
                margin-top: 20px;
            }}
            a {{
                color: #ffd700;
                text-decoration: none;
                font-weight: bold;
            }}
            a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎲 Рандомайзер</h1>
            <p>Ваше випадкове число від 1 до 6:</p>
            <div class="number">{number}</div>
            <p><a href="/">Оновити</a></p>
            <div class="info">
                <p>Час генерації: {current_time}</p>
                <p>Env var: {env_var}</p>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
