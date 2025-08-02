import os
from glob import glob
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Pastas de entrada e saída
PASTA_INPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input')
PASTA_OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')

# Configuração do Chrome headless
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Encontra todos os arquivos .html na pasta de entrada
html_files = glob(os.path.join(PASTA_INPUT, '*.html'))

# Caminho do Chrome (ajuste se necessário)
chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

for html_path in html_files:
    nome_arquivo = Path(html_path).stem
    pdf_path = os.path.join(PASTA_OUTPUT, f'{nome_arquivo}.pdf')
    try:
        # Comando para converter HTML em PDF usando Chrome headless
        cmd = f'"{chrome_path}" --headless --disable-gpu --print-to-pdf="{pdf_path}" "file://{html_path}"'
        result = os.system(cmd)
        if result == 0:
            print(f'Convertido: {html_path} -> {pdf_path}')
        else:
            print(f'Erro ao converter {html_path}: código {result}')
    except Exception as e:
        print(f'Erro ao converter {html_path}: {e}')

print('Conversão concluída.')
