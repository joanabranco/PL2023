#separa o texto recebido pelo terminal
def readTexto(texto):
    on = True
    soma=0 
    i=0
    
    while i != len(texto):
        if on:
            #se for um número
            if texto[i].isdigit(): 
                n = int(texto[i])
                soma+=n
                
            #se for off 
            elif texto[i:i+3].lower() == "off": #entre texto[i] e texto[i+3] existe off escrito de qualquer forma
                on = False
                i+=2 #passa à frente os 2 caracteres seguintes correspondentes ao off 
                
            #se for o símbolo =
            elif texto[i] == "=":
                print(f"A soma é: {soma}")
                
        else:
            #se for on 
            if texto[i:i+2].lower() == "on": #entre texto[i] e texto[i+3] existe on escrito de qualquer forma
                on = True
                i+=1 #passa à frente o caracter seguinte correspondente a on
                
            #se for o símbolo =
            elif texto[i] == "=":
                print(f"A soma é: {soma}")
                
        i+=1 #avançar para o próximo caracter
            
def main():
    print("Insira um texto: ")    
    #olaee20ihihon100=40ffastt oFf32 ON=18On=on
    
    texto = input()
    readTexto(texto)
    
main()    