# Alien Invaders

Alien Invaders é um jogo inspirado no clássico Space Invaders, desenvolvido com a biblioteca Pygame. Este projeto é baseado nos capítulos 12, 13 e 14 do livro "Python Crash Course" de Eric Matthes com minhas modificações.

## Modificações do projeto
 - Maior quantidade e tipos de projéteis.
 - Alternacia entre tela simples e Fullscreen.
 - Botão de pause.
 - Movimentação de nave do jogador para todas as direções.

## Pré-requisitos

- Python 3.6 ou superior
- Pygame

## Instalação

1. **Clone o repositório:**

    ```bash
   git clone git@github.com:Sicarruda/attack-invasion.git

2. **Navegue até o diretório do projeto:**

    ```bash
   cd alien_invaders

3. **Crie e ative um ambiente virtual (opcional, mas recomendado):**

    ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows

4. **Instale as dependências:**

    ```bash
   pip install -r requirements.txt

Se o arquivo requirements.txt não estiver presente, você pode instalar o Pygame diretamente:
    
    pip install pygame

## Como jogar
Inicie o jogo:

    python3 alien_invasion.py

Controles do jogo:

- Pressione **q** para fechar o jogo.
- Pressione **f** para alternar entre tela cheia e modo janela.
- Pressione **p** para iniciar ou pausar o jogo.
- Pressione as teclas de direção para movimentar a nave.
- Pressione **espaço** para disparar.
- Alterne entre os projéteis utilizando **1**, **2**, **3** ou **4**

## Estrutura do projeto

    attack-invasion/
    ├── alien_invasion.py      # Arquivo principal para iniciar o jogo
    ├── settings.py            # Configurações do jogo
    ├── ship.py                # Classe da nave do jogador
    ├── alien.py               # Classe dos alienígenas
    ├── bullet.py              # Classe dos projéteis
    ├── bullet_black.py        # Classe para projetil especifico
    ├── bullet_green.py        # Classe para projetil especifico
    ├── bullet_blue.py         # Classe para projetil especifico
    ├── bullet_red.py          # Classe para projetil especifico
    ├── scoreboard.py          # Placar do jogo
    ├── button.py              # Classe de botões do jogo
    ├── pause_button.py        # Classe para o botão de pausa
    ├── game_stats.py          # Classe de para controle das estatisticas do jogo
    └── README.md              # Este arquivo
## Referência

Este jogo foi desenvolvido como parte dos exercícios do livro "Python Crash Course" de Eric Matthes. Agradecimentos especiais ao autor e à comunidade de desenvolvedores Python.

 - [Python Crash Course](https://ehmatthes.github.io/pcc_3e/)
 - [Pygame Documentation](https://www.pygame.org/docs/ref/pygame.html)
 
## Licença

[MIT](https://choosealicense.com/licenses/mit/)

Sinta-se à vontade para ajustar qualquer parte conforme necessário para o seu projeto específico. Se precisar de mais alguma coisa, estou aqui para ajudar!
