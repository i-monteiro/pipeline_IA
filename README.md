# CRM e Assistente Inteligente

Bem-vindo ao **CRM e Assistente Inteligente**, um projeto que integra um sistema de CRM simples com um assistente virtual avançado. O sistema permite o registro de vendas, armazenamento em um banco de dados PostgreSQL, geração de relatórios em JSON e interação com um assistente inteligente que responde a perguntas sobre os dados, fornecendo respostas em texto e áudio.

## Índice

- [Descrição do Projeto](#descrição-do-projeto)
- [Funcionalidades](#funcionalidades)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Descrição do Projeto

O projeto consiste em:

1. **Sistema de CRM e Vendas**: Uma interface simples construída com Streamlit para inserir dados de vendas, como e-mail do cliente, data e hora da compra, valor, quantidade e produto. Os dados são validados e salvos em um banco de dados PostgreSQL (Render).

2. **Assistente Inteligente**: Utiliza a API da OpenAI para criar um assistente virtual que responde a perguntas sobre os dados de vendas. O assistente está habilitado com pesquisa de arquivos e armazena dados em um Vector Store.

3. **Respostas em Áudio**: Integração com a API da ElevenLabs para converter as respostas do assistente em áudio, proporcionando uma experiência interativa ao usuário.

4. **Exportação de Dados**: Extrai os dados do banco de dados PostgreSQL e os salva em arquivos JSON, permitindo que o assistente acesse e processe as informações.

## Funcionalidades

- **Registro de Vendas**: Interface amigável para inserir e validar dados de vendas.
- **Armazenamento de Dados**: Salva os registros em um banco de dados PostgreSQL.
- **Assistente Virtual**: Responde a perguntas sobre os dados de vendas, utilizando GPT-4.
- **Respostas em Áudio**: Converte as respostas do assistente em áudio usando a ElevenLabs.
- **Exportação para JSON**: Exporta os dados do banco para arquivos JSON para análise e processamento.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:

- **Python 3.12**
- **Pip** (gerenciador de pacotes do Python)
- **PostgreSQL** (servidor de banco de dados)

## Instalação

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/i-monteiro/pipeline_IA.git
   cd pipeline_IA
   ```

2. **Crie um ambiente virtual**:

   ```bash
   python -m venv .venv
   Windows: source .venv\Scripts\activate
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados PostgreSQL**:

   - Crie um banco de dados com o nome apropriado.
   - Crie uma tabela `vendas` com a estrutura apropriada.

## Configuração

1. **Arquivo `.env`**:

   Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

   ```env
   # Chaves de API
   API_KEY=sua_chave_api_openai
   ELEVEN_API_KEY=sua_chave_api_elevenlabs
   ASSISTANT_ID=seu_id_assistente

   # Configurações do banco de dados
   DB_HOST=localhost
   DB_NAME=nome_do_banco
   DB_USER=seu_usuario
   DB_PASS=sua_senha
   ```

2. **Configuração do Assistente**:

   - Substitua `sua_chave_api_openai` pela sua chave da OpenAI.
   - Substitua `sua_chave_api_elevenlabs` pela sua chave da ElevenLabs.
   - Substitua `seu_id_assistente` pelo ID do assistente criado.

## Uso

### 1. Executar o Sistema de CRM e Vendas

Inicie o aplicativo Streamlit para inserir vendas:

```bash
streamlit run crm_app.py
```

Onde `crm_app.py` é o arquivo que contém o código do sistema de CRM.

### 2. Criar o Assistente e Carregar Dados

Execute o script para criar o assistente, o Vector Store e carregar os dados:

```bash
python criar_assistente.py
```

Onde `criar_assistente.py` é o arquivo que contém o código para configurar o assistente.

### 3. Atualizar os Dados e Gerar JSON

Após inserir novos dados, execute o script para exportar os dados do banco para JSON:

```bash
python salvar_dados_json.py
```

Onde `salvar_dados_json.py` é o arquivo que contém o código para exportar os dados.

### 4. Interagir com o Assistente

Inicie o aplicativo Streamlit que permite interagir com o assistente:

```bash
streamlit run chat_assistente.py
```

Onde `chat_assistente.py` é o arquivo que contém o código para interação com o assistente.

## Estrutura do Projeto

- **crm_app.py**: Interface para inserção de vendas.
- **criar_assistente.py**: Configuração do assistente e Vector Store.
- **chat_assistente.py**: Interface para interagir com o assistente.
- **salvar_dados_json.py**: Exporta dados do banco para JSON.
- **contrato.py**: Definição do modelo de dados com Pydantic.
- **database.py**: Funções para salvar dados no PostgreSQL.
- **.env**: Variáveis de ambiente (não incluído no repositório).
- **requirements.txt**: Lista de dependências do projeto.

## Tecnologias Utilizadas

- **Python 3.12**
- **Streamlit**: Criação de interfaces web simples.
- **OpenAI API**: Assistente virtual com GPT-4.
- **ElevenLabs API**: Conversão de texto em fala.
- **Pydantic**: Validação de dados.
- **Render -> PostgreSQL**: Banco de dados.
- **psycopg2**: Conexão com PostgreSQL.
- **dotenv**: Gerenciamento de variáveis de ambiente.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---

**Nota**: Certifique-se de substituir os arquivos e caminhos pelos nomes reais dos seus arquivos no projeto. Além disso, lembre-se de não compartilhar suas chaves de API publicamente.