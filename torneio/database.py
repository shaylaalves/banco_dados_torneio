import pyodbc

# Conexão com o banco de dados
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

def deletar_treinador(id):
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM torneio_bairro.treinador WHERE id = ?",
        (id,)
    )
    conn.commit()
    cursor.close()

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

def deletar_pokemon(id):
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM torneio_bairro.pokemon WHERE id = ?",
        (id,)
    )
    conn.commit()
    cursor.close()

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

def deletar_item(id):
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM torneio_bairro.item WHERE id = ?",
        (id,)
    )
    conn.commit()
    cursor.close()

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

def deletar_batalha(id):
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM torneio_bairro.batalha WHERE id = ?",
        (id,)
    )
    conn.commit()
    cursor.close()

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

def deletar_local(id):
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM torneio_bairro.local WHERE id = ?",
        (id,)
    )
    conn.commit()
    cursor.close()

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

def deletar_time(id):
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM torneio_bairro.time WHERE id = ?",
        (id,)
    )
    conn.commit()
    cursor.close()