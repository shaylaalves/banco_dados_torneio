import pyodbc

conn = pyodbc.connect(
    "DRIVER={PostgreSQL Unicode};"
    "SERVER=localhost;"
    "PORT=5432;"
    "DATABASE=torneio_pokemon;"
    "UID=postgres;"
    "PWD=123456"
)

# ✅ Função para inserir um treinador
def inserir_treinador(nome, cidade, idade, ranking):
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO torneio_bairro.treinador (nome, cidade, idade, ranking)
        VALUES (?, ?, ?, ?)
        """,
        (nome, cidade, idade, ranking)
    )
    conn.commit()
    cursor.close()


# ✅ Função para listar todos os treinadores
def listar_treinadores():
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT id, nome, cidade, idade, ranking
        FROM torneio_bairro.treinador
        """
    )
    treinadores = cursor.fetchall()
    cursor.close()
    return treinadores


# ✅ Função para atualizar um treinador
def atualizar_treinador(id, nome, cidade, idade, ranking):
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE torneio_bairro.treinador
        SET nome = ?, cidade = ?, idade = ?, ranking = ?
        WHERE id = ?
        """,
        (nome, cidade, idade, ranking, id)
    )
    conn.commit()
    cursor.close()


# ✅ Função para deletar um treinador
def deletar_treinador(id):
    cursor = conn.cursor()
    cursor.execute(
        """
        DELETE FROM torneio_bairro.treinador
        WHERE id = ?
        """,
        (id,)
    )
    conn.commit()
    cursor.close()



