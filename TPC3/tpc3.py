import datetime
import re
data = {} #organizar a info dependente do número do processo
freqProcessos = {} #dicionario que armazena a frequência de processos por ano

#ler o ficheiro e organizar os dados
def readFile():  
    with open("processos.txt", "r") as file:
        for line in file.readlines(): 
            fields = line.strip().split('::') 
            key = fields[0] #processo vai ser a chave
            if key not in data: 
                data[key] = {} 
            for i in range(1, len(fields)): 
                if fields[i]: 
                    if i not in data[key]: 
                        data[key][i] = [] 
                    data[key][i].append(fields[i]) #adicionar o campo à lista correspondente

def okDate (date_str):
    if  (datetime.datetime.strptime(date_str, '%Y-%m-%d')):
        return True

# frequência de processos por ano
def procPorAno():    
    #exp.reg. re.match(r'^\d{4}', value[1][0])
    for value in data.values():
        date = value[1][0]
        if okDate (date):
            year = value[1][0][:4]  #dá o segundo elemento do dicionário e depois, o primeiro caracter da data até ao quarto
            freqProcessos[year] = freqProcessos.get(year, 0) + 1
            
    return freqProcessos


def main():
    readFile()
    print ("1 - Frequência de processos por ano")
    print ("2 - Frequeência de nomes próprios e apelidos por séculos")
    print ("3 - Frequência dos vários tipos de relação")
    print ("4 - Conversão dos primeiros 20 registos num novo ficheiro de output (Json)")
    print("Selecione uma das distribuições:")
    op = int(input())
    print("\n")
    
    if op == 1:
        print(procPorAno())
    



main()