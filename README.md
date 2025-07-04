# 📬 AutoU - Classificador Inteligente de E-mails

Este projeto é uma aplicação web desenvolvida em **Python + Flask** que classifica mensagens recebidas como **Produtivas** ou **Improdutivas** e ainda gera **respostas automáticas** com base no conteúdo da mensagem.  
Ideal para ambientes corporativos que lidam com alto volume de e-mails e precisam ganhar tempo com atendimento e triagem.

---

## 🚀 Funcionalidades

- Upload de arquivos `.txt` ou `.pdf` com mensagens
- Classificação automática via **IA** (Hugging Face - Mistral 7B)
- Geração de respostas automáticas e objetivas
- Interface web responsiva
- Histórico de mensagens com opção de exclusão

---

## 🧪 Tecnologias Utilizadas

- Python 3.13+
- Flask
- HuggingFace Hub (API - Mistral 7B Instruct)
- HTML5 + CSS3
- Deploy via Render

---

## ⚙️ Como executar localmente

1. Clone o repositório:

```bash
git clone https://github.com/Natanpython/AutoU-_-Desenvolvimento-master.git
cd AutoU-_-Desenvolvimento-master
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz do projeto com a variável de API:

```env
HUGGINGFACE_API_KEY=seu_token_aqui
```

---

## 🔐 Sobre o arquivo `.env` e o Token da Hugging Face

Para garantir a segurança e integridade do projeto, **o token da Hugging Face não está incluído diretamente no repositório**, especialmente se estiver público.  
A Hugging Face automaticamente revoga chaves expostas por razões de segurança.

Você tem duas opções:

- Gerar um novo token em: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)  
- Usar o token abaixo (caso disponibilizado separadamente), **removendo eventuais espaços** e colando no `.env`.

Exemplo de conteúdo do arquivo `.env`:

```env
HUGGINGFACE_API_KEY=hf_seu_token_aqui
```

---

## 🌐 Acessar Aplicação Online

A aplicação está hospedada e disponível no seguinte link:

👉 [https://autou-desenvolvimento-master.onrender.com/](https://autou-desenvolvimento-master.onrender.com/)

---

## 📌 Observações

- Por padrão, o Flask roda em modo de desenvolvimento. Para produção, recomenda-se o uso de servidores como **Gunicorn** ou **uWSGI**.
- As chaves de API devem ser mantidas privadas.