# Organizador de Arquivos por Tipo

Este projeto é um bot simples em Python que organiza os arquivos da pasta `Downloads` em subpastas de acordo com seu tipo (extensão de arquivo). O script move arquivos como PDFs, imagens, documentos do Word, planilhas e outros para pastas correspondentes, mantendo sua pasta `Downloads` organizada.

## Funcionalidades
- Move arquivos para pastas de acordo com suas extensões, como `pdf`, `jpg`, `png`, `docx`, etc.
- Cria pastas automaticamente, se necessário.
- Extensões de arquivos configuráveis (pode ser modificado no código).
  
## Requisitos

Certifique-se de que o Python 3 está instalado no seu sistema. Você pode verificar isso executando o seguinte comando no terminal:

``
python3 --version``
Se você não tiver o Python instalado, você pode baixá-lo [aqui](https://www.python.org/downloads/).

## Como Executar

1.  **Clone ou baixe este repositório** para o seu computador:
	```git clone https://github.com/W3ndell-S04/bot_python.git```
Ou faça o download do arquivo `.zip` e extraia os arquivos em uma pasta.

2.  **Navegue até o diretório do projeto** no terminal:
	```cd diretorio-do-projeto```
	
3.  **Execute o script Python** para organizar seus arquivos na pasta `Downloads`:

**No Windows:**
``python script.py``

**No Linux ou macOS:**
``python3 script.py``

**Nota**: O script irá acessar automaticamente a pasta `Downloads` do usuário atual e organizar os arquivos nela.
## Personalização

Se você quiser adicionar mais extensões ou alterar os tipos de arquivos, você pode modificar o dicionário `file_types` no arquivo `script.py`. Por exemplo:

    ``file_types = {
        "pdf": "pdf",
        "jpg": "imagens",
        "png": "imagens",
        "docx": "documentos",
        "xls": "planilhas",
        "mp4": "vídeos",
        "mp3": "áudios",
        # Adicione mais extensões conforme necessário
    }
    ``
