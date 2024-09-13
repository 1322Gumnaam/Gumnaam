from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)
@app.route('/')
def index():
    return "✩░▒▓▆▅▃▂▁𝐂𝐇𝐀𝐋 𝐑𝐇𝐀 𝐇𝐔▁▂▃▅▆▓▒░✩"

def run():
    app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()    