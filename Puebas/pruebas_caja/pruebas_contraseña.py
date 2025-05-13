def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return "Contraseña demasiado corta"
    if not any(c.isdigit() for c in contraseña):
        return "Debe contener al menos un número"
    if not any(c.isupper() for c in contraseña):
        return "Debe contener al menos una mayúscula"
    return "Contraseña válida"

# Lista de casos de prueba: [(entrada, resultado_esperado)]
casos_prueba = [
    # Caja negra
    ("hola", "Contraseña demasiado corta"),
    ("holamundo", "Debe contener al menos un número"),
    ("holamundo1", "Debe contener al menos una mayúscula"),
    ("Hola1234", "Contraseña válida"),
    ("HOLA", "Contraseña demasiado corta"),
    
    # Caja blanca
    ("abcd1234", "Debe contener al menos una mayúscula"),  # sin mayúsculas
    ("ABCDabcd", "Debe contener al menos un número"),       # sin números
    ("A1b2c3d4", "Contraseña válida"),                      # cumple todo
    ("HOLA123", "Contraseña demasiado corta"),              # 7 caracteres
]

# Ejecutar pruebas
print("📋 Resultados de pruebas:\n")
for entrada, esperado in casos_prueba:
    resultado = validar_contraseña(entrada)
    estado = "✅" if resultado == esperado else "❌"
    print(f"{estado} Entrada: '{entrada}' | Esperado: '{esperado}' | Obtenido: '{resultado}'")
