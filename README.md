# Boas-vindas ao projeto do TING (Trybe is not Google)!

Este é um projeto que foi desenvolvido durante o curso de Desenvolvimento Web na Trybe.

## Funcções

Neste projeto foi implementado um programa que simula um algoritmo de indexação de documentos similar ao do Google. Seu programa deverá ser capaz de identificar ocorrências de termos em arquivos _TXT_.

## Habilidades Desenvolvidas

 - Manipular Pilhas;

 - Manipular Deque;

 - Manipular Nó & Listas Ligadas e;

 - Manipular Listas Duplamente Ligadas.

# Antes de começar a desenvolver

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:mabiiak/TING.git`
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd TING`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`

  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`

  4. Crie uma branch a partir da branch `main`

  - Verifique que você está na branch `main`
    - Exemplo: `git branch`
  - Se não estiver, mude para a branch `main`
    - Exemplo: `git checkout main`
  - Agora crie uma branch à qual você vai submeter os `commits` do seu projeto
    - Você deve criar uma branch no seguinte formato: `nome-github-nome-do-projeto`
    - Exemplo: `git checkout -b joaozinho-ting`

  5. Adicione as mudanças ao _stage_ do Git e faça um `commit`

  - Verifique que as mudanças ainda não estão no _stage_
    - Exemplo: `git status` (deve aparecer listada a pasta _joaozinho_ em vermelho)
  - Adicione o novo arquivo ao _stage_ do Git
    - Exemplo:
      - `git add .` (adicionando todas as mudanças - _que estavam em vermelho_ - ao stage do Git)
      - `git status` (deve aparecer listado o arquivo _joaozinho/README.md_ em verde)
  - Faça o `commit` inicial
    - Exemplo:
      - `git commit -m 'iniciando o projeto ting'` (fazendo o primeiro commit)
      - `git status` (deve aparecer uma mensagem tipo _nothing to commit_ )

  6. Adicione a sua branch com o novo `commit` ao repositório remoto

  - Usando o exemplo anterior: `git push -u origin joaozinho-ting`

  7. Crie um novo `Pull Request` _(PR)_


<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado ambiente virtual que permite sua máquina rodar, sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas. Para utilizar este recurso siga os passos a seguir:

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo as dependências serão instaladas neste ambiente.
  
  :eyes: Caso precise desativar o ambiente virtual execute o comando _"deactivate"_.
  
  :warning: Lembre-se de ativar o ambiente virtual novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

## Requisitos do projeto

    ✅ 1 Implemente uma fila para armazenar os arquivos que serão lidos.

    ✅ 2 Implemente uma função `txt_importer` dentro do módulo `file_management` capaz de importar notícias a partir de um arquivo TXT, utilizando "\n" como separador.

    ✅ 3 - Implemente uma função `process` dentro do módulo `file_process` capaz de ler o arquivo carregado na função anterior e efetuar o pré-processamento do conteúdo.

    ✅ 4 Implemente uma função `remove` dentro do módulo `file_process` capaz de remover o primeiro arquivo processado

    ✅ 5 Implemente uma função `file_metadata` dentro do módulo `file_process` capaz de apresentar as informações superficiais de um arquivo processado.

    ✅ 6 Implemente uma função `exists_word`, dentro do módulo `word_search`, que verifique a existência de uma palavra em todos os arquivos processados.

    ✅ 7 Implemente uma função `search_by_word` dentro do módulo `word_search`, que busque uma palavra em todos os arquivos processados.

## Obrigada pela visita!
