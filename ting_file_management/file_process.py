import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return None

    texto = txt_importer(path_file)

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(texto),
        "linhas_do_arquivo": texto,
    }

    instance.enqueue(data)

    sys.stdout.write(str(data))


def remove(instance):
    tamanho = instance.__len__()

    if tamanho == 0:
        sys.stdout.write(str("Não há elementos\n"))
    else:
        remove = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(str(f"Arquivo {remove} removido com sucesso\n"))


def file_metadata(instance, position):
    tamanho = instance.__len__()

    if position > tamanho or position < 0:
        print("Posição inválida", file=sys.stderr)
    else:
        item = instance.search(position)
        sys.stdout.write(str(item))
