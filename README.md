Desafio de Análise de Conversas com OpenAI
Este projeto é uma aplicação que analisa conversas de atendimento, utilizando a API OpenAI (GPT-4o-mini) para extrair informações relevantes, como:

Satisfaction: Nota de satisfação do cliente (0 a 10)
Summary: Resumo da conversa
Improvement: Sugestões de melhoria para o atendimento
A análise é feita automaticamente ao iniciar a aplicação via Docker Compose, e os resultados são armazenados em um banco de dados PostgreSQL utilizando Prisma ORM.


📌 Tecnologias Utilizadas
Python 3.10 – Backend da aplicação
FastAPI – API para gerenciar o serviço de análise
OpenAI GPT-4o-mini – Inteligência artificial para análise das conversas
Prisma ORM – Gerenciamento do banco de dados
PostgreSQL – Banco de dados para armazenar as mensagens e análises
Docker & Docker Compose – Orquestração dos serviços


🚀 Instalação e Execução
1️⃣ Pré-requisitos
Antes de rodar a aplicação, certifique-se de que tem os seguintes programas instalados:

Docker Desktop (com Docker Compose)
Uma chave da API OpenAI (solicite ao entrevistador)
2️⃣ Configuração do Projeto
Clone este repositório:
git clone https://github.com/seu-repositorio/desafio_analise_conversa_openai.git
cd desafio_analise_conversa_openai


Crie um arquivo .env com as credenciais:
cp .env.example .env

Edite o arquivo .env e adicione sua chave da API OpenAI:
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
DATABASE_URL=postgresql://user:password@db:5432/database

3️⃣ Executar a Aplicação com Docker
Agora, basta rodar o comando abaixo para iniciar a aplicação:
docker-compose up --build

Isso fará o seguinte:

Iniciará o banco de dados PostgreSQL no Docker
Criará a estrutura do banco de dados utilizando Prisma ORM
Executará o serviço FastAPI, que analisará automaticamente as conversas

📊 Funcionamento da Aplicação
A aplicação busca todas as sessões de conversa no banco de dados.
Para cada sessão, recupera todas as mensagens trocadas entre cliente e assistente.
As mensagens são enviadas para a API OpenAI, que retorna:
Nota de satisfação do cliente (0 a 10)
Resumo da conversa
Sugestões de melhoria para o atendimento
Os dados são armazenados no banco de dados na tabela analysis.

📂 Estrutura do Projeto:
/app
  ├── main.py               # Arquivo principal (API FastAPI)
  ├── database.py           # Conexão com o banco de dados (Prisma)
  ├── models.py             # Modelos de dados do Prisma
  ├── openai_service.py     # Comunicação com a API OpenAI
  ├── analysis_service.py   # Processamento das conversas
  ├── Dockerfile            # Configuração do contêiner Docker
  ├── requirements.txt      # Dependências do projeto
  ├── .env                  # Configuração do ambiente
  ├── docker-compose.yml    # Orquestração dos serviços no Docker

🛠 Comandos Úteis
1️⃣ Parar a Aplicação:
docker-compose down

2️⃣ Recriar os Contêineres
Se fizer alterações no código, use:
docker-compose up --build

3️⃣ Acessar o Banco de Dados (PostgreSQL)
Se precisar acessar o banco de dados, rode:
docker exec -it CONTAINER_ID psql -U user -d database
(O CONTAINER_ID pode ser obtido com docker ps).

🔥 Possíveis Erros e Soluções
❌ Erro: docker-compose: command not found
Solução: Use docker compose (sem o hífen) em vez de docker-compose.

❌ Erro: No module named openai
Solução: O pacote OpenAI não está instalado. Execute dentro do contêiner:
docker exec -it CONTAINER_ID pip install -r requirements.txt

❌ Erro: Database connection failed
Solução: Certifique-se de que o banco de dados está rodando e as credenciais no .env estão corretas.

📢 Conclusão
Essa aplicação permite analisar conversas de atendimento de forma automatizada, utilizando IA para avaliar a qualidade do suporte e sugerir melhorias. 🚀

Se tiver dúvidas ou sugestões, entre em contato! 😊
