import os
import threading
from flask import Flask
import worker

app = Flask(__name__)

@app.route('/')
def home():
    return "Worker is running!"

def run_worker():
    worker.main()

if __name__ == "__main__":
    t = threading.Thread(target=run_worker)
    t.daemon = True
    t.start()
    
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
