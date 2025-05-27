from flask import Flask, render_template, request, redirect
from torneio.database import (
    inserir_treinador, listar_treinadores, deletar_treinador,
    inserir_pokemon, listar_pokemons, deletar_pokemon,
    inserir_item, listar_itens, deletar_item,
    inserir_batalha, listar_batalhas, deletar_batalha,
    inserir_local, listar_locais, deletar_local,
    inserir_time, listar_times, deletar_time
)
from torneio.consultas import batalhas_no_intervalo_de_datas

app = Flask(__name__)

# ================================
# Página inicial
# ================================
@app.route('/')
def index():
    return render_template('index.html')

# ================================
# CRUD TREINADORES
# ================================
@app.route('/treinadores')
def treinadores():
    dados = listar_treinadores()
    return render_template('treinadores.html', treinadores=dados)

@app.route('/adicionar_treinador', methods=['POST'])
def adicionar_treinador():
    nome = request.form['nome']
    cidade = request.form['cidade']
    idade = int(request.form['idade'])
    ranking = int(request.form['ranking'])
    inserir_treinador(nome, cidade, idade, ranking)
    return redirect('/treinadores')

@app.route('/excluir_treinador/<int:id>')
def excluir_treinador(id):
    deletar_treinador(id)
    return redirect('/treinadores')

# ================================
# CRUD POKÉMON
# ================================
@app.route('/pokemons')
def pokemons():
    dados = listar_pokemons()
    return render_template('pokemons.html', pokemons=dados)

@app.route('/adicionar_pokemon', methods=['POST'])
def adicionar_pokemon():
    nome = request.form['nome']
    tipo = request.form['tipo']
    nivel = int(request.form['nivel'])
    treinador_id = int(request.form['treinador_id'])
    inserir_pokemon(nome, tipo, nivel, treinador_id)
    return redirect('/pokemons')

@app.route('/excluir_pokemon/<int:id>')
def excluir_pokemon(id):
    deletar_pokemon(id)
    return redirect('/pokemons')

# ================================
# CRUD ITENS
# ================================
@app.route('/itens')
def itens():
    dados = listar_itens()
    return render_template('itens.html', itens=dados)

@app.route('/adicionar_item', methods=['POST'])
def adicionar_item():
    nome = request.form['nome']
    efeito = request.form['efeito']
    quantidade = int(request.form['quantidade'])
    treinador_id = int(request.form['treinador_id'])
    inserir_item(nome, efeito, quantidade, treinador_id)
    return redirect('/itens')

@app.route('/excluir_item/<int:id>')
def excluir_item(id):
    deletar_item(id)
    return redirect('/itens')

# ================================
# CRUD LOCAIS
# ================================
@app.route('/locais')
def locais():
    dados = listar_locais()
    return render_template('locais.html', locais=dados)

@app.route('/adicionar_local', methods=['POST'])
def adicionar_local():
    nome = request.form['nome']
    tipo_ambiente = request.form['tipo_ambiente']
    cidade = request.form['cidade']
    inserir_local(nome, tipo_ambiente, cidade)
    return redirect('/locais')

@app.route('/excluir_local/<int:id>')
def excluir_local(id):
    deletar_local(id)
    return redirect('/locais')

# ================================
# CRUD BATALHAS
# ================================
@app.route('/batalhas')
def batalhas():
    dados = listar_batalhas()
    return render_template('batalhas.html', batalhas=dados)

@app.route('/adicionar_batalha', methods=['POST'])
def adicionar_batalha():
    data = request.form['data']
    local = int(request.form['local'])
    vencedor_id = int(request.form['vencedor_id'])
    perdedor_id = int(request.form['perdedor_id'])
    inserir_batalha(data, local, vencedor_id, perdedor_id)
    return redirect('/batalhas')

@app.route('/excluir_batalha/<int:id>')
def excluir_batalha(id):
    deletar_batalha(id)
    return redirect('/batalhas')

# ================================
# CRUD TIMES
# ================================
@app.route('/times')
def times():
    dados = listar_times()
    return render_template('times.html', times=dados)

@app.route('/adicionar_time', methods=['POST'])
def adicionar_time():
    nome = request.form['nome']
    inserir_time(nome)
    return redirect('/times')

@app.route('/excluir_time/<int:id>')
def excluir_time(id):
    deletar_time(id)
    return redirect('/times')

# ================================
# CONSULTAS SQL AVANÇADAS
# ================================
@app.route('/consultas')
def consultas():
    return render_template('consultas.html', resultado=[])

@app.route('/consultar_batalhas_intervalo', methods=['POST'])
def consultar_batalhas_intervalo():
    data_inicial = request.form['data_inicial']
    data_final = request.form['data_final']
    resultado = batalhas_no_intervalo_de_datas(data_inicial, data_final)
    return render_template('consultas.html', resultado=resultado)

# ================================
# Executar a aplicação
# ================================
if __name__ == '__main__':
    app.run(debug=True)