from zipfile import ZipFile

zip_file = 'assign.zip'
file_name = 'links.txt'

with ZipFile(zip_file, 'w') as z:
    z.write(file_name)