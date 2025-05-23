import pyodbc

conn = pyodbc.connect(
    'DSN=TorneioPokemon;UID=postgres;PWD=123456'
)

# =============================
# Consultas SQL Avançadas


# BETWEEN — Batalhas em um intervalo de datas
def batalhas_no_intervalo_de_datas(data_inicial, data_final):
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM torneio_bairro.batalha
        WHERE data BETWEEN %s AND %s
        """,
        (data_inicial, data_final)
    )
    dados = cursor.fetchall()
    cursor.close()
    return dados



# LIKE — Pokémons que começam com 'Pika'
def pokemons_que_comecam_com(prefixo):
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM torneio_bairro.pokemon
        WHERE nome LIKE ?
        """,
        (prefixo + '%',)
    )
    dados = cursor.fetchall()
    cursor.close()
    return dados


# IN — Treinadores específicos por ID
def treinadores_por_lista_ids(lista_ids):
    placeholders = ','.join('?' for _ in lista_ids)
    query = f"""
        SELECT * FROM torneio_bairro.treinador
        WHERE id IN ({placeholders})
    """
    cursor = conn.cursor()
    cursor.execute(query, lista_ids)
    dados = cursor.fetchall()
    cursor.close()
    return dados


# GROUP BY — Contagem de pokémons por tipo
def contar_pokemons_por_tipo():
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT tipo, COUNT(*) AS quantidade
        FROM torneio_bairro.pokemon
        GROUP BY tipo
        """
    )
    dados = cursor.fetchall()
    cursor.close()
    return dados


# EXISTS — Treinadores que possuem pokémons com nível maior que 30
def treinadores_com_pokemon_acima_de_nivel(nivel):
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM torneio_bairro.treinador t
        WHERE EXISTS (
            SELECT 1 FROM torneio_bairro.pokemon p
            WHERE p.treinador_id = t.id AND p.nivel > ?
        )
        """,
        (nivel,)
    )
    dados = cursor.fetchall()
    cursor.close()
    return dados


# UNION — Treinadores das cidades 'Pallet' e 'Cerulean'
def treinadores_de_duas_cidades():
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT nome, cidade FROM torneio_bairro.treinador
        WHERE cidade = 'Pallet'
        UNION
        SELECT nome, cidade FROM torneio_bairro.treinador
        WHERE cidade = 'Cerulean'
        """
    )
    dados = cursor.fetchall()
    cursor.close()
    return dados


# ANY — Treinadores que tenham ranking maior que qualquer um dos IDs dados
def treinadores_com_ranking_maior_que(ids):
    placeholders = ','.join('?' for _ in ids)
    query = f"""
        SELECT * FROM torneio_bairro.treinador
        WHERE ranking > ANY (SELECT ranking FROM torneio_bairro.treinador WHERE id IN ({placeholders}))
    """
    cursor = conn.cursor()
    cursor.execute(query, ids)
    dados = cursor.fetchall()
    cursor.close()
    return dados


#  ALL — Treinadores cujo ranking seja maior que TODOS os IDs dados
def treinadores_com_ranking_maior_que_todos(ids):
    placeholders = ','.join('?' for _ in ids)
    query = f"""
        SELECT * FROM torneio_bairro.treinador
        WHERE ranking > ALL (SELECT ranking FROM torneio_bairro.treinador WHERE id IN ({placeholders}))
    """
    cursor = conn.cursor()
    cursor.execute(query, ids)
    dados = cursor.fetchall()
    cursor.close()
    return dados


#  ORDER BY — Itens ordenados por quantidade (descendente)
def itens_ordenados_por_quantidade():
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM torneio_bairro.item
        ORDER BY quantidade DESC
        """
    )
    dados = cursor.fetchall()
    cursor.close()
    return dados


# Agregações — Quantidade total de itens por treinador
def soma_itens_por_treinador():
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT treinador_id, SUM(quantidade) AS total_itens
        FROM torneio_bairro.item
        GROUP BY treinador_id
        """
    )
    dados = cursor.fetchall()
    cursor.close()
    return dados
