import random
import os

def clear():{
    os.system('cls||clear')
}

valO = random.randint(1,100)
clear()

i = 7

print(f"\nVocê tem {i} tentativas")
#para verificar o valoR sorteado
#print(valO)

Question = int(input("Qual número você acha que foi sorteado?\n>>> "))



while i != 0:
    if (Question < valO):
        i-=1
        clear()
        print("\nTente um número maior desta vez...\n")
        
        
    if (Question > valO):
        i-=1
        clear()
        print("\nTente um número menor desta vez...\n")
        
    
    if Question == valO:
        clear()
        print("\nParabénss!!!!!\nVocê descobriu o número perdido\n")
        break   
    if i==0:
        continue

    print(f"Você tem {i} tentativas restantes\n")

    Question = int(input("Qual número você acha que foi sorteado?\n>>> "))
    clear()
    

while i==0:

    if i == 0:
            result = int(input(f"\nVocê perdeu gostaria de ver o resultado?\n(1)Sim\n(2)Não\n\n>>> "))
            if result ==1:
                clear()
                print(f"O número sorteado foi {valO}\n")
                exit()
            if result ==2:
                clear()
                print("Ok, tchau\n")
                exit()
            else:
                clear()
                print("Hmmm, não consegui identificar a sua resposta com as opções dadas.\n")
            
