def generar_gramatica(gramatica, simbolo = "S", max_profundidad = 5, profundidad = 0):
    vt, vn, p = gramatica

    if profundidad > max_profundidad:
        return set()

    if simbolo in vt:
        return {simbolo}

    if simbolo not in vn:
        raise ValueError("reglas de produccion incorrecta, simbolo: " + simbolo)

    resultados = set()

    for produccion in p[simbolo]:
        partes = produccion.split()
        cadenas_actuales = {""}

        for parte in partes:
            nuevas_cadenas = set()
            subcadenas = generar_gramatica(gramatica, parte, max_profundidad, profundidad + 1)

            for cadena in cadenas_actuales:
                for subcadena in subcadenas:
                    nuevas_cadenas.add(cadena + subcadena)

            cadenas_actuales = nuevas_cadenas

        resultados.update(cadenas_actuales)

    return resultados

vt = {"a", "b"}
vn = {"S", "A"}

p = {
    "S": ["a S b", "A"],
    "A": ["a A", "b"]
}

gramatica = (vt, vn, p)

# Generar todas las cadenas posibles con un límite de profundidad
max_profundidad = 5

try:
    cadenas = generar_gramatica(gramatica)
    print("Cadenas generadas:")
    for cadena in sorted(cadenas):
        print(cadena)
except ValueError as e:
    print(f'Error: {e}')
