# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

import random as rd
import csv

# arquivo de palavras
reader = csv.reader(open('words.csv', 'r'))

# Escolher palavra resposta
words = []
for line in reader:
    words.append(line[0])

# Board (tabuleiro)
board = ['''
+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    def __init__(self, word = rd.choice(words)):
        self.word = word
        self.list_word = list(word)
        self.answers = []
        self.errors = 0
        self.list_underscore = [' _ ' for letter in self.word]

    def show_underscore(self):
        for i in self.list_underscore:
            print(i, end='')

    def show_board(self):
        print(board[self.errors])

    def show_answers(self):
        print('Letras que já foram: ', self.answers, end=' ')

    def check_letter(self, letter):
        if not (letter in self.answers):
            self.answers.append(letter)
            if letter in self.word:
                for i in range(len(self.list_word)):
                    if self.list_word[i] == letter:
                        self.list_underscore[i] = letter
            else:
                self.errors += 1
                if self.errors == 6:
                    self.show_board()
                    print()
                    print('Você perdeu!')
                    print('A palavra era: ' + self.word)
        else:
            print('Letra já inserida! Insira outra letra')
if __name__ == '__main__':
    print('>>>>>>>>>>Hangman<<<<<<<<<<')

    player1 = Hangman()

    while player1.errors < 6:

        if player1.list_underscore != player1.list_word:
            player1.show_answers()

            player1.show_board()

            player1.show_underscore()

            player1.check_letter(input('\n\nInsira a letra: '))
        else:
            print('Você acertou!')
            break