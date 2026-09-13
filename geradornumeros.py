"""
1 - criar programa para gerar numero aleatorio entre 1 e 50
2 - não aceitara letras ou numeros maior/menor que o estimado
3 - se acertar, o programa encerra
4 - se errar, ele mostrara quantas chances ainda faltam
5 - irá mostrar se o numero é maior ou menor que o escolhido
"""

import random

secret_number = random.randint(1, 50)
attempts = 0
max_attempts = 5

print("ADIVINHE O NUMERO DE 1 A 50")
print("=" * 17)
print(f"voce tem somente {max_attempts} tentativas")
print("\n")

while attempts < 5:
    try:
        number = int(input("escolha um número aleatório: "))

        if number < 1 or number > 50:
            print("digite um numero entre 1 e 50!!!!")
            continue
    except ValueError:
        print("DIGITE APENAS NUMEROS")
        continue

    attempts += 1

    if number == secret_number:
        print("ACERTOU MISERAVI🔥🔥🔥")
        correct = True
        break
    elif number < secret_number:
        print(f"o numero é maior, voce ainda tem {max_attempts - attempts} tentativas")
    elif number > secret_number:
        print(f"o numero é menor, voce ainda tem {max_attempts - attempts} tentativas")

if number != secret_number:
    print(f"mais sorte na proxima vez, seu numero era {secret_number}")
