import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        sys.stderr.write('Formato inválido\n')

    try:
        with open(path_file, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

# https://www.delftstack.com/pt/howto/python/python-print-to-stderr/#utilize-o-sysstderr-para-imprimir-para-o-stderr
