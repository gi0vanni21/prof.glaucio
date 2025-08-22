pessoas = []

for i in range(15):
    print(f"\nPessoa {i+1}:")
    altura = float(input("altura: "))
    genero = input("gênero (M/F): ").strip().upper()
    pessoas.append({"altura": altura, "genero": genero})


alturas = [p["altura"] for p in pessoas]
maior_altura = max(alturas)
menor_altura = min(alturas)


alturas_masculinas = [p["altura"] for p in pessoas if p["genero"] == "M"]
numero_feminino = sum(1 for p in pessoas if p["genero"] == "F")


media_masculina = (
    sum(alturas_masculinas) / len(alturas_masculinas)
    if alturas_masculinas else 0
)

#aqui está o resutado#
print("\n=== Resultados ===: ")
print(f"Maior altura do grupo: {maior_altura:.2f} m")
print(f"Menor altura do grupo: {menor_altura:.2f} m")
print(f"Média de altura dos homens: {media_masculina:.2f} m")
print(f"Número de mulheres: {numero_feminino}")
