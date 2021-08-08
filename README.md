## Executando a Solução
```
git clone https://github.com/talvane/desafio-backend
cd /projeto
pipenv shell
pipenv install
Renomear .env.example para .env e preencher a SECRET_KEY
pipenv run python manage.py migrate
pipenv run python manage.py createsuperuser
pipenv run python manage.py runserver
pipenv run python manage.py test
```

## Acessando os Dados
- Admin -> http://127.0.0.1:8000/admin
- Testes via Swagger API -> http://127.0.0.1:8000/api/v1/swagger/



# Desafio backend
A idéia deste desafio é nos permitir avaliar melhor as habilidades de candidatos à vagas de desenvolvedor, de vários níveis.

Este desafio deve ser feito por você em sua casa. Gaste o tempo que você quiser, porém normalmente você não deve precisar de mais do que algumas horas.

## Instruções de entrega do desafio
1. Primeiro, faça um fork deste projeto para sua conta no Github (crie uma se você não possuir).
1. Em seguida, implemente o projeto tal qual descrito abaixo, em seu próprio fork.
1. Por fim, empurre todas as suas alterações para o seu fork no Github e envie um pull request para este repositório original. Se você já entrou em contato com alguém da Garage Geek sobre uma vaga, avise também essa pessoa por email, incluindo no email o seu usuário no Github.

## Instruções alternativas de entrega do desafio (caso você não queira que sua submissão seja pública)
1. Faça um clone deste repositório.
1. Em seguida, implemente o projeto tal qual descrito abaixo, em seu clone local.
1. Por fim, envie via email um arquivo patch para seu contato na Garage Geek.

## Descrição do projeto

Desenvolver um sistema para cadastrar estados e cidades Brasileiras.

Sua tarefa é criar uma interface web que aceite o cadastro de estados e cidades Brasileiras, normalize os dados e armazene-os em um banco de dados relacional.

Sua aplicação web DEVE:

1. Aceitar (via uma API REST) o cadastro de estados
1. Aceitar (via uma API REST) o cadastro de cidades
1. Listar todas as cidades e estados cadastrados
1. Ser escrita obrigatoriamente em Ruby 2.0+, Python 3.6+, Java 7+ ou PHP 5.3+ (caso esteja entrevistando para uma vaga específica, utilize a linguagem solicitada pela vaga).
1. Ser simples de configurar e rodar, funcionando em ambiente compatível com Unix (Linux ou Mac OS X). Ela deve utilizar apenas linguagens e bibliotecas livres ou gratuitas.

Sua aplicação web não precisa:

1. Lidar com autenticação ou autorização (pontos extras se ela fizer, mais pontos extras se a autenticação for feita via OAuth).
1. Ser escrita usando algum framework específico (mas não há nada errado em usá-los também, use o que achar melhor).
1. Ter uma aparência bonita.

## Avaliação
Seu projeto será avaliado de acordo com os seguintes critérios.

1. Sua aplicação preenche os requerimentos básicos?
1. Você documentou a maneira de configurar o ambiente e rodar sua aplicação?
1. Você seguiu as instruções de envio do desafio?
1. Qualidade e cobertura dos testes unitários.

Adicionalmente, tentaremos verificar a sua familiarização com as bibliotecas padrões (standard libs), bem como sua experiência com programação orientada a objetos a partir da estrutura de seu projeto.
