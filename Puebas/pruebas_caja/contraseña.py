def validar_contraseña(contraseña):
    """
    Valida la fortaleza de una contraseña según los siguientes criterios:

    - Debe tener al menos 8 caracteres.
    - Debe contener al menos un número.
    - Debe contener al menos una letra mayúscula.
    - Debe contener al menos un carácter especial de la lista: * # $ % & = _ . , ; :
    - No debe exceder los 14 caracteres.

    Parámetros:
        contraseña (str): La contraseña a validar.

    Retorna:
        str: Un mensaje indicando si la contraseña es válida o la razón por la que no lo es.
    """
    if len(contraseña) < 8:
        return "Contraseña demasiado corta"
    if not any(c.isdigit() for c in contraseña):
        return "Debe contener al menos un número"
    if not any(c.isupper() for c in contraseña):
        return "Debe contener al menos una mayúscula"
    if not any(c in "*#$%&=_.,;:" for c in contraseña):
        return "Debe contener al menos un caracter especial (* # $ % & = _ . , ; :)"
    if len(contraseña) > 14:
        return "La contraseña debe ser de máximo 14 caracteres~"
    return "Contraseña válida"

