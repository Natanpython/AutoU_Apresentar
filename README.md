# 💼 Case Prático AutoU - Desenvolvimento

Seja bem-vindo(a) ao **Classificador Inteligente de Emails**!  
Essa é uma aplicação web desenvolvida por Natanael Pereira para teste de vaga na Autou Desenvolvimento.

Com apenas alguns cliques, ela identifica se um e-mail é **PRODUTIVO** (ou seja, realmente importante) e gera uma
**resposta educada e automática** com o apoio da inteligência artificial. Tudo isso em português!

---
 ## Deploy feito no Render
 ## acessar o Deploy = https://autou-desenvolvimento-master.onrender.com/

 ## Atenção!!!!
  para rodar o Projeto é necessario criar uma novo arquivo com o nome .env nele deve contar a chave TOKEN gerada pela huggingface, o motivo pelo qual não está aqui diretamente é que como é uma chave unica e precisa de segurança se o github estiver com o projeto como publico a huggingface desativa a chave na chave a baixo tem dois espaço retirar e inserir no arquivo .env que o projeto vai funcionar, ou pode gerar um novo token no site .
>>>chave usada atual = HUGGINGFACE_API_KEY= hf_FmAPKGYs XYKXzxtlhfSjNldhsOYmaovgGh

 🔐 Como corrigir (2 passos simples):
1. Crie um novo token com permissões corretas
Acesse: https://huggingface.co/settings/tokens

Clique em “New token”

Nome: api-classificador (ou outro qualquer)

Role até “Scope” e selecione:

✅ read

✅ inference

Clique em Create token

Copie o novo token (vai começar com hf_...)

2. Atualize a variável no Render
Vá para o Render > seu projeto > aba Environment

Encontre HUGGINGFACE_API_KEY

Clique no lápis para editar, e cole o novo token

Salve

 

## ✨ O que a aplicação faz?

- 📂 Recebe mensagens ou arquivos `.txt`/`.pdf`
- 🧠 Usa IA (modelo Mistral-7B-Instruct) para gerar respostas automáticas em **português**
- ✅ Classifica o conteúdo como **Produtivo** ou **Improdutivo** com base em critérios reais
- 🖥️ Exibe tudo em uma interface web com visual corporativo
- 🗑️ Permite excluir postagens individualmente

---

## 🧰 Tecnologias utilizadas

- **Python 3**  
- **Flask** (framework web leve e rápido)  
- **Hugging Face Inference API** (IA generativa com Mistral)  
- **HTML + CSS** para a interface  
- **PyPDF2** para leitura de PDFs

---

## 📁 Estrutura do projeto

Auto-_-Desenvolvimento/
├── static/ → Arquivos CSS (estilo)
├── templates/ → HTML principal
├── uploads/ → Onde os arquivos enviados ficam temporariamente
├── App.py → Código principal da aplicação
├── .env → Chave da API (não subir para o GitHub!)
└── README.md → Você está lendo ele agora 😄

---

📝 Como usar
Preencha seu nome e email.

Escreva a mensagem ou envie um arquivo .txt ou .pdf.

Clique em Classificar.

A IA irá analisar, classificar e sugerir uma resposta adequada.

Caso queira excluir, basta clicar no “X” vermelho da postagem.

🧠 Inteligência Artificial utilizada
Modelo: mistralai/Mistral-7B-Instruct-v0.2

API: Hugging Face Inference

Linguagem de saída: Português do Brasil 🇧🇷

🤝 Contribuição
Fique à vontade para sugerir melhorias, abrir issues ou fazer um fork do projeto. Toda colaboração é bem-vinda!

🧑‍💻 Autor
Desenvolvido com amor, café e código por [Seu Nome]
Você pode me encontrar no GitHub, LinkedIn ou por e-mail!

📄 Licença
Este projeto está sob a licença MIT — use, modifique e compartilhe à vontade.

---

## ⚙️ Como rodar na sua máquina?

### 1. Clone o repositório


git clone https://github.com/Natanpython/AutoU-_-Desenvolvimento
cd AutoU-_-Desenvolvimento

(Opcional) Crie um ambiente virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

---

## ⚙️  Instale as dependências

## pip install -r requirements.txt

##Executando o projeto
python App.py

Acesse no seu navegador:
http://127.0.0.1:5000/



