tentativas = 3

for i in range(3):
    try:
        real = float(input())
    except ValueError:
        # Reduz o número de tentativas e envia uma mensagem com a quantidade atual de tentativas
        tentativas -= 1
        if (tentativas > 0):
            print(f'Valor invalido. Você ainda tem {tentativas} tentativa(s).')
            pass
        else:
            print("Limite de tentativas excedido. Reinicie a aplicação...")
            break
            # Para a execução quando o limite de tentativas chega a 0
    else:
        print(f'Valor inserido: {real}')
        break
        # Para a execução se não tiver nenhuma exceção

