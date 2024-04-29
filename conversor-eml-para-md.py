import os
import logging
from email import policy
from email.parser import BytesParser
from markdownify import markdownify as md

# Configurar o logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def converterEmlParaMd(caminhoFonte, pastaDestino):
    try:
        # Tentar abrir e ler o arquivo .eml
        with open(caminhoFonte, 'rb') as arquivo:
            email = BytesParser(policy=policy.default).parse(arquivo)
    except Exception as e:
        logging.error(f"Não foi possível ler o arquivo {caminhoFonte}: {e}")
        return None

    try:
        # Extrair o conteúdo e a data
        conteudo = email.get_body(preferencelist=('html')).get_content()
        data = email['date']
        dataFormatada = email.get('date').datetime.strftime('%Y-%m-%d - %H:%M')

        # Converter HTML para Markdown
        conteudoMarkdown = f"Dia e hora do envio do e-mail: {dataFormatada}\n\n" + md(conteudo)
        
        # Definir novo nome de arquivo e caminho
        nomeArquivo = os.path.splitext(os.path.basename(caminhoFonte))[0] + '.md'
        novoCaminho = os.path.join(pastaDestino, nomeArquivo)

        # Salvar o arquivo Markdown
        with open(novoCaminho, 'w') as arquivoMd:
            arquivoMd.write(conteudoMarkdown)
        logging.info(f"Arquivo {nomeArquivo} convertido e salvo com sucesso em {novoCaminho}")
    except Exception as e:
        logging.error(f"Erro ao processar o arquivo {caminhoFonte}: {e}")
        return None
    
    return novoCaminho

def converterPastaEmlParaMd(caminhoPasta, pastaDestino):
    # Verificar e listar todos os arquivos .eml na pasta
    arquivosEml = [arq for arq in os.listdir(caminhoPasta) if arq.endswith('.eml')]
    if not arquivosEml:
        logging.warning("Nenhum arquivo .eml encontrado na pasta de origem.")
        return
    
    for arquivo in arquivosEml:
        caminhoArquivoFonte = os.path.join(caminhoPasta, arquivo)
        resultado = converterEmlParaMd(caminhoArquivoFonte, pastaDestino)
        if resultado:
            logging.info(f"Convertido {arquivo} para Markdown e salvo em {resultado}")

# Exemplo de uso:
caminhoPastaFonte = '<INCLUIR PASTA AQUI>'  # Pasta contendo os arquivos .eml
pastaDestino = '<INCLUIR PASTA AQUI>'  # Pasta onde você deseja salvar os arquivos .md
converterPastaEmlParaMd(caminhoPastaFonte, pastaDestino)
