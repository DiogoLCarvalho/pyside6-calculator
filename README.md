# 🔢 Calculadora 🔢

Light         |  Dark
:-------------------------:|:-------------------------:
![light_calculator](https://github.com/DiogoLCarvalho/pyside6-calculator/assets/84794798/3032143f-f587-4596-9607-a8af6844f240)  |  ![dark_calculator](https://github.com/DiogoLCarvalho/pyside6-calculator/assets/84794798/f1c8f5d5-6b26-4975-b600-a45228be5774)

Calculadora desenvolvida em Python usando PySide6. O projeto simula a calculadora do Windows no estilo e na lógica.

## Requerimentos 🗒️

<p  'align= justify'>
Para instalar o projeto corretamente na sua máquina, é necessário ter instalado:

1. Python 11 ou inferior;
2. Pyside6;
3. pyqtdarktheme.

É possível instalar as bibliotecas individualmente ou pelo arquivo <a href="https://github.com/DiogoLCarvalho/pyside6-calculator/blob/main/requirements.txt" target="_blank">requirements.txt</a>  dentro do repositório, para isso faça um clone do repositório e em seu terminal digite o comando: 

```py 

pip install -r .\requirements.txt

```

Este comando irá instalar todas as dependências necessárias para o projeto funcionar. Lembrando que <b>a versão do Python precisa ser no máximo a versão 11</b>, porque algumas bibliotecas utilizadas ainda não dão suporte para o Python 12, pelo menos até o momento atual da criação desse readme :)
</p>

## Sobre o projeto ✒️
<p  'align= justify'>

O projeto é dividido em 4 partes. 

Na raiz do projeto tem o arquivo **main.py**, nele todas as classes são integradas e é o arquivo que deve ser executado. 

Na pasta **modules**, é armazenada os módulos e classes que compõem a calculadora, sendo que: 

*appWindow.py*
* QMainWindow do projeto, que é o container principal da calculadora;
* Nesse projeto não foi utilizado o Qt Designer, todo layout foi feito manualmente.

*buttons.py*
* Classe dos botões e layout dos botões;
* Toda lógica de Slots e connect dos botões ou teclas estão nessa classe. 

*display.py*
* Classe do display da calculadora;
* Faz o emit da teclas do teclado.

*operationsText.py*
* Classe que auxilia as operações;
* Texto que aparece em cima do display.

Por último, a pasta **utils**,  que armazena funções de segurança para a aplicação, caminhos para a imagem de ícone e toda a lógica do tema da calculadora. Lembrando que as cores do tema foram modificadas, especialmente na função *setupTheme*:

<p align="center">
   <img src="https://github.com/DiogoLCarvalho/pyside6-calculator/assets/84794798/92dbbba9-5dd2-494e-8bbe-d755818c1bd4" width="60%" >
</p>

</p>

## Teclas de atalho :keyboard:

É possível realizar as operações pelas teclas do teclado, os comandos são:

  - `Atalhos`: 
    - `Enter, Return, =` : Exibe o resultado
    - `delete, backspace, d`: Remove um elemento do display
    - `escape, c`: Limpar toda a operação
    - `+, -, /, *, p`: Realiza operações
      
Vale mencionar que dependendo do teclado utilizado algumas funções podem ser diferentes.  

## Demonstração final 📹
<p align="center">
   <img src="https://github.com/DiogoLCarvalho/pyside6-calculator/assets/84794798/0dbc8989-13ff-4cc9-a1f8-3ce8632ec154" width="30%" >
</p>


## Links úteis 🔗
Python:
* https://www.python.org/downloads/
  
Bibliotecas usadas: 
* https://pypi.org/project/PySide6/
* https://pypi.org/project/pyqtdarktheme/

<br>


<h6 align='right'>Obrigado pela atenção! Até a próxima 👍</h6> 

