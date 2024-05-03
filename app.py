from flask import Flask, render_template
from dotenv import load_dotenv
import os

# Загрузка переменных окружения из файла .env
load_dotenv()

app = Flask(__name__)

# Проверка наличия переменной окружения DEBUG
if os.environ.get('DEBUG'):
    app.debug = os.environ.get('DEBUG').lower() == 'true'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()