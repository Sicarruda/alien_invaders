import json


#   Salvar em arquivo JSON 
with open("estado_do_jogo.json", "r") as f:
    
    lala = json.load(f)
    print(lala)
print("Estado salvo!")

print(f"Voce está na fase {lala['fase']}")