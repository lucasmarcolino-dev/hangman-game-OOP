# Hangman Game 🎯

Bem-vindo ao **Hangman Game**, um jogo de forca feito em Python!

---

## 🛠️ **Pré-requisitos**
Para rodar o jogo no seu ambiente local, você precisará do seguinte:
- **Python 3.x** instalado

---

## ▶️ **Como executar o jogo**
1. Clone este repositório em sua máquina:
   ```bash
   git clone https://github.com/lucasmarcolino-dev/hangman-game-OOP.git
   cd hangman-game-OOP
   ```
2Execute o arquivo principal:
   ```bash
   python main.py
   ```

---

## 🎮 **Como jogar**
1. O jogo sorteará uma palavra e exibirá os espaços correspondentes.
2. Insira uma letra por vez para tentar adivinhar.
3. Você pode errar até 6 vezes antes do **Game Over**.
4. Se acertar todas as letras, você ganha! 🏆

---

## 📂 **Estrutura do projeto**
```bash
hangman-game-OOP/
│
├── words.csv               # Arquivo de palavras usadas no jogo
├── main.py                 # Arquivo principal com a implementação do jogo
```

---

## 🔧 **Personalização**
Você pode adicionar mais palavras ao arquivo `words.csv`, colocando uma palavra por linha.

Exemplo de `words.csv`:
```csv
python
jogo
forca
programacao
```

---

## 📝 **Notas de uso**
- Certifique-se de que o `words.csv` esteja no mesmo diretório do `main.py`.
- Caso tenha problemas de caminho, verifique o diretório de execução no PyCharm em **Run > Edit Configurations > Working Directory**.

---