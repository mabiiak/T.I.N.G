from ting_file_management.file_management import txt_importer 


def process(path_file, instance):
    texto = txt_importer(path_file)

    instance.enqueue(texto)

    formato = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(texto),
        "linhas_do_arquivo": instance._data[-1],
    }

    print(formato)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
