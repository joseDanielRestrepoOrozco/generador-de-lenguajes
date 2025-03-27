def generar_gramatica(gramatica, simbolo = "S", max_profundidad = 5, profundidad = 0):
    vt, vn, p = gramatica

    if simbolo in vt:
        return {simbolo}

    if profundidad >= max_profundidad:
        return {""}

    if simbolo not in vn:
        raise ValueError("reglas de produccion incorrecta, simbolo: " + simbolo)

    resultados = set()

    for produccion in p[simbolo]:
        partes = produccion.split()
        cadenas_actuales = {""}

        for parte in partes:
            nuevas_cadenas = set()
            subcadenas = generar_gramatica(gramatica=gramatica, simbolo=parte, max_profundidad=max_profundidad, profundidad=profundidad + 1)

            for cadena in cadenas_actuales:
                for subcadena in subcadenas:
                    nuevas_cadenas.add(cadena + subcadena)

            cadenas_actuales = nuevas_cadenas

        resultados.update(cadenas_actuales)

    return resultados
