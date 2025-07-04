from flask import Flask, render_template, request, redirect, url_for;
from huggingface_hub import InferenceClient;
from dotenv import load_dotenv;
import os;
import PyPDF2;

load_dotenv();
api_key = os.getenv("HUGGINGFACE_API_KEY");

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=api_key,
    timeout=60
);

app = Flask(__name__);
UPLOAD_FOLDER = 'uploads';
os.makedirs(UPLOAD_FOLDER, exist_ok=True);
postagens = [];

def gerar_resposta(prompt):
    try:
        completion = client.chat.completions.create(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        print("Erro ao chamar API:", e)
        return "Erro ao gerar resposta."

@app.route('/', methods=['GET', 'POST'])
def index():
    global postagens

    if request.method == 'POST':
        nome = request.form.get('nome', '')
        email = request.form.get('email', '')
        mensagem = request.form.get('mensagem', '')

        arquivo = request.files.get('arquivo')
        if arquivo and arquivo.filename != '':
            caminho = os.path.join(UPLOAD_FOLDER, arquivo.filename)
            arquivo.save(caminho)
            if caminho.endswith('.txt'):
                with open(caminho, 'r', encoding='utf-8') as f:
                    mensagem = f.read()
            elif caminho.endswith('.pdf'):
                with open(caminho, 'rb') as f:
                    reader = PyPDF2.PdfReader(f)
                    mensagem = ''
                    for page in reader.pages:
                        mensagem += page.extract_text()

        prompt_resp = f"Responda de forma educada, curta e objetiva em português do Brasil ao seguinte email:\n\n{mensagem}"
        resposta = gerar_resposta(prompt_resp)

        if any(palavra in mensagem.lower() for palavra in ["reunião","reuniao","ajuda", "financeiro", "pagamento", "contrato", "urgente", "pedido", "orçamento", "venda", "cliente", "proposta", "serviço", "reclamação", "atendimento"]):
            categoria = "Produtivo"
        else:
            categoria = "Improdutivo"

        postagens.append({
            'id': len(postagens),
            'nome': nome,
            'email': email,
            'mensagem': mensagem,
            'categoria': categoria,
            'resposta': resposta
        })

        return redirect(url_for('index'))

    return render_template('index.html', postagens=postagens)

@app.route('/excluir/<int:id>')
def excluir(id):
    global postagens
    postagens = [p for p in postagens if p['id'] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))