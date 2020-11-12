import os
from dotenv import load_dotenv
from flask import Flask, render_template, request

from api import get_user_data

load_dotenv()

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main_route():
    if request.method == 'POST':
        name = str(request.form['name'])
        message = 'Нет информации'
        avatar_src = ''
        if name:
            user_data = get_user_data(name)
            if user_data:
                name = user_data['name']
                message = user_data['status']
                avatar_src = user_data['avatar']
        return render_template('index.html', name=name, message=message, avatar_src=avatar_src)
    else:
        return render_template('index.html', message='Введите имя пользователя')
