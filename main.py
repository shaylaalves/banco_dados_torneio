from torneio.database import inserir_treinador, listar_treinadores

# 🔥 Inserindo dados
inserir_treinador("Ash", "Pallet", 10, 1)
inserir_treinador("Misty", "Cerulean", 12, 4)

# 🔍 Listando treinadores
treinadores = listar_treinadores()

for t in treinadores:
    print(t)
