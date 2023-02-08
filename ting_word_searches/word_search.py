from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    result = []

    for element in instance._data:  # para cada elem da fila
        ocorrencias = []

        # percorre as linhas do element em busca da palavra
        for index, line in enumerate(element['linhas_do_arquivo']):
            if word.lower() in line.lower():  # se tiver a palavra na linha
                # add a posição da linha em ocorrencias
                ocorrencias.append({"linha": index + 1})

        # se tiver ocorrencia no element, cria o obj e add em result
        if len(ocorrencias):
            obj = {
                "palavra": word,
                "arquivo": element['nome_do_arquivo'],
                "ocorrencias": ocorrencias
            }
            result.append(obj)

    return result


def search_by_word(word, instance: Queue):
    obj = exists_word(word, instance)
    for element in obj:
        element['ocorrencias']
    ...
