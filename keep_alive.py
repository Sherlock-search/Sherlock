import os
from flask import Flask
import threading

app = Flask('')

@app.route('/')
def home():
    return "Cyber Search Bot is active and running 24/7!"

def run():
    # Render veya diğer platformların PORT değişkenini alır, yoksa 8080 kullanır
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()
    