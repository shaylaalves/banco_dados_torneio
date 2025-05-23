import pyodbc

conn = pyodbc.connect(
    'DSN=TorneioPokemon;UID=postgres;PWD=123456'
)

# ========================
# CRUD Treinadores
# ========================

def inserir_treinador(nome, cidade, idade, ranking):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO torneio_bairro.treinador (nome, cidade, idade, ranking) VALUES (?, ?, ?, ?)",
        (nome, cidade, idade, ranking)
    )
    conn.commit()
    cursor.close()

def listar_treinadores():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM torneio_bairro.treinador")
    dados = cursor.fetchall()
    cursor.close()
    return dados

# ========================
# CRUD Pokémon
# ========================

def inserir_pokemon(nome, tipo, nivel, treinador_id):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO torneio_bairro.pokemon (nome, tipo, nivel, treinador_id) VALUES (?, ?, ?, ?)",
        (nome, tipo, nivel, treinador_id)
    )
    conn.commit()
    cursor.close()

def listar_pokemons():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM torneio_bairro.pokemon")
    dados = cursor.fetchall()
    cursor.close()
    return dados

# ========================
# CRUD Itens
# ========================

def inserir_item(nome, efeito, quantidade, treinador_id):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO torneio_bairro.item (nome, efeito, quantidade, treinador_id) VALUES (?, ?, ?, ?)",
        (nome, efeito, quantidade, treinador_id)
    )
    conn.commit()
    cursor.close()

def listar_itens():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM torneio_bairro.item")
    dados = cursor.fetchall()
    cursor.close()
    return dados

# ========================
# CRUD Batalhas
# ========================

def inserir_batalha(data, local_id, vencedor_id, perdedor_id):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO torneio_bairro.batalha (data, local_id, vencedor_id, perdedor_id) VALUES (?, ?, ?, ?)",
        (data, local_id, vencedor_id, perdedor_id)
    )
    conn.commit()
    cursor.close()

def listar_batalhas():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM torneio_bairro.batalha")
    dados = cursor.fetchall()
    cursor.close()
    return dados

# ========================
# CRUD Locais
# ========================

def inserir_local(nome, tipo_ambiente, cidade):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO torneio_bairro.local (nome, tipo_ambiente, cidade) VALUES (?, ?, ?)",
        (nome, tipo_ambiente, cidade)
    )
    conn.commit()
    cursor.close()

def listar_locais():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM torneio_bairro.local")
    dados = cursor.fetchall()
    cursor.close()
    return dados

# ========================
# CRUD Times
# ========================

def inserir_time(nome):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO torneio_bairro.time (nome) VALUES (?)",
        (nome,)
    )
    conn.commit()
    cursor.close()

def listar_times():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM torneio_bairro.time")
    dados = cursor.fetchall()
    cursor.close()
    return dados
