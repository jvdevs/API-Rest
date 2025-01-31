from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios)

@app.route('/usuarios', methods=['POST'])
def adicionar_usuario():
    dados = request.get_json()
    
    if 'nome' in dados:
        usuarios.append(dados)
        return jsonify({"mensagem": "Usuário cadastrado com sucesso!"}), 201
    else:
        return jsonify({"erro": "Nome do usuário é obrigatório!"}), 400

@app.route('/usuarios/<int:indice>', methods=['GET'])
def obter_usuario(indice):
    if 0 <= indice < len(usuarios):
        return jsonify(usuarios[indice])
    return jsonify({"erro": "Usuário não encontrado."}), 404


@app.route('/usuarios/<int:indice>', methods=['DELETE'])
def deletar_usuario(indice):
    if 0 <= indice < len(usuarios):
        usuario_removido = usuarios.pop(indice)
        return jsonify({"mensagem": "Usuário removido com sucesso!", "usuario": usuario_removido})
    return jsonify({"erro": "Usuário não encontrado."}), 404

if __name__ == '__main__':
    app.run(debug=True)
