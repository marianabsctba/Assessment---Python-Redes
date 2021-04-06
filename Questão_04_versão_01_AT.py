
def reversed_file():
    words = []
    try:
        with open('questao4.txt', 'r') as file:
            for texts in file:
                for word in texts:
                    words.append(word)

        words.reverse()

        for texts in words:
            print(texts, end='')

    except FileNotFoundError as error:
        print(error)


reversed_file()
