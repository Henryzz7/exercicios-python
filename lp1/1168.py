n = int(input())

for a in range(n):
    leds = input()
    vet = list(leds)
    count = 0
    for i in range(len(leds)):
        if vet[i] == '1':
            count += 2
        elif vet[i] == '2' or vet[i] == '3' or vet[i] == '5':
            count +=5
        elif vet[i] == '4':
            count +=4
        elif vet[i] == '6' or vet[i] == '9' or vet[i] == '0':
            count+=6
        elif vet[i] == '7':
            count+=3
        elif vet[i] == '8':
            count+=7
    print(f'{count} leds')