# Atividade ponderada semana 3 

## Objetivo

O objetivo desse ponderada é criar um pacote de ros que permita o usuaŕio mapear um ambiente utilizando o turtlebot3 e após isso fornecer ao robô pontos para navegar no ambiente mapeado.


## Como usar

Para usar esse pacote é necessário ter o ros instalado, o turtlebot3, rvis e o nav2( zero de chance de eu explicar como instala tudo isso vai na doc do Nicola para ver como faz isso:<https://rmnicola.github.io/m8-ec-encontros/sprint2/encontro4/nav2/>).Instale xterm com o seguinte comando:

```bash
    sudo apt-get install xterm
```

Clone o repositório com o comando:

```bash
    git clone https://github.com/angrysine/ponderada3m8.git
```

Após isso, entre na pasta pacote do repositório e execute o comando:

```bash
    source /install/setup.bash
```

Após isso, execute o comando:

```bash
    cd /launch
    ros2 launch map.launch.py
```

Esse comando permite que o usuário mapeie o ambiente, para mover o robo selecione o terminal gerado pelo xterm use as tecla awsd para controlar o robô e termine o mapeamento com ctrl+c no terminal. após issso rode:

```bash
    cd /launch
    ros2 launch run.launch.py
```

Esse comando permitira o usuário fornecer pontos para o robô navegar no ambiente mapeado, para isso selecione o terminal gerado pelo xterm e use as teclas e insira 2 números com espaço entre si e aperte enter para fornecer um ponto para o robô navegar, para finalizar o programa  digite exit no terminal sem espaços e aperte enter.

## video

Um vídeo se encontra na root do repositório junto com o readme.md.