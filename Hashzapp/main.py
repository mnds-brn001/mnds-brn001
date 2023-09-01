# site com os scripts: https://cdnjs.com/
# bibliotecas a instalar: 
    # Flask – pip install flask
    # Socketio – pip install python-socketio / pip install flask-socketio
    # Simple Websocket – pip install simple-websocket

from flask import Flask, render_template # Ferramentas para criar o site
from flask_socketio import SocketIO, send # Ferramentas para criar o chat

app=Flask(__name__,template_folder='template') # Cria o site
app.config["SECRET"] = "ajuiahfa78fh9f78shfs768fgs7f6" # Chave de Segurança
app.config["DEBUG"] = True # Código utillizando somente enquanto são feitos os testes.]
socketio = SocketIO(app, cors_allowed_origins="*") #cria a conexão entre diferentes máquinas que estão no mesmo site

@socketio.on("message") #Define que a função abaixo vai ser acionada quando este evento for ativado.
def gerenciar_mensagens(mensagem):
    print(f'Mensagem: {mensagem}')
    send(mensagem, broadcast=True) # Envia a mensagem para todos conectados no site, 'Ao vivo'.

@app.route("/") # Cria a página do site
def home():
    return render_template("index.html") # essa página vai carregar o template linkado aqui.

if __name__ =="__main__":
    socketio.run(app,host="localhost") # Definque que o app vai rodar no seu servido local.
 
