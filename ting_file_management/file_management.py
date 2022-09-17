from os.path import exists
import sys


def txt_importer(path_file):
    if '.txt' not in path_file:
        print(f"Formato inválido", file=sys.stderr)
        return None

    if not exists(path_file):
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return None

    with open(path_file, "r") as file:
        return file.read().split("\n")


# https://www.pythontutorial.net/python-basics/python-check-if-file-exists/
