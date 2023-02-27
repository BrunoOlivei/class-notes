from flask import Flask, render_template

class Jogo:
    def __init__(self, nome: str, categoria: str, console: str):
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)

@app.route('/inicio')
def ola():
    jogo_1 = Jogo("Tetris", "Puzzle", "Atari")
    jogo_2 = Jogo("God of War", "Rack n Slash", "PS2")
    jogo_3 = Jogo("Mortal Kombat", "Luta", "PS2")
    lista_jogos = [jogo_1, jogo_2, jogo_3]
    return render_template("lista.html", titulo="Jogos", jogos=lista_jogos)

@app.route("/novo")
def novo():
    return render_template("novo.html", titulo="Novo Jogo")

app.run()