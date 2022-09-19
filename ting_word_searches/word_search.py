def exists_word(word, instance):
    data = instance._data

    result = []
    ocorrencias = []

    for i, palavra in enumerate(data[0]["linhas_do_arquivo"]):
        if word.lower() in palavra.lower():
            ocorrencias.append({ "linha": i + 1 })

    if len(ocorrencias) != 0:
        result.append({
            "palavra": word,
            "arquivo": data[0]["nome_do_arquivo"],
            "ocorrencias": ocorrencias
        })
    
    return result


def search_by_word(word, instance):
    data = instance._data

    result = []
    ocorrencias = []

    for i, palavra in enumerate(data[0]["linhas_do_arquivo"]):
        if word.lower() in palavra.lower():
            ocorrencias.append({ "linha": i + 1, "conteudo": palavra })

    if len(ocorrencias) != 0:
        result.append({
            "palavra": word,
            "arquivo": data[0]["nome_do_arquivo"],
            "ocorrencias": ocorrencias
        })
    
    return result
