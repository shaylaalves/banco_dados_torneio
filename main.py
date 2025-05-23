from torneio.consultas import batalhas_no_intervalo_de_datas
from torneio.database import (
    inserir_treinador, listar_treinadores,
    inserir_pokemon, listar_pokemons,
    inserir_item, listar_itens,
    inserir_batalha, listar_batalhas,
    inserir_local, listar_locais,
    inserir_time, listar_times
)

# Inserindo dados de exemplo

# Treinadores
inserir_treinador('Ash', 'Pallet Town', 10, 1)
inserir_treinador('Misty', 'Cerulean', 12, 2)

# Locais
inserir_local('Ginásio de Pedra', 'Rochoso', 'Pewter')
inserir_local('Centro Pokémon', 'Cidade', 'Pallet Town')

# Pokémon
inserir_pokemon('Pikachu', 'Elétrico', 35, 1)  # treinador_id = 1
inserir_pokemon('Staryu', 'Água', 30, 2)       # treinador_id = 2

# Itens
inserir_item('Poção', 'Cura 20HP', 5, 1)
inserir_item('Reviver', 'Revive um Pokémon', 2, 2)

# Batalhas (observe que local_id = 1 -> Ginásio de Pedra)
inserir_batalha('2024-05-20', 1, 1, 2)


# Times
inserir_time('Time Rocket')

#  Listando dados
print("\n------ Treinadores ------")
for t in listar_treinadores():
    print('Treinador:', t)

print("\n------ Pokémons ------")
for p in listar_pokemons():
    print('Pokémon:', p)

print("\n------ Itens ------")
for i in listar_itens():
    print('Item:', i)

print("\n------ Batalhas ------")
for b in listar_batalhas():
    print('Batalha:', b)

print("\n------ Locais ------")
for l in listar_locais():
    print('Local:', l)

print("\n------ Times ------")
for tm in listar_times():
    print('Time:', tm)

resultado = batalhas_no_intervalo_de_datas('2024-01-01', '2024-12-31')
for linha in resultado:
    print(linha)
