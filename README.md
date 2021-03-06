# Python Bot TS3LU com Selenium

![Robo Bender](https://github.com/mouracfs007/Python-Bot-TS3LU/blob/main/Imagens%20-Tutorial%20BOT%20Ts3LU/bender-robot.jpg "Bender, de futurama")

# Sobre o projeto: BOT
   ***Salve, Devs***. Venho trazer humildemente pra vocês a criação desse script bem legal e super divertido, 
  que você vai conseguir ver na prática como que funciona o mundo da programação.
  
  Pois bem, este bot ( ou script ) foi criado por mim, para atender algumas necessidades de tarefas repetitivas e super irritantes que eu fazia todos os dias,
  e o que eu fiz? eu simplesmente automatizei o processo apenas com 1 click.
  
  Na época em que foi criado o bot, eu simplesmente não tinha nenhuma experiência com o Python, não conhecia muito bem suas funções, seus tipos primitivos, sua estrutura etc.
  Eu apenas pesquisei e de forma autodidata consegui uma resolução para que eu automatizasse o processo. Lembrando de sempre ter uma base sólida de lógica de programação,
  com ela você é capaz de aprender qualquer linguagem de programação, seja ela para aplicações WEB, desktop ou Mobile.
  
  ***Uma observação:*** O python é uma linguagem de programação feita para quem nunca programou,ela nos ajuda a facilitar as nossas tarefas diarias, e que tem como seu forte sua enorme gama de bibliotecas e frameworks.
  Quando eu criei este Script, quis criar justamente sem funções, sem estruturas de repetições para mostrar o quão é possível sim construir uma resolução
  por um caminho simples para resolver determinado problema. Com o conhecimento que tenho hoje, poderia muito bem utilizar funções, como def, classes etc, mas resolvi
  optar por um caminho simples e de fácil compreensão para quem vai executar o script (bot ) em sua máquina.
  
  
  # Tutorial com imagens -- > BOTS3
  
  ## Como executar o projeto? 
  
  Primeiro de tudo, para que seja possível você ver na prática como funciona o bot, é preciso acessar o site alvo do bot. [***Click aqui***](https://www.ts3.lu/registro.php "Site do TS3LU"). E também é claro, fazer uma conta. É bem rápido, nem pede validação de email.
  
  ## Para facilitar, dividi o tutorial em uma estrutura linear em 4 passos + dicas.
  
  Os pré-requisitos para execução do projeto são:
  
  ### Passo 1º:
  
- Baixar o Python através do seu site oficial, clicando neste link : https://www.python.org/downloads/
- Não esqueça de adicionar a opção de add ao PATH quando estiver instalando o Python. Isso vai adicionar uma variável de ambiente nas configurações de seu SO.

### Passo 2º:

- Baixar o Chrome WebDriver através do endereço :https://chromedriver.chromium.org/downloads

- Verificar qual a versão do seu navegador Chrome
### Como ver a versão do meu navegador ? 
![Chrome](https://github.com/mouracfs007/Python-Bot-TS3LU/blob/main/Imagens%20-Tutorial%20BOT%20Ts3LU/drive%203.png "Chrome Webdriver")

### Baixar o exe do ChromeWebDriver com a versão compatível de seu navegador
![Chrome-exe](https://github.com/mouracfs007/Python-Bot-TS3LU/blob/main/Imagens%20-Tutorial%20BOT%20Ts3LU/drive%201.png "Chrome Webdriver")

### Baixar o arquivo de acordo com o seu tipo de sistema operacional
![Chrome-SO](https://github.com/mouracfs007/Python-Bot-TS3LU/blob/main/Imagens%20-Tutorial%20BOT%20Ts3LU/drive%202.png "Chrome Webdriver")

### Após baixar o exe do WebDriver, coloque-o dentro da pasta do seu projeto:
![Chrome-project](https://github.com/mouracfs007/Python-Bot-TS3LU/blob/main/Imagens%20-Tutorial%20BOT%20Ts3LU/drive%204.png "Chrome Webdriver")

***Observação***: Também existe uma outro alternativa para automatizar outro tipo de navegador, se chama ***geckoDriver***, funciona para navegadores mozilla.

Link para o download do GeckoDriver : https://github.com/mozilla/geckodriver/releases

No código padrão ao invés de ser: 

```
 browser = webdriver.Chrome()
```

Ficará assim ....
```
browser = webdriver.Firefox()
```

(O código mudará caso você venha por optar a usar o geckodriver ).


### Passo 3º: 

Baixar algum editor de codigo fonte ou IDE
Seja sublime text, Vs Code (Recomendado ) ou similares.


Link para o download do Vs Code: https://code.visualstudio.com/download


### Passo 4º:

### Instalando a biblioteca selenium

- Abra o seu CMD (Prompt de comandos ) ou PowerShell

Digite os comandos:
```
pip install selenium
```

![Selenium](https://github.com/mouracfs007/Python-Bot-TS3LU/blob/main/Imagens%20-Tutorial%20BOT%20Ts3LU/install%20selenium....png "Instalação do selenium como dependências")


Caso esteja desatualizado a versão do selenium apenas digite:

```
pip install --upgrade pip
```

Espere a instalação dos pacotes e feche o seu CMD. É um processo bem rápido.

Após instalar todas as dependências, abra o Vs Code, crie um arquivo .py,e dentro da pasta do seu projeto, ( Por exemplo: bots.py ), copie e cole o código python dentro desse arquivo, logo em seguida, salve o arquivo.

## Seu projeto deverá ficar dessa forma:

![Project in Python](https://github.com/mouracfs007/Python-Bot-TS3LU/blob/main/Imagens%20-Tutorial%20BOT%20Ts3LU/folder%20bots3.png "Pasta do projeto")

## E é isso aí, ufa..curtiu? finalizamos nosso tutorial. Espero vocês que tenham gostado de verdade, e que eu tenha sido o mais didático possível.

**Veja também algumas extensões que podem te ajudar na hora de codar em Python (Extensões de Vs Code )**

![Vs Code Ext](https://github.com/mouracfs007/Python-Bot-TS3LU/blob/main/Imagens%20-Tutorial%20BOT%20Ts3LU/Python%20extension%20image%20fixed.png "Extension Vs Code")


### Veja como que ficou a navegabilidade do nosso bot para WEB no Chrome: 



### Tela inicial de login
![Page 1](https://github.com/mouracfs007/Python-Bot-TS3LU/blob/main/Imagens%20-Tutorial%20BOT%20Ts3LU/page%201.png "Tela inicial")


### Clicando em três elementos da página e inserindo caracteres
![Page 2](https://github.com/mouracfs007/Python-Bot-TS3LU/blob/main/Imagens%20-Tutorial%20BOT%20Ts3LU/page%202.png "Colocando Login")


### Clicando no botão de administrador
![Page 3](https://github.com/mouracfs007/Python-Bot-TS3LU/blob/main/Imagens%20-Tutorial%20BOT%20Ts3LU/page%203.png "Clicando no painel de Administrador")


### Clicando em dois elementos da página
![Page 4](https://github.com/mouracfs007/Python-Bot-TS3LU/blob/main/Imagens%20-Tutorial%20BOT%20Ts3LU/page%204.png "Clicando na checkbox")


### Clicando em " renovar 2 dias (gratis ) " para renovar a licença do servidor
![Page 5](https://github.com/mouracfs007/Python-Bot-TS3LU/blob/main/Imagens%20-Tutorial%20BOT%20Ts3LU/page%205.png "Finalizando a requisição")
  
  Quaisquer dúvidas , troca de ideias meu e-mail de contato é : danielmourajuve21@gmail.com
  
   _By:_ Daniel Moura
  
  [![NPM](https://img.shields.io/npm/l/react)](https://github.com/mouracfs007/Python-Bot-TS3LU/blob/main/LICENSE)
