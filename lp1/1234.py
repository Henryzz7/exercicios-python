while True:
    try:

        mensagem = input()
        count = 0
        result = ''

        for i in range(len(mensagem)):
            if mensagem[i].isalpha():
                if count % 2 == 0:
                    result += mensagem[i].upper()
                else:
                    result += mensagem[i].lower()
                count += 1
            else:
                result += mensagem[i]
        print(result)
    except EOFError:
        break