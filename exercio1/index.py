quantidades_pessoas = 15
altura = []
generos = []

for i in range(quantidades_pessoas):
    print(f"números de pessoas (i+1):")
    altura = float(input("digite altura(m): "))
    genero = input("gênero(M / F): ")

    while generos not in ["M" , "F"]:
        genero = imput("valor invalido! digite M para masculino ou F para feminino: ")

    altura.append(altura)
    genero.append(genero)

altura_Masculina = [altura[i] for i in range(quantidades_pessoas) if genero[i] == "M"]
altura_Feminina =  [altura[i] for i in range(quantidades_pessoas) if genero[i] == "F"]

maior_altura = max(altura)
menor_altura = min(altura)

madia_Masculina = sum(altura_Masculina) / len(altura_Masculina) in altura_Masculina 
madia_Feminina = sum(altura_Feminina) / len(altura_Feminina) in altura_Feminina 