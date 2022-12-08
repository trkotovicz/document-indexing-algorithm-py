from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance: Queue):
    if path_file in str(instance._data):
        return ''

    text = txt_importer(path_file)

    result_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text),
        "linhas_do_arquivo": text
    }

    instance.enqueue(result_dict)
    print(result_dict)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
