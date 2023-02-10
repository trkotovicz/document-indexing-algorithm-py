# Algoritmo de Indexação de Documentos

Programa que simula um algoritmo de indexação de documentos similar ao do Google. Ele é capaz de identificar ocorrências de termos em arquivos TXT.

Este projeto não tem como foco a análise de significados ou busca por sinônimos.

## Contexto

O programa simula o algoritmo de indexação de documentos similar ao do google. Ou seja, um programa que permite anexar arquivos de texto e posteriormente operar funções de busca sobre tais arquivos.

Com a quantidade de informações disponíveis na Web, encontrar o que você precisa seria quase impossível sem nenhuma ajuda para classificá-las. Os sistemas de classificação do Google organizam centenas de bilhões de páginas da Web, no índice da pesquisa, para fornecer os resultados mais úteis e relevantes em uma fração de segundo. Além disso tudo, a a Google também precisa se preocupar em apresentar os resultados de uma maneira que ajude você a encontrar o que está procurando com mais facilidade ainda.

### Analisar palavras

Compreender o significado da sua pesquisa é crucial para retornarmos boas respostas. Por isso, para encontrar páginas com informações relevantes, nosso primeiro passo é analisar o significado das palavras na consulta de pesquisa. Desenvolvemos modelos linguísticos para decifrar as sequências de palavras que precisamos procurar no índice.

Não iremos nos apegar a análise de significados ou busca por sinônimos. Nosso objetivo será identificar ocorrências de termos em arquivos TXT. Neste contexto, foi criado um programa que permite anexar arquivos de texto e posteriormente operar funções de busca sobre tais arquivos.

Sendo assim o programa possui dois módulos:

- Modo gerenciamento de arquivos;
- Modo de buscas.

</br>

## Habilidades desenvolvidas:

Manipulação de Pilhas.</br>
Manipulação de Deque.</br>
Manipulação de Nó & Listas Ligadas.</br>
Manipulação de Listas Duplamente Ligadas.</br>


## Ambiente Virtual

O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.</br>

Criar o ambiente virtual
```
$ python3 -m venv .venv
```

Ativar o ambiente virtual
```
$ source .venv/bin/activate
```

Instalar as dependências no ambiente virtual
```
$ python3 -m pip install -r dev-requirements.txt
```
Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
Quando precisar desativar o ambiente virtual, execute o comando "deactivate".

O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto.


---


</br>

Projeto desenvolvido por [Thais R Kotovicz](https://www.linkedin.com/in/thaiskotovicz/).
</br>

