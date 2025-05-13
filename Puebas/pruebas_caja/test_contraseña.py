import unittest
from contraseña import validar_contraseña

class TestValidarContraseña(unittest.TestCase):

    def test_corta(self):
        self.assertEqual(validar_contraseña("hola"), "Contraseña demasiado corta")

    def test_sin_numero(self):
        self.assertEqual(validar_contraseña("Holamundo"), "Debe contener al menos un número")

    def test_sin_mayuscula(self):
        self.assertEqual(validar_contraseña("holamundo1"), "Debe contener al menos una mayúscula")

    def test_valida(self):
        self.assertEqual(validar_contraseña("Hola1234"), "Debe contener al menos un caracter especial (* # $ % & = _ . , ; :)")

    def test_exactamente_ocho(self):
        self.assertEqual(validar_contraseña("HOLA1234"), "Debe contener al menos un caracter especial (* # $ % & = _ . , ; :)")

    def test_solo_mayuscula_y_numero(self):
        self.assertEqual(validar_contraseña("HOLA123"), "Contraseña demasiado corta")

    def test_un_caracter_especial(self):
        self.assertEqual(validar_contraseña("HOLA123*"), "Contraseña válida")
    
    def test_longitud(self):
        self.assertEqual(validar_contraseña("HOLA123*123123123"), "La contraseña debe ser de máximo 14 caracteres~")

if __name__ == '__main__':
    unittest.main()
