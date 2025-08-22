
pessoas = [
    {"altura": 1.70, "genero": "M"},
    {"altura": 1.60, "genero": "F"},
    {"altura": 1.82, "genero": "M"},
    {"altura": 1.55, "genero": "F"},
    {"altura": 1.90, "genero": "M"},
    {"altura": 1.45, "genero": "F"},
    {"altura": 1.78, "genero": "M"},
    {"altura": 1.65, "genero": "F"},
    {"altura": 1.88, "genero": "M"},
    {"altura": 1.58, "genero": "F"},
    {"altura": 2.00, "genero": "M"},
    {"altura": 1.72, "genero": "F"},
    {"altura": 1.80, "genero": "M"},
    {"altura": 1.68, "genero": "F"},
    {"altura": 1.76, "genero": "M"}
]

alturas = [p["altura"] for p in pessoas]
maior_altura = max(alturas)
menor_altura = min(alturas)

alturas_masculinas = [p["altura"] for p in pessoas if p["genero"] == "M"]
numero_feminino = sum(1 for p in pessoas if p["genero"] == "F")

media_masculina = (
    sum(alturas_masculinas) / len(alturas_masculinas)
    if alturas_masculinas else 0
)

print("\n==== RESULTADOS ====")
print(f"Maior altura do grupo: {maior_altura:.2f} m")
print(f"Menor altura do grupo: {menor_altura:.2f} m")
print(f"Média de altura dos homens: {media_masculina:.2f} m")
print(f"Número de mulheres: {numero_feminino}")

