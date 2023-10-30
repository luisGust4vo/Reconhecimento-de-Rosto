from flask import Flask, request, jsonify #instalar para rotas
import os

app = Flask(__name__)
@app.route('/api/excluir_video', methods=['POST'])
def excluir_video():
    data = request.get_json()
    if 'comando' in data and data['comando'] == 'excluir' and 'pasta' in data and 'nome_do_video' in data:
        pasta = data['pasta'] 
        nome_do_video = data['nome_do_video']
        caminho_do_video = os.path.join(pasta, nome_do_video)
        if os.path.exists(caminho_do_video):
            os.remove(caminho_do_video)
            return jsonify({'mensagem': f'O vídeo {nome_do_video} foi excluído com sucesso.'})
        else:
            return jsonify({'mensagem': f'O vídeo {nome_do_video} não foi encontrado na pasta.'})
    else:
        return jsonify({'mensagem': 'Solicitação inválida. Certifique-se de incluir o comando "excluir" e os detalhes do vídeo.'}), 400

if __name__ == '__main__':
    app.run()
