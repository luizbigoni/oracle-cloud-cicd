from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Atividade Oracle Cloud</title>
        </head>
        <body>
            <h1>Hello World- CI/CD funcionando! Teste</h1>
            <h2>Servidor Web no Oracle Cloud</h2>
            <p>Aplicacao desenvolvida em Python com Flask.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
