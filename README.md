# htmltopdf

Ferramenta para converter arquivos HTML em PDF em lote usando Google Chrome headless.

## Estrutura de Pastas
- `input/`: coloque aqui todos os arquivos `.html` que deseja converter.
- `output/`: os arquivos PDF convertidos serão salvos aqui.

## Como usar
1. Certifique-se de ter o Google Chrome instalado no macOS.
2. Coloque os arquivos HTML na pasta `input`.
3. Execute o script:
   ```sh
   python converter_html_para_pdf_selenium.py
   ```
   Os PDFs serão gerados na pasta `output`.

## Requisitos
- Python 3.8+
- Google Chrome
- (Opcional) Ambiente virtual Python
- Pacote `selenium` (instalado via `pip install selenium`)

## Observações
- O script usa o Chrome via linha de comando para conversão, não depende de bibliotecas externas problemáticas.
- Ajuste o caminho do Chrome no script se necessário.

## Licença
MIT
