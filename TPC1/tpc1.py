allData = [] #lista com todos os dados
total = 0 #número total de pessoas

sexos = {"M": 0, "F": 0} #quantidade de pessoas do sexo masculino e feminino com doença

escaloesEtar = dict() #chave é a idade x e valor o número de pessoas com idade x
niveisColest = dict()


#lê o ficheiro e vai guardando a info numa lista
def readFile():  
    global total  
    with open("myheart.csv", "r") as file:
            for line in file.readlines()[1:]: #ignora a linha de cabeçalho
                total += 1
                dataPerson = line[:-1].split(',') # [:-1] ignora o \n
                allData.append(dataPerson)  

#calcula a distribuição da doença por sexo
def calcSexos():
    for data in allData:
        if data[1] == "M" or data[1] == "F":
            if int(data[5]) == 1: #tem doença
                sexos[data[1]] += 1

#retorna o mínimo e máximo de idades
def minMaxIdade():
    min = 30 #definido no enunciado
    max = 0
    for data in allData:
        if int(data[0]) > max:
            max = int(data[0])
    return (min,max)
            
#calcula a distribuição por escalões etários
def escaloesEtarios():
    min,max = minMaxIdade()
    
    #definir o intervalo (dicionário começa na idade mínima até à máxima)
    while min <= max:
        escaloesEtar[min] = 0
        min += 5 
    
    #quantas pessoas com a doença existem em cada escalão etário
    for data in allData:
        for key in escaloesEtar.keys():
            if key <= int(data[0]) <= key + 4:
                if int(data[5]) == 1:
                    escaloesEtar[key] += 1
                      
#retorna o mínimo e máximo de nível de colesterol
def minMaxColesterol():
    min = 900
    max = 0
    for data in allData:
        if int(data[3]) != 0 and int(data[3]) < min:
            min = int(data[3])
        if int(data[3]) > max:
            max = int(data[3])
    return (min,max)

#calcula a distribuição da doença por níveis de colesterol
def niveisColesterol():
        min,max = minMaxColesterol()
        
        #definir o intervalo
        while min <= max:
            niveisColest[min] = 0
            min += 11
        
        #quantas pessoas com a doença existem em cada nível de colesterol
        for data in allData:
            for key in niveisColest.keys():
                if key <= int(data[3]) <= key + 10:
                    if int(data[5]) == 1:
                        niveisColest[key] += 1
                        
#imprimir tabela de sexos
def sexosTable():
    for sexo,quant in sexos.items():
        if sexo == "F": s = "Feminino"
        else: s = "Masculino"
        
        percentagem = quant/total * 100
        print (f"| {s}    |  {round(percentagem,2)} %  |")
 
#imprimir tabela de idades
def idadesTable():
      for idade,quant in escaloesEtar.items():
        percentagem = quant/total * 100
        
        print (f"| {idade} a {idade+4}  |  {round(percentagem,2)} %  |")
sexos
#imprimir tabela de níveis de colesterol
def niveisColestTable():
    for nivel,quant in niveisColest.items():
        
        percentagem = quant/total * 100
        print (f"| {nivel} a {nivel+10} |    {round(percentagem,2)} %  |")
        
        
def main():
    readFile()

    print ("1 - Tabela de Sexos")
    print ("2 - Tabela de Escalões Etários")
    print ("3 - Tabela de Níveis de Colesterol")
    print("Selecione uma das distribuições:")
    op = int(input())
    print("\n")
    
    if op == 1:
        calcSexos()
        sexosTable()
    
    elif op == 2:
        escaloesEtarios()
        idadesTable()
        
    elif op == 3:
        niveisColesterol()
        niveisColestTable()

    else:
        print("Opção é inválida!")
        main()
        
        
main()
