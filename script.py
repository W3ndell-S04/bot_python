import os
import shutil

# Função para organizar os arquivos em uma pasta
def organize_files_by_type(folder_path):
    # Verifica se o diretório existe
    if not os.path.exists(folder_path):
        print(f"O diretório {folder_path} não foi encontrado.")
        return

    # Mapeamento de extensões de arquivos para pastas
    file_types = {
        "pdf": "pdf",
        "jpg": "imagens",
        "jpeg": "imagens",
        "png": "imagens",
        "doc": "documentos",
        "docx": "documentos",
        "xls": "planilhas",
        "xlsx": "planilhas",
        "ppt": "apresentações",
        "pptx": "apresentações",
        "mp4": "vídeos",
        "mp3": "áudios",
        # Adicione mais extensões conforme necessário
    }

    # Percorre todos os arquivos na pasta
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Ignora se for uma pasta
        if os.path.isdir(file_path):
            continue

        # Obtém a extensão do arquivo (sem o ponto inicial)
        file_extension = filename.split('.')[-1].lower()

        # Verifica se a extensão está no dicionário de tipos de arquivos
        if file_extension in file_types:
            # Cria a pasta de destino, se ainda não existir
            destination_folder = os.path.join(folder_path, file_types[file_extension])
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Move o arquivo para a pasta correta
            shutil.move(file_path, os.path.join(destination_folder, filename))
            print(f'Movido: {filename} -> {destination_folder}')
        else:
            print(f"Extensão não reconhecida: {filename}")

# Diretório de Downloads
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
# Diretório de Documentos
documents_folder = os.path.join(os.path.expanduser("~"), "Documents")

# Organiza os arquivos em ambos os diretórios
print("Organizando a pasta Downloads...")
organize_files_by_type(downloads_folder)

print("Organizando a pasta Documentos...")
organize_files_by_type(documents_folder)

