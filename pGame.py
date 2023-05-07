import random

i = 7
print(f"\nVocê tem {i} tentativas")
Question = int(input("Qual número você acha que foi sorteado?\n>>> "))


valO = random.randint(1,100)
print(valO)
while i != 0:
    if (Question < valO):
        i-=1
        print("\nTente um número maior desta vez...\n")

        
    if (Question > valO):
        i-=1
        print("\nTente um número menor desta vez...\n")
    
    if Question == valO:
        print("\nParabénss!!!!!\nVocê descobriu o número perdido")
        break
    print(f"\nVocê tem {i} tentativas restantes\n")

    Question = int(input("Qual número você acha que foi sorteado?\n>>> "))

if i == 0:
        result = int(input(f"\nVocê perdeu gostaria de ver o resultado?\n(1)Sim\n(2)Não\n\n>>> "))
        if result ==1:
            print(f"O número sorteado foi {valO}")
        if result !=1:
            print("Ok, tchau")
