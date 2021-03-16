"""
 * Universidad de Los Andes
 * ISIS 1221 - Introducción a la Programación
 * Proyecto de nivel 2
 * 10 de Marzo de 2021
 *
 * @author Juan Lugo Sánchez
 * jd.lugo@uniandes.edu.co
 * 201913094
"""

import unittest
import analizador_sangre as mod

test = 0


class TestAnalizador(unittest.TestCase):

    def test_crear_paciente(self):
        print()
        print("################### Test crear_paciente ############################################")
        global test
        examen1_funcion = mod.crear_paciente(1, "M", 20, 88, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 0)
        examen1 = {"id": 1, "genero": "M", "edad": 20, "PPM": 88, "Hb": 20, "CGB": 11.5, "glicemia": 280,
                   "LDL": 89.7, "HDL": 50, "trigliceridos": 120.8, "CT": 240, "CL": 7.9, "CP": 150, "tiempo": 25,
                   "GCH": 0}
        print("Verificando la creacion de un paciente ------------------------------------ ❌", end='')
        self.assertEqual(examen1, examen1_funcion,
                         "El diccionario creado no corresponde con los valores dados por parametro; "
                         "revisar los elementos que tienen + y - para determinar que valores son diferentes")
        print("\rVerificando la creacion de un paciente ------------------------------------ ✅")
        test += 1

    def test_buscar_examen(self):
        print()
        print("################### Test buscar_examen #############################################")
        global test
        examen1 = mod.crear_paciente(11, "M", 20, 88, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 0)
        examen2 = mod.crear_paciente(26, "F", 30, 90, 9, 10.5, 69, 98.3, 60, 100.9, 225, 9.8, 141, 35, 10)
        examen3 = mod.crear_paciente(3, "F", 69, 70, 15, 12.5, 115, 138.6, 40, 150.3, 260, 8.2, 160, 15, 2)
        examen4 = mod.crear_paciente(42, "M", 33, 60, 10, 9.9, 65, 102.5, 55, 120.8, 236, 10.6, 167, 43, 0)

        encontrado1 = mod.buscar_examen(11, examen1, examen2, examen3, examen4)

        print("Verificando la busqueda de un paciente existente -------------------------- ❌", end='')
        self.assertEqual(examen1, encontrado1, "La funcion no encontró el examen buscado")
        print("\rVerificando la busqueda de un paciente existente -------------------------- ✅")
        test += 1

        encontrado2 = mod.buscar_examen(5, examen1, examen2, examen3, examen4)

        print("Verificando la busqueda de un paciente NO existente ----------------------- ❌", end='')
        self.assertIsNone(encontrado2, "La funcion encontró un examen que no existe")
        print("\rVerificando la busqueda de un paciente NO existente ----------------------- ✅")
        test += 1

    def test_confirmar_embarazo(self):
        global test
        print()
        print("################### Test confirmar_embarazo ########################################")
        examen1 = mod.crear_paciente(11, "F", 20, 88, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen2 = mod.crear_paciente(26, "M", 30, 90, 9, 10.5, 69, 98.3, 60, 100.9, 225, 9.8, 141, 35, 10)
        examen3 = mod.crear_paciente(3, "F", 69, 70, 15, 12.5, 115, 138.6, 40, 150.3, 260, 8.2, 160, 15, 9)

        no_embarazo = mod.confirmar_embarazo(examen1)
        test_masculino = mod.confirmar_embarazo(examen2)
        embarazo = mod.confirmar_embarazo(examen3)

        print("Verificando prueba de embarazo negativa ----------------------------------- ❌", end='')
        self.assertFalse(no_embarazo, "El método no determinó que la paciente NO estaba embarazada.")
        print("\rVerificando prueba de embarazo negativa ----------------------------------- ✅")
        test += 1

        print("Verificando prueba de embarazo en un paciente masculino ------------------- ❌", end='')
        self.assertFalse(test_masculino, "El método le realizo una prueba de embarazo a un paciente masculino.")
        print("\rVerificando prueba de embarazo en un paciente masculino ------------------- ✅")
        test += 1

        print("Verificando prueba de embarazo positiva ------------------------------------❌", end='')
        self.assertTrue(embarazo, "El método no determinó que la paciente estaba embarazada.")
        print("\rVerificando prueba de embarazo positiva ----------------------------------- ✅")
        test += 1

    def test_validar_pulsaciones(self):
        global test
        print()
        print("################### Test validar_pulsaciones #######################################")

        examen1B = mod.crear_paciente(1, "M", 20, 60, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen1N = mod.crear_paciente(1, "M", 20, 75, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen1T = mod.crear_paciente(2, "M", 20, 86, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)

        print("Verificando bradicardia en paciente masculino de 20 años ------------------ ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen1B), "bradicardia",
                         "El método no determinó que el paciente tenía bradicardia.")
        print("\rVerificando bradicardia en paciente masculino de 20 años ------------------ ✅")
        test += 1

        print("Verificando estado normal en paciente masculino de 20 años ---------------- ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen1N), "normalidad",
                         "El método no determinó que el paciente no tenía PPM irregulares.")
        print("\rVerificando estado normal en paciente masculino de 20 años ---------------- ✅")
        test += 1

        print("Verificando taquicardia en paciente masculino de 20 años ------------------ ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen1T), "taquicardia",
                         "El método no determinó que el paciente tenía taquicardia.")
        print("\rVerificando taquicardia en paciente masculino de 20 años ------------------ ✅")
        test += 1
        print()

        examen2B = mod.crear_paciente(3, "M", 30, 62, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen2N = mod.crear_paciente(1, "M", 30, 75, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen2T = mod.crear_paciente(4, "M", 30, 86, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)

        print("Verificando bradicardia en paciente masculino de 30 años ------------------ ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen2B), "bradicardia",
                         "El método no determinó que el paciente tenía bradicardia.")
        print("\rVerificando bradicardia en paciente masculino de 30 años ------------------ ✅")
        test += 1

        print("Verificando estado normal en paciente masculino de 30 años ---------------- ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen2N), "normalidad",
                         "El método no determinó que el paciente no tenía PPM irregulares.")
        print("\rVerificando estado normal en paciente masculino de 30 años ---------------- ✅")
        test += 1

        print("Verificando taquicardia en paciente masculino de 30 años ------------------ ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen2T), "taquicardia",
                         "El método no determinó que el paciente tenía taquicardia.")
        print("\rVerificando taquicardia en paciente masculino de 30 años ------------------ ✅")
        test += 1
        print()

        examen3B = mod.crear_paciente(5, "M", 40, 64, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen3N = mod.crear_paciente(1, "M", 40, 75, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen3T = mod.crear_paciente(6, "M", 40, 90, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)

        print("Verificando bradicardia en paciente masculino de 40 años ------------------ ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen3B), "bradicardia",
                         "El método no determinó que el paciente tenía bradicardia.")
        print("\rVerificando bradicardia en paciente masculino de 40 años ------------------ ✅")
        test += 1

        print("Verificando estado normal en paciente masculino de 40 años ---------------- ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen3N), "normalidad",
                         "El método no determinó que el paciente no tenía PPM irregulares.")
        print("\rVerificando estado normal en paciente masculino de 40 años ---------------- ✅")
        test += 1

        print("Verificando taquicardia en paciente masculino de 40 años ------------------ ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen3T), "taquicardia",
                         "El método no determinó que el paciente tenía taquicardia.")
        print("\rVerificando taquicardia en paciente masculino de 40 años ------------------ ✅")
        test += 1
        print()

        examen4B = mod.crear_paciente(7, "M", 50, 66, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen4N = mod.crear_paciente(1, "M", 50, 75, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen4T = mod.crear_paciente(8, "M", 50, 90, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)

        print("Verificando bradicardia en paciente masculino de 50 años ------------------ ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen4B), "bradicardia",
                         "El método no determinó que el paciente tenía bradicardia.")
        print("\rVerificando bradicardia en paciente masculino de 50 años ------------------ ✅")
        test += 1

        print("Verificando estado normal en paciente masculino de 50 años ---------------- ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen4N), "normalidad",
                         "El método no determinó que el paciente no tenía PPM irregulares.")
        print("\rVerificando estado normal en paciente masculino de 50 años ---------------- ✅")
        test += 1

        print("Verificando taquicardia en paciente masculino de 50 años ------------------ ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen4T), "taquicardia",
                         "El método no determinó que el paciente tenía taquicardia.")
        print("\rVerificando taquicardia en paciente masculino de 50 años ------------------ ✅")
        test += 1
        print()
        print("#")
        print()

        examen5B = mod.crear_paciente(1, "F", 20, 70, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen5N = mod.crear_paciente(1, "F", 20, 75, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen5T = mod.crear_paciente(2, "F", 20, 96, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)

        print("Verificando bradicardia en paciente femenino de 20 años ------------------- ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen5B), "bradicardia",
                         "El método no determinó que el paciente tenía bradicardia.")
        print("\rVerificando bradicardia en paciente femenino de 20 años ------------------- ✅")
        test += 1

        print("Verificando estado normal en paciente femenino de 20 años ----------------- ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen5N), "normalidad",
                         "El método no determinó que el paciente no tenía PPM irregulares.")
        print("\rVerificando estado normal en paciente femenino de 20 años ----------------- ✅")
        test += 1

        print("Verificando taquicardia en paciente femenino de 20 años ------------------- ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen5T), "taquicardia",
                         "El método no determinó que el paciente tenía taquicardia.")
        print("\rVerificando taquicardia en paciente femenino de 20 años ------------------- ✅")
        test += 1
        print()

        examen6B = mod.crear_paciente(3, "F", 30, 70, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen6N = mod.crear_paciente(1, "F", 30, 75, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen6T = mod.crear_paciente(4, "F", 30, 98, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)

        print("Verificando bradicardia en paciente femenino de 30 años ------------------- ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen6B), "bradicardia",
                         "El método no determinó que el paciente tenía bradicardia.")
        print("\rVerificando bradicardia en paciente femenino de 30 años ------------------- ✅")
        test += 1

        print("Verificando estado normal en paciente femenino de 30 años ----------------- ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen6N), "normalidad",
                         "El método no determinó que el paciente no tenía PPM irregulares.")
        print("\rVerificando estado normal en paciente femenino de 30 años ----------------- ✅")
        test += 1

        print("Verificando taquicardia en paciente femenino de 30 años ------------------- ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen6T), "taquicardia",
                         "El método no determinó que el paciente tenía taquicardia.")
        print("\rVerificando taquicardia en paciente femenino de 30 años ------------------- ✅")
        test += 1
        print()

        examen7B = mod.crear_paciente(5, "F", 40, 72, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen7N = mod.crear_paciente(1, "F", 40, 75, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen7T = mod.crear_paciente(6, "F", 40, 100, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)

        print("Verificando bradicardia en paciente femenino de 40 años ------------------- ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen7B), "bradicardia",
                         "El método no determinó que el paciente tenía bradicardia.")
        print("\rVerificando bradicardia en paciente femenino de 40 años ------------------- ✅")
        test += 1

        print("Verificando estado normal en paciente femenino de 40 años ----------------- ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen7N), "normalidad",
                         "El método no determinó que el paciente no tenía PPM irregulares.")
        print("\rVerificando estado normal en paciente femenino de 40 años ----------------- ✅")
        test += 1

        print("Verificando taquicardia en paciente femenino de 40 años ------------------- ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen7T), "taquicardia",
                         "El método no determinó que el paciente tenía taquicardia.")
        print("\rVerificando taquicardia en paciente femenino de 40 años ------------------- ✅")
        test += 1
        print()

        examen8B = mod.crear_paciente(7, "F", 50, 72, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen8N = mod.crear_paciente(1, "F", 50, 75, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen8T = mod.crear_paciente(8, "F", 50, 104, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)

        print("Verificando bradicardia en paciente femenino de 50 años ------------------- ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen8B), "bradicardia",
                         "El método no determinó que el paciente tenía bradicardia.")
        print("\rVerificando bradicardia en paciente femenino de 50 años ------------------- ✅")
        test += 1

        print("Verificando estado normal en paciente femenino de 50 años ----------------- ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen8N), "normalidad",
                         "El método no determinó que el paciente no tenía PPM irregulares.")
        print("\rVerificando estado normal en paciente femenino de 50 años ----------------- ✅")
        test += 1

        print("Verificando taquicardia en paciente femenino de 50 años ------------------- ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen8T), "taquicardia",
                         "El método no determinó que el paciente tenía taquicardia.")
        print("\rVerificando taquicardia en paciente femenino de 50 años ------------------- ✅")
        test += 1
        print()
        print("#")
        print()

        examen01 = mod.crear_paciente(7, "F", 11, 50, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen02 = mod.crear_paciente(7, "F", 6, 75, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen03 = mod.crear_paciente(7, "F", 18, 105, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen04 = mod.crear_paciente(1, "M", 9, 50, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen05 = mod.crear_paciente(7, "M", 15, 75, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen06 = mod.crear_paciente(8, "M", 19, 105, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)

        print("Verificando estado normal en paciente femenino fuera de rango 50 PPM ------ ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen01), "normalidad",
                         "El método no determinó que el paciente está fuera de rango.")
        print("\rVerificando estado normal en paciente femenino fuera de rango 50 PPM ------ ✅")
        test += 1

        print("Verificando estado normal en paciente femenino fuera de rango 75 PPM ------ ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen02), "normalidad",
                         "El método no determinó que el paciente está fuera de rango.")
        print("\rVerificando estado normal en paciente femenino fuera de rango 75 PPM ------ ✅")
        test += 1

        print("Verificando estado normal en paciente femenino fuera de rango 105 PPM ----- ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen03), "normalidad",
                         "El método no determinó que el paciente está fuera de rango.")
        print("\rVerificando estado normal en paciente femenino fuera de rango 105 PPM ----- ✅")
        test += 1

        print("Verificando estado normal en paciente masculino fuera de rango 50 PPM ----- ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen04), "normalidad",
                         "El método no determinó que el paciente está fuera de rango.")
        print("\rVerificando estado normal en paciente masculino fuera de rango 50 PPM ----- ✅")
        test += 1

        print("Verificando estado normal en paciente masculino fuera de rango 75 PPM ----- ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen05), "normalidad",
                         "El método no determinó que el paciente está fuera de rango.")
        print("\rVerificando estado normal en paciente masculino fuera de rango 75 PPM ----- ✅")
        test += 1

        print("Verificando estado normal en paciente masculino fuera de rango 105 PPM ---- ❌", end='')
        self.assertEqual(mod.validar_pulsaciones(examen06), "normalidad",
                         "El método no determinó que el paciente está fuera de rango.")
        print("\rVerificando estado normal en paciente masculino fuera de rango 105 PPM ---- ✅")
        test += 1

    def test_confirmar_anemia(self):
        global test
        print()
        print("################### Test confirmar_anemia ##########################################")

        examen1A = mod.crear_paciente(4, "F", 4, 50, 10, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen1N = mod.crear_paciente(4, "M", 4, 50, 13, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)

        print("Verificando el paciente de 04 años con nivel Hb 10 de positivo ------------ ❌", end='')
        self.assertTrue(mod.confirmar_anemia(examen1A),
                        "El método no determina correctamente que el paciente tiene anemia.")
        print("\rVerificando el paciente de 04 años con nivel Hb 10 de positivo ------------ ✅")
        test += 1

        print("Verificando el paciente de 04 años con nivel Hb 13 de negativo ------------ ❌", end='')
        self.assertFalse(mod.confirmar_anemia(examen1N),
                         "El método no determina correctamente que el paciente NO tiene anemia.")
        print("\rVerificando el paciente de 04 años con nivel Hb 13 de negativo ------------ ✅")
        test += 1

        examen2A = mod.crear_paciente(11, "M", 11, 75, 10, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen2N = mod.crear_paciente(11, "F", 11, 75, 13, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)

        print("Verificando el paciente de 11 años con nivel Hb 11 de positivo ------------ ❌", end='')
        self.assertTrue(mod.confirmar_anemia(examen2A),
                        "El método no determina correctamente que el paciente tiene anemia.")
        print("\rVerificando el paciente de 11 años con nivel Hb 11 de positivo ------------ ✅")
        test += 1

        print("Verificando el paciente de 11 años con nivel Hb 13 de negativo ------------ ❌", end='')
        self.assertFalse(mod.confirmar_anemia(examen2N),
                         "El método no determina correctamente que el paciente NO tiene anemia.")
        print("\rVerificando el paciente de 11 años con nivel Hb 13 de negativo ------------ ✅")
        test += 1

        examen3A = mod.crear_paciente(15, "F", 15, 105, 11, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen3N = mod.crear_paciente(15, "M", 15, 105, 13, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)

        print("Verificando el paciente de 15 años con nivel Hb 11 de positivo ------------ ❌", end='')
        self.assertTrue(mod.confirmar_anemia(examen3A),
                        "El método no determina correctamente que el paciente tiene anemia.")
        print("\rVerificando el paciente de 15 años con nivel Hb 11 de positivo ------------ ✅")
        test += 1

        print("Verificando el paciente de 15 años con nivel Hb 13 de negativo ------------ ❌", end='')
        self.assertFalse(mod.confirmar_anemia(examen3N),
                         "El método no determina correctamente que el paciente NO tiene anemia.")
        print("\rVerificando el paciente de 15 años con nivel Hb 13 de negativo ------------ ✅")
        test += 1

        examen4A = mod.crear_paciente(20, "F", 20, 50, 10, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 10)
        examen4N = mod.crear_paciente(20, "F", 20, 50, 12, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 10)

        print("Verificando la paciente en embarazo de 20 años con nivel Hb 10 de positivo  ❌", end='')
        self.assertTrue(mod.confirmar_anemia(examen4A),
                        "El método no determina correctamente que el paciente tiene anemia.")
        print("\rVerificando la paciente en embarazo de 20 años con nivel Hb 10 de positivo  ✅")
        test += 1

        print("Verificando la paciente en embarazo de 20 años con nivel Hb 12 de negativo  ❌", end='')
        self.assertFalse(mod.confirmar_anemia(examen4N),
                         "El método no determina correctamente que el paciente NO tiene anemia.")
        print("\rVerificando la paciente en embarazo de 20 años con nivel Hb 12 de negativo  ✅")
        test += 1

        examen5A = mod.crear_paciente(20, "F", 20, 75, 11, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 7)
        examen5N = mod.crear_paciente(20, "F", 20, 75, 13, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 7)

        print("Verificando la paciente de 20 años con nivel Hb 11 de positivo ------------ ❌", end='')
        self.assertTrue(mod.confirmar_anemia(examen5A),
                        "El método no determina correctamente que el paciente tiene anemia.")
        print("\rVerificando la paciente de 20 años con nivel Hb 11 de positivo ------------ ✅")
        test += 1

        print("Verificando la paciente de 20 años con nivel Hb 13 de negativo ------------ ❌", end='')
        self.assertFalse(mod.confirmar_anemia(examen5N),
                         "El método no determina correctamente que el paciente NO tiene anemia.")
        print("\rVerificando la paciente de 20 años con nivel Hb 13 de negativo ------------ ✅")
        test += 1

        examen6A = mod.crear_paciente(20, "M", 20, 105, 12, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        examen6N = mod.crear_paciente(20, "M", 20, 105, 14, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)

        print("Verificando el paciente de 20 años con nivel Hb 12 de positivo ------------ ❌", end='')
        self.assertTrue(mod.confirmar_anemia(examen6A),
                        "El método no determina correctamente que el paciente tiene anemia.")
        print("\rVerificando el paciente de 20 años con nivel Hb 12 de positivo ------------ ✅")
        test += 1

        print("Verificando el paciente de 20 años con nivel Hb 14 de negativo ------------ ❌", end='')
        self.assertFalse(mod.confirmar_anemia(examen6N),
                         "El método no determina correctamente que el paciente NO tiene anemia.")
        print("\rVerificando el paciente de 20 años con nivel Hb 14 de negativo ------------ ✅")
        test += 1

    def test_contar_hipoglicemicos(self):
        global test
        print()
        print("################### Test confirmar_anemia ##########################################")

        e1 = mod.crear_paciente(7, "F", 11, 50, 20, 11.5, 50, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        e2 = mod.crear_paciente(7, "F", 6, 75, 20, 11.5, 20, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        e3 = mod.crear_paciente(7, "F", 18, 105, 20, 11.5, 69, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        e4 = mod.crear_paciente(1, "M", 9, 50, 20, 11.5, 70, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        e5 = mod.crear_paciente(7, "M", 15, 75, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        e6 = mod.crear_paciente(8, "M", 19, 105, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)

        print("Verificando el calculo correcto de 3 pacientes hipoglicemicos ------------- ❌", end='')
        self.assertEqual(mod.contar_hipoglicemicos(e1, e2, e3, e4), 3,
                         "El método no determinó correctamente el numero de pacientes hipoglicemicos.")
        print("\rVerificando el calculo correcto de 3 pacientes hipoglicemicos ------------- ✅")
        test += 1

        print("Verificando el calculo correcto de 1 paciente hipoglicemico --------------- ❌", end='')
        self.assertEqual(mod.contar_hipoglicemicos(e6, e5, e3, e4), 1,
                         "El método no determinó correctamente el numero de pacientes hipoglicemicos.")
        print("\rVerificando el calculo correcto de 1 paciente hipoglicemico --------------- ✅")
        test += 1

        print("Verificando el calculo correcto de 2 pacientes hipoglicemicos ------------- ❌", end='')
        self.assertEqual(mod.contar_hipoglicemicos(e1, e2, e5, e6), 2,
                         "El método no determinó correctamente el numero de pacientes hipoglicemicos.")
        print("\rVerificando el calculo correcto de 2 pacientes hipoglicemicos ------------- ✅")
        test += 1

    def test_validar_infecciones(self):
        global test
        print()
        print("################### Test validar_infecciones #######################################")

        e1 = mod.crear_paciente(1, "F", 11, 50, 20, 11.5, 50, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        e2 = mod.crear_paciente(2, "F", 6, 75, 20, 12.5, 20, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        e3 = mod.crear_paciente(3, "F", 18, 105, 20, 11.1, 69, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        e4 = mod.crear_paciente(4, "M", 9, 50, 20, 5.5, 70, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        e5 = mod.crear_paciente(5, "M", 15, 75, 20, 4.6, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        e6 = mod.crear_paciente(6, "M", 19, 105, 20, 1.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)

        print("Verificando la valoracion correcta de 3 pacientes en riesgo --------------- ❌", end='')
        self.assertEqual(mod.validar_infecciones(e1, e2, e3, e4), "1,2,3",
                         "El método no determinó correctamente los pacientes con riesgo de infeccion.")
        print("\rVerificando la valoracion correcta de 3 pacientes en riesgo --------------- ✅")
        test += 1

        print("Verificando la valoracion correcta de 1 paciente en riesgo ---------------- ❌", end='')
        self.assertEqual(mod.validar_infecciones(e6, e5, e3, e4), "3",
                         "El método no determinó correctamente los pacientes con riesgo de infeccion.")
        print("\rVerificando la valoracion correcta de 1 paciente en riesgo ---------------- ✅")
        test += 1

        print("Verificando la valoracion correcta de 2 pacientes en riesgo --------------- ❌", end='')
        self.assertEqual(mod.validar_infecciones(e1, e2, e5, e6), "1,2",
                         "El método no determinó correctamente los pacientes con riesgo de infeccion.")
        print("\rVerificando la valoracion correcta de 2 pacientes en riesgo --------------- ✅")
        test += 1

    def test_calcular_promedio(self):
        global test
        print()
        print("################### Test calcular_promedio #########################################")

        e1 = mod.crear_paciente(1, "F", 11, 50, 20, 11.5, 50, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        e2 = mod.crear_paciente(2, "F", 6, 75, 20, 12.5, 20, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        e3 = mod.crear_paciente(3, "F", 18, 105, 20, 11, 69, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        e4 = mod.crear_paciente(4, "M", 9, 50, 20, 5.5, 70, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)
        e5 = mod.crear_paciente(5, "M", 15, 75, 20, 4.6, 280, 89.7, 50, 120.8, 240, 7.9, 150, 10, 8)
        e6 = mod.crear_paciente(6, "M", 19, 105, 20, 1.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 10, 8)

        print("Verificando el calculo correcto del promedio de tiempo de pruebas 25 min -- ❌", end='')
        self.assertEqual(mod.calcular_promedio(e1, e2, e3, e4), 25)
        print("\rVerificando el calculo correcto del promedio de tiempo de pruebas 25 min -- ✅")
        test += 1

        print("Verificando el calculo correcto del promedio de tiempo de pruebas 18 min -- ❌", end='')
        self.assertEqual(mod.calcular_promedio(e6, e5, e3, e4), 18)
        print("\rVerificando el calculo correcto del promedio de tiempo de pruebas 18 min -- ✅")
        test += 1

    def test_actualizar_glicemia(self):
        global test
        print()
        print("################### Test actualizar_glicemia #######################################")

        e1 = mod.crear_paciente(1, "F", 11, 50, 20, 11.5, 280, 89.7, 280, 120.8, 240, 7.9, 150, 25, 8)
        e2 = mod.crear_paciente(2, "F", 6, 75, 20, 12.5, 50, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)

        print("Verificando el calculo correcto del numero de ampolletas por usar 2 undades ❌", end='')
        self.assertEqual(mod.actualizar_glicemia(1, 200, e1), 2,
                         "El método no determinó correctamente el numero de ampolletas por usar.")
        print("\rVerificando el calculo correcto del numero de ampolletas por usar 2 undades ✅")
        test += 1

        print("Verificando cambio de nivel despues de actualizar la glicemia ------------- ❌", end='')
        self.assertEqual(e1["glicemia"], 200, "El método actualizó correctamente el nivel de glicemia.")
        print("\rVerificando cambio de nivel despues de actualizar la glicemia ------------- ✅")
        test += 1

        print("Verificando el calculo correcto del numero de ampolletas por usar 0 undades ❌", end='')
        self.assertEqual(mod.actualizar_glicemia(1, 200, e2), 0,
                         "El método no determinó correctamente el numero de ampolletas por usar.")
        print("\rVerificando el calculo correcto del numero de ampolletas por usar 0 undades ✅")
        test += 1

        print("Verificando NO haber cambiado e nivel despues de actualizar la glicemia --- ❌", end='')
        self.assertEqual(e2["glicemia"], 50, "El método cambió el nivel de glicemia correcto.")
        print("\rVerificando NO haber cambiado e nivel despues de actualizar la glicemia --- ✅")
        test += 1

    def test_validar_diabetes(self):
        global test
        print()
        print("################### Test validar_diabetes ##########################################")

        e1 = mod.crear_paciente(1, "F", 11, 50, 20, 11.5, 126, 89.7, 280, 120.8, 240, 7.9, 150, 25, 8)
        e2 = mod.crear_paciente(2, "F", 11, 50, 20, 11.5, 130, 89.7, 280, 120.8, 240, 7.9, 150, 25, 8)
        e3 = mod.crear_paciente(1, "F", 11, 50, 20, 11.5, 112, 89.7, 280, 120.8, 240, 7.9, 150, 25, 8)
        e4 = mod.crear_paciente(2, "F", 11, 50, 20, 11.5, 100, 89.7, 280, 120.8, 240, 7.9, 150, 25, 8)
        e5 = mod.crear_paciente(3, "F", 6, 75, 20, 12.5, 50, 89.7, 50, 120.8, 240, 7.9, 150, 25, 8)

        print("Verificando diagnostico de diabetes en paciente con glicemia 126 ---------- ❌", end='')
        self.assertEqual(mod.validar_diabetes(e1), "diabetes", "El método no determinó si el paciente tiene diabetes.")
        print("\rVerificando diagnostico de diabetes en paciente con glicemia 126 ---------- ✅")
        test += 1

        print("Verificando diagnostico de diabetes en paciente con glicemia 130 ---------- ❌", end='')
        self.assertEqual(mod.validar_diabetes(e2), "diabetes", "El método no determinó si el paciente tiene diabetes.")
        print("\rVerificando diagnostico de diabetes en paciente con glicemia 130 ---------- ✅")
        test += 1

        print("Verificando diagnostico de prediabetes en paciente con glicemia 112 ------- ❌", end='')
        self.assertEqual(mod.validar_diabetes(e3), "prediabetes",
                         "El método no determinó si el paciente tiene prediabetes.")
        print("\rVerificando diagnostico de prediabetes en paciente con glicemia 112 ------- ✅")
        test += 1

        print("Verificando diagnostico de prediabetes en paciente con glicemia 100 ------- ❌", end='')
        self.assertEqual(mod.validar_diabetes(e4), "prediabetes",
                         "El método no determinó si el paciente tiene prediabetes.")
        print("\rVerificando diagnostico de prediabetes en paciente con glicemia 100 ------- ✅")
        test += 1

        print("Verificando estdo normal en paciente con glicemia 50 ---------------------- ❌", end='')
        self.assertEqual(mod.validar_diabetes(e5), "normalidad",
                         "El método no determinó si el paciente está en estado normal.")
        print("\rVerificando estdo normal en paciente con glicemia 50 ---------------------- ✅")
        test += 1

    def test_calcular_riesgo_cardiaco(self):
        global test
        print()
        print("################### Test calcular_riesgo_cardiaco ##################################")

        e1 = mod.crear_paciente(11, "M", 20, 88, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 0)
        e2 = mod.crear_paciente(26, "F", 30, 90, 9, 10.5, 69, 98.3, 60, 100.9, 225, 9.8, 141, 35, 10)
        e3 = mod.crear_paciente(3, "M", 69, 70, 15, 12.5, 130, 100.6, 39, 150.3, 260, 8.2, 160, 15, 2)
        e4 = mod.crear_paciente(3, "F", 69, 70, 15, 12.5, 100, 138.6, 49, 150.3, 260, 8.2, 160, 15, 2)

        print("Verificando calculo correcto de riesgo cardiaco 1 ------------------------- ❌", end='')
        self.assertEqual(mod.calcular_riesgo_cardiaco(e1), 1, "El método no calculo correctamente el riesgo cardiaco.")
        print("\rVerificando calculo correcto de riesgo cardiaco 1 ------------------------- ✅")
        test += 1

        print("Verificando calculo correcto de riesgo cardiaco 0 ------------------------- ❌", end='')
        self.assertEqual(mod.calcular_riesgo_cardiaco(e2), 0, "El método no calculo correctamente el riesgo cardiaco.")
        print("\rVerificando calculo correcto de riesgo cardiaco 0 ------------------------- ✅")
        test += 1

        print("Verificando calculo correcto de riesgo cardiaco 5 ------------------------- ❌", end='')
        self.assertEqual(mod.calcular_riesgo_cardiaco(e3), 5, "El método no calculo correctamente el riesgo cardiaco.")
        print("\rVerificando calculo correcto de riesgo cardiaco 5 ------------------------- ✅")
        test += 1

        print("Verificando calculo correcto de riesgo cardiaco 5 ------------------------- ❌", end='')
        self.assertEqual(mod.calcular_riesgo_cardiaco(e4), 5, "El método no calculo correctamente el riesgo cardiaco.")
        print("\rVerificando calculo correcto de riesgo cardiaco 5 ------------------------- ✅")
        test += 1

    def test_evaluar_prioridad(self):
        global test
        print()
        print("################### Test evaluar_prioridad #########################################")

        e1 = mod.crear_paciente(11, "M", 20, 88, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 0)
        e2 = mod.crear_paciente(26, "F", 30, 90, 9, 10.5, 69, 98.3, 60, 100.9, 225, 9.8, 141, 35, 10)
        e3 = mod.crear_paciente(3, "M", 69, 70, 15, 12.5, 130, 100.6, 50, 150.3, 260, 8.2, 160, 15, 2)
        e4 = mod.crear_paciente(3, "F", 69, 70, 15, 12.5, 100, 138.6, 39, 150.3, 260, 8.2, 160, 15, 2)

        print("Verificando calculo correcto de paciente con mayor prioridad -------------- ❌", end='')
        self.assertEqual(mod.evaluar_prioridad(e1, e2, e3, e4), e4,
                         "El método no determinó correctamente el paciente con mayor prioridad.")
        print("\rVerificando calculo correcto de paciente con mayor prioridad -------------- ✅")
        test += 1

    def test_validar_CLL(self):
        global test
        print()
        print("################### Test validar_CLL ###############################################")

        e1 = mod.crear_paciente(11, "M", 20, 88, 20, 11.5, 280, 89.7, 50, 120.8, 240, 10, 150, 25, 0)
        e2 = mod.crear_paciente(11, "M", 20, 88, 20, 11.5, 280, 89.7, 50, 120.8, 240, 8.1, 130, 25, 0)
        e3 = mod.crear_paciente(26, "F", 30, 90, 9, 10.5, 69, 98.3, 60, 100.9, 225, 5, 141, 35, 10)

        print("Verificando diagnostico correcto de CCL positivo -------------------------- ❌", end='')
        self.assertEqual(mod.validar_CLL(e1, False), 1,
                         "El método no generó correctamente el diagnostico positivo de CLL.")
        print("\rVerificando diagnostico correcto de CCL positivo -------------------------- ✅")
        test += 1

        print("Verificando diagnostico correcto de CCL positivo -------------------------- ❌", end='')
        self.assertEqual(mod.validar_CLL(e2, False), 1,
                         "El método no generó correctamente el diagnostico positivo de CLL.")
        print("\rVerificando diagnostico correcto de CCL positivo -------------------------- ✅")
        test += 1

        print("Verificando diagnostico correcto de CCL negativo -------------------------- ❌", end='')
        self.assertEqual(mod.validar_CLL(e3, False), 0,
                         "El método no generó correctamente el diagnostico negativo de CLL.")
        print("\rVerificando diagnostico correcto de CCL negativo -------------------------- ✅")
        test += 1

        print("Verificando diagnostico correcto de biopsia ------------------------------- ❌", end='')
        self.assertEqual(mod.validar_CLL(e3, True), -1,
                         "El método no generó correctamente el diagnostico de biopsia de CLL.")
        print("\rVerificando diagnostico correcto de biopsia ------------------------------- ✅")
        test += 1


if __name__ == '__main__':
    unittest.main()


def print_percent_done(index, total, bar_len=75, title='Please wait'):
    print()

    percent_done = (index + 1) / total * 100
    percent_done = round(percent_done, 1)

    done = round(percent_done / (100 / bar_len))
    togo = bar_len - done

    done_str = '█' * int(done)
    togo_str = '░' * int(togo)

    print(f'❌Test: [{done_str}{togo_str}] {percent_done}% done', end='\r')

    if round(percent_done) == 100:
        print('✅')


if True:
    print_percent_done(test, 75)
