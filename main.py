#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get("button_discord")
    return render_template('index.html', 
                           button_python=button_python,
                           button_discord=button_discord)

# request.form = {"email":"1@mail.com", "text":"1234567890"}
@app.route("/form", methods=['POST'])
def form_render():
    name = request.form["email"]
    text = request.form["text"]
    return render_template("form.html",
                           name=name,
                           text=text)


if __name__ == "__main__":
    app.run(debug=True)