from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Devops Lab Impacta Sebah!!"

if __name__ == '__main__':
    app.run()