import os
import shutil

def create_folders_if_not_exist():
    folders = ['Im\u00e1genes', 'Documentos', 'Instaladores', 'Videos', 'M\u00fasica', 'PDF']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

def organize_downloads():
    create_folders_if_not_exist()
    downloads_dir = 'C:\\Users\\Oscar Alvarado\\Downloads'
    files = os.listdir(downloads_dir)
    for file in files:
        if os.path.isfile(os.path.join(downloads_dir, file)):
            file_extension = file.split('.')[-1]
            if file_extension.lower() in ['jpg', 'png', 'gif', 'jpeg']:
                shutil.move(os.path.join(downloads_dir, file), 'Im\u00e1genes')
            elif file_extension.lower() in ['doc', 'docx', 'txt', 'pdf']:
                shutil.move(os.path.join(downloads_dir, file), 'Documentos')
            elif file_extension.lower() in ['exe', 'msi']:
                shutil.move(os.path.join(downloads_dir, file), 'Instaladores')
            elif file_extension.lower() in ['mp4', 'avi', 'mov']:
                shutil.move(os.path.join(downloads_dir, file), 'Videos')
            elif file_extension.lower() in ['mp3', 'wav']:
                shutil.move(os.path.join(downloads_dir, file), 'M\u00fasica')
            elif file_extension.lower() == 'pdf':
                shutil.move(os.path.join(downloads_dir, file), 'PDF')

organize_downloads()
print('Archivos organizados exitosamente.')