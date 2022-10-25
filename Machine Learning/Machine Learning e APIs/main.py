from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_basicauth import BasicAuth
from sklearn.linear_model import LinearRegression
import pickle

colunas = ['tamanho', 'ano', 'garagem']

modelo = pickle.load(open('modelo.sav', 'rb'))

''' 
Para criar o app, cria-se uma variável com a instância do pacote importado, dentro entre aspas recebe-se o nome do
 app “(name)”. Assim vai ficar mais fácil para o Flask saber onde que essa aplicação está rodando, o que foi que 
 “startou” essa aplicação e vai ajudar ele a encontrar os recursos que ele precisa para a execução da aplicação.
'''
app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = "julio"
app.config['BASIC_AUTH_PASSWORD'] = "alura"

basic_auth = BasicAuth(app)

# Definindo a rota, a rota base ou seja a home é definida com barra entre aspas '/'
@app.route('/')
# Função que vai ser executada quando a api é chamada
def home():
    return "Minha primeira API."


'''
Definindo pontos de acesso a aplicação, através da URL, dessa forma a frase que será analisada pela aplicação deve 
 ser passada através da URL
'''


@app.route('/sentimento/<frase>')
@basic_auth.required
def sentimento(frase):
    tb = TextBlob(frase)
    tb_en = tb.translate(to='en')
    polaridade = tb_en.sentiment.polarity
    return f"Polaridade: {polaridade}"


@app.route('/cotacao/', methods=['POST'])
@basic_auth.required
def cotacao():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas]
    preco = modelo.predict([dados_input])
    return jsonify(preco=preco[0])

'''
O método run, permite que sempre que o nosso arquivo python for executado, ele rode o app criado com flask
 O argumento debug com valor True permite que se alterarmos qualquer parte do script e salvarmos o Flask vai identificar
 automaticamente e restartar a execução no terminal.
'''
app.run(debug=True)
