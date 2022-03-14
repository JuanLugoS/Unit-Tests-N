# -*- coding: utf-8 -*-
"""
Copyright 2021 Juan Lugo Sánchez - jd.lugo@uniandes.edu.co
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish and/or distribute copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to
the following conditions:

Atribution to the original author.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

 * Universidad de Los Andes
 * ISIS 1221 - Introducción a la Programación
 * Proyecto de nivel 2
 * 11 de Marzo de 2022
 *
 * @author Juan Lugo Sánchez
 * jd.lugo@uniandes.edu.co
 * 201913094
"""
import unittest
import cupibook as cb

test = 0


class TestCupiBook(unittest.TestCase):

    def test_crear_amigo(self):
        print()
        print(
            "################### Test crear_amigo ####################################################################")

        global test

        amigo_funcion = cb.crear_amigo("Pedro Gómez", 20000424, "M", "pop", "drama", 100, 20, 5, False)
        amigo = {'nombre': 'Pedro Gómez', 'fecha_de_nacimiento': 20000424, 'signo_zodiacal': 'TAURO', 'genero': 'M',
                 'genero_musical_favorito': 'pop', 'genero_literaro_favorito': 'drama', 'likes': 100,
                 'numero_de_publicaciones': 20, 'amigos_en_comun': 5, 'bloqueado': False}

        print("Verificando la creacion de un amigo ------------------------------------------------------- ❌", end='')
        self.assertEqual(amigo, amigo_funcion, "El diccionario creado no corresponde con los valores dados por "
                                               "parametro; revisar los elementos que tienen + y - para determinar "
                                               "que valores son diferentes")
        print("\rVerificando la creacion de un amigo ------------------------------------------------------- ✅")
        test += 1

    def test_buscar_amigo_por_nombre(self):
        print()
        print(
            "################### Test buscar_amigo_por_nombre ########################################################")

        global test

        amigo1 = {'nombre': 'Pedro Gómez'}
        amigo2 = {'nombre': 'Pedro Gomez'}
        amigo3 = {'nombre': 'Andrés Gómez'}
        amigo4 = {'nombre': 'Pedro Gonzalez'}

        buscado1 = cb.buscar_amigo_por_nombre("Pedro Gómez", amigo1, amigo2, amigo3, amigo4)

        print("Verificando la busqueda del amigo 1 ------------------------------------------------------- ❌", end='')
        self.assertEqual(buscado1, amigo1, "La función no encontró el amigo buscado o encontró el erroneo")
        print("\rVerificando la busqueda del amigo 1 ------------------------------------------------------- ✅")
        test += 1

        buscado2 = cb.buscar_amigo_por_nombre("Pedro Gomez", amigo1, amigo2, amigo3, amigo4)

        print("Verificando la busqueda del amigo 2 ------------------------------------------------------- ❌", end='')
        self.assertEqual(buscado2, amigo2, "La función no encontró el amigo buscado o encontró el erroneo")
        print("\rVerificando la busqueda del amigo 2 ------------------------------------------------------- ✅")
        test += 1

        buscado3 = cb.buscar_amigo_por_nombre("Andrés Gómez", amigo1, amigo2, amigo3, amigo4)

        print("Verificando la busqueda del amigo 3 ------------------------------------------------------- ❌", end='')
        self.assertEqual(buscado3, amigo3, "La función no encontró el amigo buscado o encontró el erroneo")
        print("\rVerificando la busqueda del amigo 3 ------------------------------------------------------- ✅")
        test += 1

        buscado4 = cb.buscar_amigo_por_nombre("Pedro Gonzalez", amigo1, amigo2, amigo3, amigo4)

        print("Verificando la busqueda del amigo 4 ------------------------------------------------------- ❌", end='')
        self.assertEqual(buscado4, amigo4, "La función no encontró el amigo buscado o encontró el erroneo")
        print("\rVerificando la busqueda del amigo 4 ------------------------------------------------------- ✅")
        test += 1

        buscado5 = cb.buscar_amigo_por_nombre("Nicolás Gonzalez", amigo1, amigo2, amigo3, amigo4)

        print("Verificando la busqueda del amigo no existente -------------------------------------------- ❌", end='')
        self.assertIsNone(buscado5, "La función encontró un amigo que no existe")
        print("\rVerificando la busqueda del amigo no existente -------------------------------------------- ✅")
        test += 1

    def test_buscar_amigo_con_mas_likes(self):
        print()
        print(
            "################### Test buscar_amigo_con_mas_likes #####################################################")

        global test

        amigo_con_1like = {'nombre': 'Nicolas Torres', 'numero_de_likes': 1}
        amigo_con_4like = {'nombre': 'Andrea Rodriguez', 'numero_de_likes': 4}
        amigo_con_5like = {'nombre': 'Andrés Gómez', 'numero_de_likes': 5}
        amigo_con_6like = {'nombre': 'Pedro Gonzalez', 'numero_de_likes': 6}

        respuesta_mas_likes = "El usuario Pedro Gonzalez es el usuario más famoso con 6 likes."

        mas_likes_en_1 = cb.buscar_amigo_con_mas_likes(amigo_con_6like, amigo_con_1like, amigo_con_4like,
                                                       amigo_con_5like)

        print("Verificando la busqueda del amigo en la posicion 1 ---------------------------------------- ❌", end='')
        self.assertEqual(mas_likes_en_1, respuesta_mas_likes, "La función no devolvió o encontró el erroneo")
        print("\rVerificando la busqueda del amigo en la posicion 1 ---------------------------------------- ✅")
        test += 1

        mas_likes_en_2 = cb.buscar_amigo_con_mas_likes(amigo_con_1like, amigo_con_6like, amigo_con_4like,
                                                       amigo_con_5like)

        print("Verificando la busqueda del amigo en la posicion 2 ---------------------------------------- ❌", end='')
        self.assertEqual(mas_likes_en_2, respuesta_mas_likes, "La función no devolvió o encontró el erroneo")
        print("\rVerificando la busqueda del amigo en la posicion 2 ---------------------------------------- ✅")
        test += 1

        mas_likes_en_3 = cb.buscar_amigo_con_mas_likes(amigo_con_4like, amigo_con_1like, amigo_con_6like,
                                                       amigo_con_5like)

        print("Verificando la busqueda del amigo en la posicion 3 ---------------------------------------- ❌", end='')
        self.assertEqual(mas_likes_en_3, respuesta_mas_likes, "La función no devolvió o encontró el erroneo")
        print("\rVerificando la busqueda del amigo en la posicion 3 ---------------------------------------- ✅")
        test += 1

        mas_likes_en_4 = cb.buscar_amigo_con_mas_likes(amigo_con_5like, amigo_con_1like, amigo_con_4like,
                                                       amigo_con_6like)

        print("Verificando la busqueda del amigo en la posicion 4 ---------------------------------------- ❌", end='')
        self.assertEqual(mas_likes_en_4, respuesta_mas_likes, "La función no devolvió o encontró el erroneo")
        print("\rVerificando la busqueda del amigo en la posicion 4 ---------------------------------------- ✅")
        test += 1

    def test_buscar_amigo_con_menos_publicaciones(self):
        print()
        print(
            "################### Test buscar_amigo_con_menos_publicaciones ###########################################")

        global test

        amigo_con_1publicaciones = {'nombre': 'Nicolas Torres', 'numero_de_publicaciones': 1}
        amigo_con_4publicaciones = {'nombre': 'Andrea Rodriguez', 'numero_de_publicaciones': 4}
        amigo_con_5publicaciones = {'nombre': 'Andrés Gómez', 'numero_de_publicaciones': 5}
        amigo_con_6publicaciones = {'nombre': 'Pedro Gonzalez', 'numero_de_publicaciones': 6}

        respuesta_mas_publicaciones = "El usuario Nicolas Torres es el usuario con el menor número de publicaciones."

        menos_publicaciones_en_1 = cb.buscar_amigo_con_menos_publicaciones(amigo_con_1publicaciones,
                                                                           amigo_con_4publicaciones,
                                                                           amigo_con_5publicaciones,
                                                                           amigo_con_6publicaciones)

        print("Verificando la busqueda del amigo en la posicion 1 ---------------------------------------- ❌", end='')
        self.assertEqual(menos_publicaciones_en_1, respuesta_mas_publicaciones,
                         "La función no devolvió o encontró el erroneo")
        print("\rVerificando la busqueda del amigo en la posicion 1 ---------------------------------------- ✅")
        test += 1

        menos_publicaciones_en_2 = cb.buscar_amigo_con_menos_publicaciones(amigo_con_4publicaciones,
                                                                           amigo_con_1publicaciones,
                                                                           amigo_con_5publicaciones,
                                                                           amigo_con_6publicaciones)

        print("Verificando la busqueda del amigo en la posicion 2 ---------------------------------------- ❌", end='')
        self.assertEqual(menos_publicaciones_en_2, respuesta_mas_publicaciones,
                         "La función no devolvió o encontró el erroneo")
        print("\rVerificando la busqueda del amigo en la posicion 2 ---------------------------------------- ✅")
        test += 1

        menos_publicaciones_en_3 = cb.buscar_amigo_con_menos_publicaciones(amigo_con_5publicaciones,
                                                                           amigo_con_4publicaciones,
                                                                           amigo_con_1publicaciones,
                                                                           amigo_con_6publicaciones)

        print("Verificando la busqueda del amigo en la posicion 3 ---------------------------------------- ❌", end='')
        self.assertEqual(menos_publicaciones_en_3, respuesta_mas_publicaciones,
                         "La función no devolvió o encontró el erroneo")
        print("\rVerificando la busqueda del amigo en la posicion 3 ---------------------------------------- ✅")
        test += 1

        menos_publicaciones_en_4 = cb.buscar_amigo_con_menos_publicaciones(amigo_con_6publicaciones,
                                                                           amigo_con_4publicaciones,
                                                                           amigo_con_5publicaciones,
                                                                           amigo_con_1publicaciones)

        print("Verificando la busqueda del amigo en la posicion 4 ---------------------------------------- ❌", end='')
        self.assertEqual(menos_publicaciones_en_4, respuesta_mas_publicaciones,
                         "La función no devolvió o encontró el erroneo")
        print("\rVerificando la busqueda del amigo en la posicion 4 ---------------------------------------- ✅")
        test += 1

    def test_asignar_signo_zodiacal(self):
        print()
        print(
            "################### Test asignar_signo_zodiacal #########################################################")

        global test

        # --------------------------------------------------------------------------------------------------------------
        # Fechas de prueba

        capricornio1 = 20001222
        acuario1 = 20000121
        piscis1 = 20000220
        aries1 = 20000321
        tauro1 = 20000421
        capricornio2 = 20000120
        acuario2 = 20000219
        piscis2 = 20000320
        aries2 = 20000420
        tauro2 = 20000521
        geminis1 = 20000522
        cancer1 = 20000622
        leo1 = 20000723
        virgo1 = 20000823
        libra1 = 20000923
        geminis2 = 20000621
        cancer2 = 20000722
        leo2 = 20000822
        virgo2 = 20000922
        libra2 = 20001022
        escorpio1 = 20001023
        sagitario1 = 20001123
        escorpio2 = 20001122
        sagitario2 = 20001221

        # --------------------------------------------------------------------------------------------------------------
        # Escenarios capricornio

        caso_capri1 = cb.asignar_signo_zodiacal(capricornio1)
        caso_capri2 = cb.asignar_signo_zodiacal(capricornio2)

        print(f"Verificando la asignación de capricornio como signo zodiacal para la fecha {capricornio1} ------- ❌",
              end='')
        self.assertEqual(caso_capri1, "CAPRICORNIO", "La función no devolvió o encontró el erroneo")
        print(f"\rVerificando la asignación de capricornio como signo zodiacal para la fecha {capricornio1} ------- ✅")
        test += 1

        print(f"Verificando la asignación de capricornio como signo zodiacal para la fecha {capricornio2} ------- ❌",
              end='')
        self.assertEqual(caso_capri2, "CAPRICORNIO", "La función no devolvió o encontró el erroneo")
        print(f"\rVerificando la asignación de capricornio como signo zodiacal para la fecha {capricornio2} ------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Escenarios acuario

        caso_acuario1 = cb.asignar_signo_zodiacal(acuario1)
        caso_acuario2 = cb.asignar_signo_zodiacal(acuario2)

        print(f"Verificando la asignación de acuario como signo zodiacal para la fecha {acuario1} ----------- ❌",
              end='')
        self.assertEqual(caso_acuario1, "ACUARIO", "La función no devolvió o encontró el erroneo")
        print(f"\rVerificando la asignación de acuario como signo zodiacal para la fecha {acuario1} ----------- ✅")
        test += 1

        print(f"Verificando la asignación de acuario como signo zodiacal para la fecha {acuario2} ----------- ❌",
              end='')
        self.assertEqual(caso_acuario2, "ACUARIO", "La función no devolvió o encontró el erroneo")
        print(f"\rVerificando la asignación de acuario como signo zodiacal para la fecha {acuario2} ----------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Escenarios piscis

        caso_piscis1 = cb.asignar_signo_zodiacal(piscis1)
        caso_piscis2 = cb.asignar_signo_zodiacal(piscis2)

        print(f"Verificando la asignación de piscis como signo zodiacal para la fecha {piscis1} ------------ ❌", end='')
        self.assertEqual(caso_piscis1, "PISCIS", "La función no devolvió o encontró el erroneo")
        print(f"\rVerificando la asignación de piscis como signo zodiacal para la fecha {piscis1} ------------ ✅")
        test += 1

        print(f"Verificando la asignación de piscis como signo zodiacal para la fecha {piscis2} ------------ ❌", end='')
        self.assertEqual(caso_piscis2, "PISCIS", "La función no devolvió o encontró el erroneo")
        print(f"\rVerificando la asignación de piscis como signo zodiacal para la fecha {piscis2} ------------ ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Escenarios aries

        caso_aries1 = cb.asignar_signo_zodiacal(aries1)
        caso_aries2 = cb.asignar_signo_zodiacal(aries2)

        print(f"Verificando la asignación de aries como signo zodiacal para la fecha {aries1} ------------- ❌", end='')
        self.assertEqual(caso_aries1, "ARIES", "La función no devolvió o encontró el erroneo")
        print(f"\rVerificando la asignación de aries como signo zodiacal para la fecha {aries1} ------------- ✅")
        test += 1

        print(f"Verificando la asignación de aries como signo zodiacal para la fecha {aries2} ------------- ❌", end='')
        self.assertEqual(caso_aries2, "ARIES", "La función no devolvió o encontró el erroneo")
        print(f"\rVerificando la asignación de aries como signo zodiacal para la fecha {aries2} ------------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Escenarios tauro

        caso_tauro1 = cb.asignar_signo_zodiacal(tauro1)
        caso_tauro2 = cb.asignar_signo_zodiacal(tauro2)

        print(f"Verificando la asignación de tauro como signo zodiacal para la fecha {tauro1} ------------- ❌", end='')
        self.assertEqual(caso_tauro1, "TAURO", "La función no devolvió o encontró el erroneo")
        print(f"\rVerificando la asignación de tauro como signo zodiacal para la fecha {tauro1} ------------- ✅")
        test += 1

        print(f"Verificando la asignación de tauro como signo zodiacal para la fecha {tauro2} ------------- ❌", end='')
        self.assertEqual(caso_tauro2, "TAURO", "La función no devolvió o encontró el erroneo")
        print(f"\rVerificando la asignación de tauro como signo zodiacal para la fecha {tauro2} ------------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Escenarios geminis

        caso_geminis1 = cb.asignar_signo_zodiacal(geminis1)
        caso_geminis2 = cb.asignar_signo_zodiacal(geminis2)

        print(f"Verificando la asignación de geminis como signo zodiacal para la fecha {geminis1} ----------- ❌",
              end='')
        self.assertEqual(caso_geminis1, "GÉMINIS", "La función no devolvió o encontró el erroneo")
        print(f"\rVerificando la asignación de geminis como signo zodiacal para la fecha {geminis1} ----------- ✅")
        test += 1

        print(f"Verificando la asignación de geminis como signo zodiacal para la fecha {geminis2} ----------- ❌",
              end='')
        self.assertEqual(caso_geminis2, "GÉMINIS", "La función no devolvió o encontró el erroneo")
        print(f"\rVerificando la asignación de geminis como signo zodiacal para la fecha {geminis2} ----------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Escenarios cancer

        caso_cancer1 = cb.asignar_signo_zodiacal(cancer1)
        caso_cancer2 = cb.asignar_signo_zodiacal(cancer2)

        print(f"Verificando la asignación de cancer como signo zodiacal para la fecha {cancer1} ------------ ❌", end='')
        self.assertEqual(caso_cancer1, "CÁNCER", "La función no devolvió o encontró el erroneo")
        print(f"\rVerificando la asignación de cancer como signo zodiacal para la fecha {cancer1} ------------ ✅")
        test += 1

        print(f"Verificando la asignación de cancer como signo zodiacal para la fecha {cancer2} ------------ ❌", end='')
        self.assertEqual(caso_cancer2, "CÁNCER", "La función no devolvió o encontró el erroneo")
        print(f"\rVerificando la asignación de cancer como signo zodiacal para la fecha {cancer2} ------------ ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Escenarios leo

        caso_leo1 = cb.asignar_signo_zodiacal(leo1)
        caso_leo2 = cb.asignar_signo_zodiacal(leo2)

        print(f"Verificando la asignación de leo como signo zodiacal para la fecha {leo1} --------------- ❌", end='')
        self.assertEqual(caso_leo1, "LEO", "La función no devolvió o encontró el erroneo")
        print(f"\rVerificando la asignación de leo como signo zodiacal para la fecha {leo1} --------------- ✅")
        test += 1

        print(f"Verificando la asignación de leo como signo zodiacal para la fecha {leo2} --------------- ❌", end='')
        self.assertEqual(caso_leo2, "LEO", "La función no devolvió o encontró el erroneo")
        print(f"\rVerificando la asignación de leo como signo zodiacal para la fecha {leo2} --------------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Escenarios virgo

        caso_virgo1 = cb.asignar_signo_zodiacal(virgo1)
        caso_virgo2 = cb.asignar_signo_zodiacal(virgo2)

        print(f"Verificando la asignación de virgo como signo zodiacal para la fecha {virgo1} ------------- ❌", end='')
        self.assertEqual(caso_virgo1, "VIRGO", "La función no devolvió o encontró el erroneo")
        print(f"\rVerificando la asignación de virgo como signo zodiacal para la fecha {virgo1} ------------- ✅")
        test += 1

        print(f"Verificando la asignación de virgo como signo zodiacal para la fecha {virgo2} ------------- ❌", end='')
        self.assertEqual(caso_virgo2, "VIRGO", "La función no devolvió o encontró el erroneo")
        print(f"\rVerificando la asignación de virgo como signo zodiacal para la fecha {virgo2} ------------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Escenarios libra

        caso_libra1 = cb.asignar_signo_zodiacal(libra1)
        caso_libra2 = cb.asignar_signo_zodiacal(libra2)

        print(f"Verificando la asignación de libra como signo zodiacal para la fecha {libra1} ------------- ❌", end='')
        self.assertEqual(caso_libra1, "LIBRA", "La función no devolvió o encontró el erroneo")
        print(f"\rVerificando la asignación de libra como signo zodiacal para la fecha {libra1} ------------- ✅")
        test += 1

        print(f"Verificando la asignación de libra como signo zodiacal para la fecha {libra2} ------------- ❌", end='')
        self.assertEqual(caso_libra2, "LIBRA", "La función no devolvió o encontró el erroneo")
        print(f"\rVerificando la asignación de libra como signo zodiacal para la fecha {libra2} ------------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Escenarios escorpio

        caso_escorpio1 = cb.asignar_signo_zodiacal(escorpio1)
        caso_escorpio2 = cb.asignar_signo_zodiacal(escorpio2)

        print(f"Verificando la asignación de escorpio como signo zodiacal para la fecha {escorpio1} ---------- ❌",
              end='')
        self.assertEqual(caso_escorpio1, "ESCORPIO", "La función no devolvió o encontró el erroneo")
        print(f"\rVerificando la asignación de escorpio como signo zodiacal para la fecha {escorpio1} ---------- ✅")
        test += 1

        print(f"Verificando la asignación de escorpio como signo zodiacal para la fecha {escorpio2} ---------- ❌",
              end='')
        self.assertEqual(caso_escorpio2, "ESCORPIO", "La función no devolvió o encontró el erroneo")
        print(f"\rVerificando la asignación de escorpio como signo zodiacal para la fecha {escorpio2} ---------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Escenarios sagitario

        caso_sagitario1 = cb.asignar_signo_zodiacal(sagitario1)
        caso_sagitario2 = cb.asignar_signo_zodiacal(sagitario2)

        print(f"Verificando la asignación de sagitario como signo zodiacal para la fecha {sagitario1} --------- ❌",
              end='')
        self.assertEqual(caso_sagitario1, "SAGITARIO", "La función no devolvió o encontró el erroneo")
        print(f"\rVerificando la asignación de sagitario como signo zodiacal para la fecha {sagitario1} --------- ✅")
        test += 1

        print(f"Verificando la asignación de sagitario como signo zodiacal para la fecha {sagitario2} --------- ❌",
              end='')
        self.assertEqual(caso_sagitario2, "SAGITARIO", "La función no devolvió o encontró el erroneo")
        print(f"\rVerificando la asignación de sagitario como signo zodiacal para la fecha {sagitario2} --------- ✅")
        test += 1

    def test_es_cupiamigo(self):
        print()
        print(
            "################### Test es_cupiamigo ###################################################################")

        global test

        # --------------------------------------------------------------------------------------------------------------
        # Escenario favorable

        amigo1 = {"amigos_en_comun": 3, "bloqueado": False, "genero_literaro_favorito": "drama",
                  "genero_musical_favorito": "pop", "signo_zodiacal": "TAURO"}
        amigo2 = {"amigos_en_comun": 3, "bloqueado": False, "genero_literaro_favorito": "drama",
                  "genero_musical_favorito": "pop", "signo_zodiacal": "TAURO"}

        # --------------------------------------------------------------------------------------------------------------
        # Escenarios desfavorables

        amigo3 = {"amigos_en_comun": 3, "bloqueado": True, "genero_literaro_favorito": "drama",
                  "genero_musical_favorito": "pop", "signo_zodiacal": "TAURO"}
        amigo4 = {"amigos_en_comun": 3, "bloqueado": False, "genero_literaro_favorito": "drama",
                  "genero_musical_favorito": "pop", "signo_zodiacal": "TAURO"}

        amigo5 = {"amigos_en_comun": 3, "bloqueado": False, "genero_literaro_favorito": "lirico",
                  "genero_musical_favorito": "pop", "signo_zodiacal": "TAURO"}
        amigo6 = {"amigos_en_comun": 3, "bloqueado": False, "genero_literaro_favorito": "drama",
                  "genero_musical_favorito": "pop", "signo_zodiacal": "TAURO"}

        amigo7 = {"amigos_en_comun": 3, "bloqueado": False, "genero_literaro_favorito": "drama",
                  "genero_musical_favorito": "pop", "signo_zodiacal": "TAURO"}
        amigo8 = {"amigos_en_comun": 3, "bloqueado": False, "genero_literaro_favorito": "drama",
                  "genero_musical_favorito": "rock", "signo_zodiacal": "TAURO"}

        amigo9 = {"amigos_en_comun": 3, "bloqueado": False, "genero_literaro_favorito": "drama",
                  "genero_musical_favorito": "pop", "signo_zodiacal": "TAURO"}
        amigo0 = {"amigos_en_comun": 0, "bloqueado": False, "genero_literaro_favorito": "drama",
                  "genero_musical_favorito": "pop", "signo_zodiacal": "TAURO"}

        amigo11 = {"amigos_en_comun": 3, "bloqueado": False, "genero_literaro_favorito": "drama",
                   "genero_musical_favorito": "pop", "signo_zodiacal": "ARIES"}
        amigo12 = {"amigos_en_comun": 3, "bloqueado": False, "genero_literaro_favorito": "drama",
                   "genero_musical_favorito": "pop", "signo_zodiacal": "TAURO"}

        # --------------------------------------------------------------------------------------------------------------
        # Escenario favorable

        amigos_compatibles = cb.es_cupiamigo(amigo1, amigo2)

        print('Verificando si un par de amigos son compatibles ------------------------------------------- ❌ ', end='')
        self.assertTrue(amigos_compatibles,
                        "La función determinó que los amigos NO eran compatibles a pesar de que SI lo eran")
        print('\rVerificando si un par de amigos son compatibles ------------------------------------------- ✅ ')
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Escenario no compatibles por amigos en comun

        amigos_en_comun1 = cb.es_cupiamigo(amigo9, amigo0)

        print('Verificando si un par de amigos son compatibles por amigos en comun ----------------------- ❌ ', end='')
        self.assertFalse(amigos_en_comun1,
                         "La función determinó que los amigos SI eran compatibles a pesar de que NO lo eran")
        print('\rVerificando si un par de amigos son compatibles por amigos en comun ----------------------- ✅ ')
        test += 1

        amigos_en_comun2 = cb.es_cupiamigo(amigo0, amigo9)

        print('Verificando si un par de amigos son compatibles por amigos en comun ----------------------- ❌ ', end='')
        self.assertFalse(amigos_en_comun2,
                         "La función determinó que los amigos SI eran compatibles a pesar de que NO lo eran")
        print('\rVerificando si un par de amigos son compatibles por amigos en comun ----------------------- ✅ ')
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Escenario no compatibles por bloqueo

        amigos_en_bloqueo1 = cb.es_cupiamigo(amigo3, amigo4)

        print('Verificando si un par de amigos son compatibles por bloqueo ------------------------------- ❌ ', end='')
        self.assertFalse(amigos_en_bloqueo1,
                         "La función determinó que los amigos SI eran compatibles a pesar de que NO lo eran")
        print('\rVerificando si un par de amigos son compatibles por bloqueo ------------------------------- ✅ ')
        test += 1

        amigos_en_bloqueo2 = cb.es_cupiamigo(amigo4, amigo3)

        print('Verificando si un par de amigos son compatibles por bloqueo ------------------------------- ❌ ', end='')
        self.assertFalse(amigos_en_bloqueo2,
                         "La función determinó que los amigos SI eran compatibles a pesar de que NO lo eran")
        print('\rVerificando si un par de amigos son compatibles por bloqueo ------------------------------- ✅ ')
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Escenario no compatibles por amigos en literario y musical

        amigos_en_gen1 = cb.es_cupiamigo(amigo5, amigo6)

        print('Verificando si un par de amigos son compatibles por gen. literatio ------------------------ ❌ ', end='')
        self.assertFalse(amigos_en_gen1,
                         "La función determinó que los amigos SI eran compatibles a pesar de que NO lo eran")
        print('\rVerificando si un par de amigos son compatibles por gen. literatio ------------------------ ✅ ')
        test += 1

        amigos_en_gen2 = cb.es_cupiamigo(amigo7, amigo8)

        print('Verificando si un par de amigos son compatibles por gen. musical -------------------------- ❌ ', end='')
        self.assertFalse(amigos_en_gen2,
                         "La función determinó que los amigos SI eran compatibles a pesar de que NO lo eran")
        print('\rVerificando si un par de amigos son compatibles por gen. musical -------------------------- ✅ ')
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Escenario no compatibles por signo

        amigos_en_signo1 = cb.es_cupiamigo(amigo11, amigo12)

        print('Verificando si un par de amigos son compatibles por signo zodiacal ------------------------ ❌ ', end='')
        self.assertFalse(amigos_en_signo1,
                         "La función determinó que los amigos SI eran compatibles a pesar de que NO lo eran")
        print('\rVerificando si un par de amigos son compatibles por signo zodiacal ------------------------ ✅ ')
        test += 1

        amigos_en_signo2 = cb.es_cupiamigo(amigo12, amigo11)

        print('Verificando si un par de amigos son compatibles por signo zodiacal ------------------------ ❌ ', end='')
        self.assertFalse(amigos_en_signo2,
                         "La función determinó que los amigos SI eran compatibles a pesar de que NO lo eran")
        print('\rVerificando si un par de amigos son compatibles por signo zodiacal ------------------------ ✅ ')
        test += 1

    def test_es_cupienemigo(self):
        print()
        print(
            "################### Test es_cupienemigo #################################################################")

        global test

        # --------------------------------------------------------------------------------------------------------------
        # Escenario favorable

        amigo1 = {"bloqueado": False, "numero_de_likes": 5, "amigos_en_comun": 1}

        # --------------------------------------------------------------------------------------------------------------
        # Escenarios desfavorables

        amigo2 = {"bloqueado": True, "numero_de_likes": 5, "amigos_en_comun": 1}
        amigo3 = {"bloqueado": False, "numero_de_likes": 4, "amigos_en_comun": 1}
        amigo4 = {"bloqueado": False, "numero_de_likes": 5, "amigos_en_comun": 0}

        # --------------------------------------------------------------------------------------------------------------
        # Escenario favorable

        no_cupienemigo = cb.es_cupienemigo(amigo1)

        print('Verificando si un amigo NO es cupienemigo ------------------------------------------------- ❌ ', end='')
        self.assertFalse(no_cupienemigo,
                         "La función determinó que era un cupienemigo a pesar de que NO lo era")
        print('\rVerificando si un amigo NO es cupienemigo ------------------------------------------------- ✅ ')
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Escenario bloqueo

        es_cupienemigo_por_bloqueo = cb.es_cupienemigo(amigo2)

        print('Verificando si un amigo es cupienemigo por bloqueo ---------------------------------------- ❌ ', end='')
        self.assertTrue(es_cupienemigo_por_bloqueo,
                        "La función determinó que NO era un cupienemigo a pesar de que SI lo era")
        print('\rVerificando si un amigo es cupienemigo por bloqueo ---------------------------------------- ✅ ')
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Escenario likes

        es_cupienemigo_por_likes = cb.es_cupienemigo(amigo3)

        print('Verificando si un amigo es cupienemigo por likes ------------------------------------------ ❌ ', end='')
        self.assertTrue(es_cupienemigo_por_likes,
                        "La función determinó que NO era un cupienemigo a pesar de que SI lo era")
        print('\rVerificando si un amigo es cupienemigo por likes ------------------------------------------ ✅ ')
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Escenario likes

        es_cupienemigo_por_amigos = cb.es_cupienemigo(amigo4)

        print('Verificando si un amigo es cupienemigo por amigos ----------------------------------------- ❌ ', end='')
        self.assertTrue(es_cupienemigo_por_amigos,
                        "La función determinó que NO era un cupienemigo a pesar de que SI lo era")
        print('\rVerificando si un amigo es cupienemigo por amigos ----------------------------------------- ✅ ')
        test += 1

    def test_signo_es_compatible(self):
        print()
        print(
            "################### Test signo_es_compatible ############################################################")

        global test

        aries = {'signo_zodiacal': 'ARIES'}
        tauro = {'signo_zodiacal': 'TAURO'}
        geminis = {'signo_zodiacal': 'GÉMINIS'}
        cancer = {'signo_zodiacal': 'CÁNCER'}
        leo = {'signo_zodiacal': 'LEO'}
        virgo = {'signo_zodiacal': 'VIRGO'}
        libra = {'signo_zodiacal': 'LIBRA'}
        escorpio = {'signo_zodiacal': 'ESCORPIO'}
        sagitario = {'signo_zodiacal': 'SAGITARIO'}
        capricornio = {'signo_zodiacal': 'CAPRICORNIO'}
        acuario = {'signo_zodiacal': 'ACUARIO'}
        piscis = {'signo_zodiacal': 'PISCIS'}

        # --------------------------------------------------------------------------------------------------------------
        # Escenario aries y aries

        ariesaries = cb.signo_es_compatible(aries, aries)
        print('verificando si los signos aries y aries son compatiples ----------------------------------- ❌ ', end='')
        self.assertEqual(ariesaries, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos aries y aries son compatiples ----------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario aries y tauro

        ariestauro = cb.signo_es_compatible(aries, tauro)
        print('verificando si los signos aries y tauro son compatiples ----------------------------------- ❌ ', end='')
        self.assertEqual(ariestauro, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos aries y tauro son compatiples ----------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario aries y geminis

        ariesgeminis = cb.signo_es_compatible(aries, geminis)
        print('verificando si los signos aries y geminis son compatiples --------------------------------- ❌ ', end='')
        self.assertEqual(ariesgeminis, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos aries y geminis son compatiples --------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario aries y cancer

        ariescancer = cb.signo_es_compatible(aries, cancer)
        print('verificando si los signos aries y cancer son compatiples ---------------------------------- ❌ ', end='')
        self.assertEqual(ariescancer, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos aries y cancer son compatiples ---------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario aries y leo

        ariesleo = cb.signo_es_compatible(aries, leo)
        print('verificando si los signos aries y leo son compatiples ------------------------------------- ❌ ', end='')
        self.assertEqual(ariesleo, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos aries y leo son compatiples ------------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario aries y virgo

        ariesvirgo = cb.signo_es_compatible(aries, virgo)
        print('verificando si los signos aries y virgo son compatiples ----------------------------------- ❌ ', end='')
        self.assertEqual(ariesvirgo, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos aries y virgo son compatiples ----------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario aries y libra

        arieslibra = cb.signo_es_compatible(aries, libra)
        print('verificando si los signos aries y libra son compatiples ----------------------------------- ❌ ', end='')
        self.assertEqual(arieslibra, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos aries y libra son compatiples ----------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario aries y escorpio

        ariesescorpio = cb.signo_es_compatible(aries, escorpio)
        print('verificando si los signos aries y escorpio son compatiples -------------------------------- ❌ ', end='')
        self.assertEqual(ariesescorpio, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos aries y escorpio son compatiples -------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario aries y sagitario

        ariessagitario = cb.signo_es_compatible(aries, sagitario)
        print('verificando si los signos aries y sagitario son compatiples ------------------------------- ❌ ', end='')
        self.assertEqual(ariessagitario, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos aries y sagitario son compatiples ------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario aries y capricornio

        ariescapricornio = cb.signo_es_compatible(aries, capricornio)
        print('verificando si los signos aries y capricornio son compatiples ----------------------------- ❌ ', end='')
        self.assertEqual(ariescapricornio, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos aries y capricornio son compatiples ----------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario aries y acuario

        ariesacuario = cb.signo_es_compatible(aries, acuario)
        print('verificando si los signos aries y acuario son compatiples --------------------------------- ❌ ', end='')
        self.assertEqual(ariesacuario, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos aries y acuario son compatiples --------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario aries y piscis

        ariespiscis = cb.signo_es_compatible(aries, piscis)
        print('verificando si los signos aries y piscis son compatiples ---------------------------------- ❌ ', end='')
        self.assertEqual(ariespiscis, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos aries y piscis son compatiples ---------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario tauro y aries

        tauroaries = cb.signo_es_compatible(tauro, aries)
        print('verificando si los signos tauro y aries son compatiples ----------------------------------- ❌ ', end='')
        self.assertEqual(tauroaries, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos tauro y aries son compatiples ----------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario tauro y tauro

        taurotauro = cb.signo_es_compatible(tauro, tauro)
        print('verificando si los signos tauro y tauro son compatiples ----------------------------------- ❌ ', end='')
        self.assertEqual(taurotauro, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos tauro y tauro son compatiples ----------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario tauro y geminis

        taurogeminis = cb.signo_es_compatible(tauro, geminis)
        print('verificando si los signos tauro y geminis son compatiples --------------------------------- ❌ ', end='')
        self.assertEqual(taurogeminis, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos tauro y geminis son compatiples --------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario tauro y cancer

        taurocancer = cb.signo_es_compatible(tauro, cancer)
        print('verificando si los signos tauro y cancer son compatiples ---------------------------------- ❌ ', end='')
        self.assertEqual(taurocancer, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos tauro y cancer son compatiples ---------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario tauro y leo

        tauroleo = cb.signo_es_compatible(tauro, leo)
        print('verificando si los signos tauro y leo son compatiples ------------------------------------- ❌ ', end='')
        self.assertEqual(tauroleo, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos tauro y leo son compatiples ------------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario tauro y virgo

        taurovirgo = cb.signo_es_compatible(tauro, virgo)
        print('verificando si los signos tauro y virgo son compatiples ----------------------------------- ❌ ', end='')
        self.assertEqual(taurovirgo, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos tauro y virgo son compatiples ----------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario tauro y libra

        taurolibra = cb.signo_es_compatible(tauro, libra)
        print('verificando si los signos tauro y libra son compatiples ----------------------------------- ❌ ', end='')
        self.assertEqual(taurolibra, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos tauro y libra son compatiples ----------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario tauro y escorpio

        tauroescorpio = cb.signo_es_compatible(tauro, escorpio)
        print('verificando si los signos tauro y escorpio son compatiples -------------------------------- ❌ ', end='')
        self.assertEqual(tauroescorpio, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos tauro y escorpio son compatiples -------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario tauro y sagitario

        taurosagitario = cb.signo_es_compatible(tauro, sagitario)
        print('verificando si los signos tauro y sagitario son compatiples ------------------------------- ❌ ', end='')
        self.assertEqual(taurosagitario, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos tauro y sagitario son compatiples ------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario tauro y capricornio

        taurocapricornio = cb.signo_es_compatible(tauro, capricornio)
        print('verificando si los signos tauro y capricornio son compatiples ----------------------------- ❌ ', end='')
        self.assertEqual(taurocapricornio, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos tauro y capricornio son compatiples ----------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario tauro y acuario

        tauroacuario = cb.signo_es_compatible(tauro, acuario)
        print('verificando si los signos tauro y acuario son compatiples --------------------------------- ❌ ', end='')
        self.assertEqual(tauroacuario, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos tauro y acuario son compatiples --------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario tauro y piscis

        tauropiscis = cb.signo_es_compatible(tauro, piscis)
        print('verificando si los signos tauro y piscis son compatiples ---------------------------------- ❌ ', end='')
        self.assertEqual(tauropiscis, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos tauro y piscis son compatiples ---------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario geminis y aries

        geminisaries = cb.signo_es_compatible(geminis, aries)
        print('verificando si los signos geminis y aries son compatiples --------------------------------- ❌ ', end='')
        self.assertEqual(geminisaries, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos geminis y aries son compatiples --------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario geminis y tauro

        geministauro = cb.signo_es_compatible(geminis, tauro)
        print('verificando si los signos geminis y tauro son compatiples --------------------------------- ❌ ', end='')
        self.assertEqual(geministauro, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos geminis y tauro son compatiples --------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario geminis y geminis

        geminisgeminis = cb.signo_es_compatible(geminis, geminis)
        print('verificando si los signos geminis y geminis son compatiples ------------------------------- ❌ ', end='')
        self.assertEqual(geminisgeminis, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos geminis y geminis son compatiples ------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario geminis y cancer

        geminiscancer = cb.signo_es_compatible(geminis, cancer)
        print('verificando si los signos geminis y cancer son compatiples -------------------------------- ❌ ', end='')
        self.assertEqual(geminiscancer, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos geminis y cancer son compatiples -------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario geminis y leo

        geminisleo = cb.signo_es_compatible(geminis, leo)
        print('verificando si los signos geminis y leo son compatiples ----------------------------------- ❌ ', end='')
        self.assertEqual(geminisleo, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos geminis y leo son compatiples ----------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario geminis y virgo

        geminisvirgo = cb.signo_es_compatible(geminis, virgo)
        print('verificando si los signos geminis y virgo son compatiples --------------------------------- ❌ ', end='')
        self.assertEqual(geminisvirgo, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos geminis y virgo son compatiples --------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario geminis y libra

        geminislibra = cb.signo_es_compatible(geminis, libra)
        print('verificando si los signos geminis y libra son compatiples --------------------------------- ❌ ', end='')
        self.assertEqual(geminislibra, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos geminis y libra son compatiples --------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario geminis y escorpio

        geminisescorpio = cb.signo_es_compatible(geminis, escorpio)
        print('verificando si los signos geminis y escorpio son compatiples ------------------------------ ❌ ', end='')
        self.assertEqual(geminisescorpio, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos geminis y escorpio son compatiples ------------------------------ ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario geminis y sagitario

        geminissagitario = cb.signo_es_compatible(geminis, sagitario)
        print('verificando si los signos geminis y sagitario son compatiples ---------------------------- ❌ ', end='')
        self.assertEqual(geminissagitario, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos geminis y sagitario son compatiples ----------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario geminis y capricornio

        geminiscapricornio = cb.signo_es_compatible(geminis, capricornio)
        print('verificando si los signos geminis y capricornio son compatiples --------------------------- ❌ ', end='')
        self.assertEqual(geminiscapricornio, False, 'La función determinó erradamente que eran compatibles')
        print(
            '\rVerificando si los signos geminis y capricornio son compatiples --------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario geminis y acuario

        geminisacuario = cb.signo_es_compatible(geminis, acuario)
        print('verificando si los signos geminis y acuario son compatiples ------------------------------- ❌ ', end='')
        self.assertEqual(geminisacuario, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos geminis y acuario son compatiples ------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario geminis y piscis

        geminispiscis = cb.signo_es_compatible(geminis, piscis)
        print('verificando si los signos geminis y piscis son compatiples -------------------------------- ❌ ', end='')
        self.assertEqual(geminispiscis, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos geminis y piscis son compatiples -------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario cancer y aries

        canceraries = cb.signo_es_compatible(cancer, aries)
        print('verificando si los signos cancer y aries son compatiples ---------------------------------- ❌ ', end='')
        self.assertEqual(canceraries, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos cancer y aries son compatiples ---------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario cancer y tauro

        cancertauro = cb.signo_es_compatible(cancer, tauro)
        print('verificando si los signos cancer y tauro son compatiples ---------------------------------- ❌ ', end='')
        self.assertEqual(cancertauro, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos cancer y tauro son compatiples ---------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario cancer y geminis

        cancergeminis = cb.signo_es_compatible(cancer, geminis)
        print('verificando si los signos cancer y geminis son compatiples -------------------------------- ❌ ', end='')
        self.assertEqual(cancergeminis, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos cancer y geminis son compatiples -------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario cancer y cancer

        cancercancer = cb.signo_es_compatible(cancer, cancer)
        print('verificando si los signos cancer y cancer son compatiples --------------------------------- ❌ ', end='')
        self.assertEqual(cancercancer, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos cancer y cancer son compatiples --------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario cancer y leo

        cancerleo = cb.signo_es_compatible(cancer, leo)
        print('verificando si los signos cancer y leo son compatiples ------------------------------------ ❌ ', end='')
        self.assertEqual(cancerleo, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos cancer y leo son compatiples ------------------------------------ ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario cancer y virgo

        cancervirgo = cb.signo_es_compatible(cancer, virgo)
        print('verificando si los signos cancer y virgo son compatiples ---------------------------------- ❌ ', end='')
        self.assertEqual(cancervirgo, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos cancer y virgo son compatiples ---------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario cancer y libra

        cancerlibra = cb.signo_es_compatible(cancer, libra)
        print('verificando si los signos cancer y libra son compatiples ---------------------------------- ❌ ', end='')
        self.assertEqual(cancerlibra, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos cancer y libra son compatiples ---------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario cancer y escorpio

        cancerescorpio = cb.signo_es_compatible(cancer, escorpio)
        print('verificando si los signos cancer y escorpio son compatiples ------------------------------- ❌ ', end='')
        self.assertEqual(cancerescorpio, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos cancer y escorpio son compatiples ------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario cancer y sagitario

        cancersagitario = cb.signo_es_compatible(cancer, sagitario)
        print('verificando si los signos cancer y sagitario son compatiples ------------------------------ ❌ ', end='')
        self.assertEqual(cancersagitario, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos cancer y sagitario son compatiples ------------------------------ ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario cancer y capricornio

        cancercapricornio = cb.signo_es_compatible(cancer, capricornio)
        print('verificando si los signos cancer y capricornio son compatiples ---------------------------- ❌ ', end='')
        self.assertEqual(cancercapricornio, False, 'La función determinó erradamente que eran compatibles')
        print(
            '\rVerificando si los signos cancer y capricornio son compatiples ---------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario cancer y acuario

        canceracuario = cb.signo_es_compatible(cancer, acuario)
        print('verificando si los signos cancer y acuario son compatiples -------------------------------- ❌ ', end='')
        self.assertEqual(canceracuario, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos cancer y acuario son compatiples -------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario cancer y piscis

        cancerpiscis = cb.signo_es_compatible(cancer, piscis)
        print('verificando si los signos cancer y piscis son compatiples --------------------------------- ❌ ', end='')
        self.assertEqual(cancerpiscis, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos cancer y piscis son compatiples --------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario leo y aries

        leoaries = cb.signo_es_compatible(leo, aries)
        print('verificando si los signos leo y aries son compatiples ------------------------------------- ❌ ', end='')
        self.assertEqual(leoaries, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos leo y aries son compatiples ------------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario leo y tauro

        leotauro = cb.signo_es_compatible(leo, tauro)
        print('verificando si los signos leo y tauro son compatiples ------------------------------------- ❌ ', end='')
        self.assertEqual(leotauro, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos leo y tauro son compatiples ------------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario leo y geminis

        leogeminis = cb.signo_es_compatible(leo, geminis)
        print('verificando si los signos leo y geminis son compatiples ----------------------------------- ❌ ', end='')
        self.assertEqual(leogeminis, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos leo y geminis son compatiples ----------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario leo y cancer

        leocancer = cb.signo_es_compatible(leo, cancer)
        print('verificando si los signos leo y cancer son compatiples ------------------------------------ ❌ ', end='')
        self.assertEqual(leocancer, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos leo y cancer son compatiples ------------------------------------ ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario leo y leo

        leoleo = cb.signo_es_compatible(leo, leo)
        print('verificando si los signos leo y leo son compatiples --------------------------------------- ❌ ', end='')
        self.assertEqual(leoleo, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos leo y leo son compatiples --------------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario leo y virgo

        leovirgo = cb.signo_es_compatible(leo, virgo)
        print('verificando si los signos leo y virgo son compatiples ------------------------------------- ❌ ', end='')
        self.assertEqual(leovirgo, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos leo y virgo son compatiples ------------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario leo y libra

        leolibra = cb.signo_es_compatible(leo, libra)
        print('verificando si los signos leo y libra son compatiples ------------------------------------- ❌ ', end='')
        self.assertEqual(leolibra, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos leo y libra son compatiples ------------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario leo y escorpio

        leoescorpio = cb.signo_es_compatible(leo, escorpio)
        print('verificando si los signos leo y escorpio son compatiples ---------------------------------- ❌ ', end='')
        self.assertEqual(leoescorpio, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos leo y escorpio son compatiples ---------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario leo y sagitario

        leosagitario = cb.signo_es_compatible(leo, sagitario)
        print('verificando si los signos leo y sagitario son compatiples -------------------------------- ❌ ', end='')
        self.assertEqual(leosagitario, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos leo y sagitario son compatiples --------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario leo y capricornio

        leocapricornio = cb.signo_es_compatible(leo, capricornio)
        print('verificando si los signos leo y capricornio son compatiples ------------------------------- ❌ ', end='')
        self.assertEqual(leocapricornio, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos leo y capricornio son compatiples ------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario leo y acuario

        leoacuario = cb.signo_es_compatible(leo, acuario)
        print('verificando si los signos leo y acuario son compatiples ----------------------------------- ❌ ', end='')
        self.assertEqual(leoacuario, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos leo y acuario son compatiples ----------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario leo y piscis

        leopiscis = cb.signo_es_compatible(leo, piscis)
        print('verificando si los signos leo y piscis son compatiples ------------------------------------ ❌ ', end='')
        self.assertEqual(leopiscis, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos leo y piscis son compatiples ------------------------------------ ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario virgo y aries

        virgoaries = cb.signo_es_compatible(virgo, aries)
        print('verificando si los signos virgo y aries son compatiples ----------------------------------- ❌ ', end='')
        self.assertEqual(virgoaries, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos virgo y aries son compatiples ----------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario virgo y tauro

        virgotauro = cb.signo_es_compatible(virgo, tauro)
        print('verificando si los signos virgo y tauro son compatiples ----------------------------------- ❌ ', end='')
        self.assertEqual(virgotauro, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos virgo y tauro son compatiples ----------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario virgo y geminis

        virgogeminis = cb.signo_es_compatible(virgo, geminis)
        print('verificando si los signos virgo y geminis son compatiples --------------------------------- ❌ ', end='')
        self.assertEqual(virgogeminis, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos virgo y geminis son compatiples --------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario virgo y cancer

        virgocancer = cb.signo_es_compatible(virgo, cancer)
        print('verificando si los signos virgo y cancer son compatiples ---------------------------------- ❌ ', end='')
        self.assertEqual(virgocancer, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos virgo y cancer son compatiples ---------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario virgo y leo

        virgoleo = cb.signo_es_compatible(virgo, leo)
        print('verificando si los signos virgo y leo son compatiples ------------------------------------- ❌ ', end='')
        self.assertEqual(virgoleo, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos virgo y leo son compatiples ------------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario virgo y virgo

        virgovirgo = cb.signo_es_compatible(virgo, virgo)
        print('verificando si los signos virgo y virgo son compatiples ----------------------------------- ❌ ', end='')
        self.assertEqual(virgovirgo, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos virgo y virgo son compatiples ----------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario virgo y libra

        virgolibra = cb.signo_es_compatible(virgo, libra)
        print('verificando si los signos virgo y libra son compatiples ----------------------------------- ❌ ', end='')
        self.assertEqual(virgolibra, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos virgo y libra son compatiples ----------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario virgo y escorpio

        virgoescorpio = cb.signo_es_compatible(virgo, escorpio)
        print('verificando si los signos virgo y escorpio son compatiples -------------------------------- ❌ ', end='')
        self.assertEqual(virgoescorpio, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos virgo y escorpio son compatiples -------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario virgo y sagitario

        virgosagitario = cb.signo_es_compatible(virgo, sagitario)
        print('verificando si los signos virgo y sagitario son compatiples ------------------------------- ❌ ', end='')
        self.assertEqual(virgosagitario, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos virgo y sagitario son compatiples ------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario virgo y capricornio

        virgocapricornio = cb.signo_es_compatible(virgo, capricornio)
        print('verificando si los signos virgo y capricornio son compatiples ----------------------------- ❌ ', end='')
        self.assertEqual(virgocapricornio, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos virgo y capricornio son compatiples ----------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario virgo y acuario

        virgoacuario = cb.signo_es_compatible(virgo, acuario)
        print('verificando si los signos virgo y acuario son compatiples --------------------------------- ❌ ', end='')
        self.assertEqual(virgoacuario, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos virgo y acuario son compatiples --------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario virgo y piscis

        virgopiscis = cb.signo_es_compatible(virgo, piscis)
        print('verificando si los signos virgo y piscis son compatiples ---------------------------------- ❌ ', end='')
        self.assertEqual(virgopiscis, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos virgo y piscis son compatiples ---------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario libra y aries

        libraaries = cb.signo_es_compatible(libra, aries)
        print('verificando si los signos libra y aries son compatiples ----------------------------------- ❌ ', end='')
        self.assertEqual(libraaries, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos libra y aries son compatiples ----------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario libra y tauro

        libratauro = cb.signo_es_compatible(libra, tauro)
        print('verificando si los signos libra y tauro son compatiples ----------------------------------- ❌ ', end='')
        self.assertEqual(libratauro, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos libra y tauro son compatiples ----------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario libra y geminis

        librageminis = cb.signo_es_compatible(libra, geminis)
        print('verificando si los signos libra y geminis son compatiples --------------------------------- ❌ ', end='')
        self.assertEqual(librageminis, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos libra y geminis son compatiples --------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario libra y cancer

        libracancer = cb.signo_es_compatible(libra, cancer)
        print('verificando si los signos libra y cancer son compatiples ---------------------------------- ❌ ', end='')
        self.assertEqual(libracancer, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos libra y cancer son compatiples ---------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario libra y leo

        libraleo = cb.signo_es_compatible(libra, leo)
        print('verificando si los signos libra y leo son compatiples ------------------------------------- ❌ ', end='')
        self.assertEqual(libraleo, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos libra y leo son compatiples ------------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario libra y virgo

        libravirgo = cb.signo_es_compatible(libra, virgo)
        print('verificando si los signos libra y virgo son compatiples ----------------------------------- ❌ ', end='')
        self.assertEqual(libravirgo, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos libra y virgo son compatiples ----------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario libra y libra

        libralibra = cb.signo_es_compatible(libra, libra)
        print('verificando si los signos libra y libra son compatiples ----------------------------------- ❌ ', end='')
        self.assertEqual(libralibra, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos libra y libra son compatiples ----------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario libra y escorpio

        libraescorpio = cb.signo_es_compatible(libra, escorpio)
        print('verificando si los signos libra y escorpio son compatiples -------------------------------- ❌ ', end='')
        self.assertEqual(libraescorpio, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos libra y escorpio son compatiples -------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario libra y sagitario

        librasagitario = cb.signo_es_compatible(libra, sagitario)
        print('verificando si los signos libra y sagitario son compatiples ------------------------------- ❌ ', end='')
        self.assertEqual(librasagitario, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos libra y sagitario son compatiples ------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario libra y capricornio

        libracapricornio = cb.signo_es_compatible(libra, capricornio)
        print('verificando si los signos libra y capricornio son compatiples ---------------------------- ❌ ', end='')
        self.assertEqual(libracapricornio, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos libra y capricornio son compatiples ----------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario libra y acuario

        libraacuario = cb.signo_es_compatible(libra, acuario)
        print('verificando si los signos libra y acuario son compatiples --------------------------------- ❌ ', end='')
        self.assertEqual(libraacuario, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos libra y acuario son compatiples --------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario libra y piscis

        librapiscis = cb.signo_es_compatible(libra, piscis)
        print('verificando si los signos libra y piscis son compatiples ---------------------------------- ❌ ', end='')
        self.assertEqual(librapiscis, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos libra y piscis son compatiples ---------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario escorpio y aries

        escorpioaries = cb.signo_es_compatible(escorpio, aries)
        print('verificando si los signos escorpio y aries son compatiples -------------------------------- ❌ ', end='')
        self.assertEqual(escorpioaries, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos escorpio y aries son compatiples -------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario escorpio y tauro

        escorpiotauro = cb.signo_es_compatible(escorpio, tauro)
        print('verificando si los signos escorpio y tauro son compatiples -------------------------------- ❌ ', end='')
        self.assertEqual(escorpiotauro, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos escorpio y tauro son compatiples -------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario escorpio y geminis

        escorpiogeminis = cb.signo_es_compatible(escorpio, geminis)
        print('verificando si los signos escorpio y geminis son compatiples ------------------------------ ❌ ', end='')
        self.assertEqual(escorpiogeminis, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos escorpio y geminis son compatiples ------------------------------ ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario escorpio y cancer

        escorpiocancer = cb.signo_es_compatible(escorpio, cancer)
        print('verificando si los signos escorpio y cancer son compatiples ------------------------------- ❌ ', end='')
        self.assertEqual(escorpiocancer, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos escorpio y cancer son compatiples ------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario escorpio y leo

        escorpioleo = cb.signo_es_compatible(escorpio, leo)
        print('verificando si los signos escorpio y leo son compatiples ---------------------------------- ❌ ', end='')
        self.assertEqual(escorpioleo, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos escorpio y leo son compatiples ---------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario escorpio y virgo

        escorpiovirgo = cb.signo_es_compatible(escorpio, virgo)
        print('verificando si los signos escorpio y virgo son compatiples -------------------------------- ❌ ', end='')
        self.assertEqual(escorpiovirgo, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos escorpio y virgo son compatiples -------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario escorpio y libra

        escorpiolibra = cb.signo_es_compatible(escorpio, libra)
        print('verificando si los signos escorpio y libra son compatiples -------------------------------- ❌ ', end='')
        self.assertEqual(escorpiolibra, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos escorpio y libra son compatiples -------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario escorpio y escorpio

        escorpioescorpio = cb.signo_es_compatible(escorpio, escorpio)
        print('verificando si los signos escorpio y escorpio son compatiples ----------------------------- ❌ ', end='')
        self.assertEqual(escorpioescorpio, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos escorpio y escorpio son compatiples ----------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario escorpio y sagitario

        escorpiosagitario = cb.signo_es_compatible(escorpio, sagitario)
        print('verificando si los signos escorpio y sagitario son compatiples ---------------------------- ❌ ', end='')
        self.assertEqual(escorpiosagitario, False, 'La función determinó erradamente que eran compatibles')
        print(
            '\rVerificando si los signos escorpio y sagitario son compatiples ---------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario escorpio y capricornio

        escorpiocapricornio = cb.signo_es_compatible(escorpio, capricornio)
        print(
            'verificando si los signos escorpio y capricornio son compatiples -------------------------- ❌ ', end='')
        self.assertEqual(escorpiocapricornio, False, 'La función determinó erradamente que eran compatibles')
        print(
            '\rVerificando si los signos escorpio y capricornio son compatiples -------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario escorpio y acuario

        escorpioacuario = cb.signo_es_compatible(escorpio, acuario)
        print('verificando si los signos escorpio y acuario son compatiples ------------------------------ ❌ ', end='')
        self.assertEqual(escorpioacuario, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos escorpio y acuario son compatiples ------------------------------ ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario escorpio y piscis

        escorpiopiscis = cb.signo_es_compatible(escorpio, piscis)
        print('verificando si los signos escorpio y piscis son compatiples ------------------------------- ❌ ', end='')
        self.assertEqual(escorpiopiscis, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos escorpio y piscis son compatiples ------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario sagitario y aries

        sagitarioaries = cb.signo_es_compatible(sagitario, aries)
        print('verificando si los signos sagitario y aries son compatiples ------------------------------- ❌ ', end='')
        self.assertEqual(sagitarioaries, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos sagitario y aries son compatiples ------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario sagitario y tauro

        sagitariotauro = cb.signo_es_compatible(sagitario, tauro)
        print('verificando si los signos sagitario y tauro son compatiples ------------------------------- ❌ ', end='')
        self.assertEqual(sagitariotauro, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos sagitario y tauro son compatiples ------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario sagitario y geminis

        sagitariogeminis = cb.signo_es_compatible(sagitario, geminis)
        print('verificando si los signos sagitario y geminis son compatiples ----------------------------- ❌ ', end='')
        self.assertEqual(sagitariogeminis, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos sagitario y geminis son compatiples ----------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario sagitario y cancer

        sagitariocancer = cb.signo_es_compatible(sagitario, cancer)
        print('verificando si los signos sagitario y cancer son compatiples ------------------------------ ❌ ', end='')
        self.assertEqual(sagitariocancer, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos sagitario y cancer son compatiples ------------------------------ ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario sagitario y leo

        sagitarioleo = cb.signo_es_compatible(sagitario, leo)
        print('verificando si los signos sagitario y leo son compatiples --------------------------------- ❌ ', end='')
        self.assertEqual(sagitarioleo, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos sagitario y leo son compatiples --------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario sagitario y virgo

        sagitariovirgo = cb.signo_es_compatible(sagitario, virgo)
        print('verificando si los signos sagitario y virgo son compatiples ------------------------------- ❌ ', end='')
        self.assertEqual(sagitariovirgo, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos sagitario y virgo son compatiples ------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario sagitario y libra

        sagitariolibra = cb.signo_es_compatible(sagitario, libra)
        print('verificando si los signos sagitario y libra son compatiples ------------------------------- ❌ ', end='')
        self.assertEqual(sagitariolibra, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos sagitario y libra son compatiples ------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario sagitario y escorpio

        sagitarioescorpio = cb.signo_es_compatible(sagitario, escorpio)
        print('verificando si los signos sagitario y escorpio son compatiples ---------------------------- ❌ ', end='')
        self.assertEqual(sagitarioescorpio, False, 'La función determinó erradamente que eran compatibles')
        print(
            '\rVerificando si los signos sagitario y escorpio son compatiples ---------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario sagitario y sagitario

        sagitariosagitario = cb.signo_es_compatible(sagitario, sagitario)
        print('verificando si los signos sagitario y sagitario son compatiples --------------------------- ❌ ', end='')
        self.assertEqual(sagitariosagitario, True, 'La función determinó erradamente que eran compatibles')
        print(
            '\rVerificando si los signos sagitario y sagitario son compatiples --------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario sagitario y capricornio

        sagitariocapricornio = cb.signo_es_compatible(sagitario, capricornio)
        print(
            'verificando si los signos sagitario y capricornio son compatiples ------------------------- ❌ ', end='')
        self.assertEqual(sagitariocapricornio, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos sagitario y capricornio son compatiples ------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario sagitario y acuario

        sagitarioacuario = cb.signo_es_compatible(sagitario, acuario)
        print('verificando si los signos sagitario y acuario son compatiples ----------------------------- ❌ ', end='')
        self.assertEqual(sagitarioacuario, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos sagitario y acuario son compatiples ----------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario sagitario y piscis

        sagitariopiscis = cb.signo_es_compatible(sagitario, piscis)
        print('verificando si los signos sagitario y piscis son compatiples ------------------------------ ❌ ', end='')
        self.assertEqual(sagitariopiscis, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos sagitario y piscis son compatiples ------------------------------ ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario capricornio y aries

        capricornioaries = cb.signo_es_compatible(capricornio, aries)
        print('verificando si los signos capricornio y aries son compatiples ----------------------------- ❌ ', end='')
        self.assertEqual(capricornioaries, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos capricornio y aries son compatiples ----------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario capricornio y tauro

        capricorniotauro = cb.signo_es_compatible(capricornio, tauro)
        print('verificando si los signos capricornio y tauro son compatiples ----------------------------- ❌ ', end='')
        self.assertEqual(capricorniotauro, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos capricornio y tauro son compatiples ----------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario capricornio y geminis

        capricorniogeminis = cb.signo_es_compatible(capricornio, geminis)
        print('verificando si los signos capricornio y geminis son compatiples --------------------------- ❌ ', end='')
        self.assertEqual(capricorniogeminis, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos capricornio y geminis son compatiples --------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario capricornio y cancer

        capricorniocancer = cb.signo_es_compatible(capricornio, cancer)
        print('verificando si los signos capricornio y cancer son compatiples ---------------------------- ❌ ', end='')
        self.assertEqual(capricorniocancer, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos capricornio y cancer son compatiples ---------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario capricornio y leo

        capricornioleo = cb.signo_es_compatible(capricornio, leo)
        print('verificando si los signos capricornio y leo son compatiples ------------------------------- ❌ ', end='')
        self.assertEqual(capricornioleo, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos capricornio y leo son compatiples ------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario capricornio y virgo

        capricorniovirgo = cb.signo_es_compatible(capricornio, virgo)
        print('verificando si los signos capricornio y virgo son compatiples ----------------------------- ❌ ', end='')
        self.assertEqual(capricorniovirgo, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos capricornio y virgo son compatiples ----------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario capricornio y libra

        capricorniolibra = cb.signo_es_compatible(capricornio, libra)
        print('verificando si los signos capricornio y libra son compatiples ----------------------------- ❌ ', end='')
        self.assertEqual(capricorniolibra, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos capricornio y libra son compatiples ----------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario capricornio y escorpio

        capricornioescorpio = cb.signo_es_compatible(capricornio, escorpio)
        print('verificando si los signos capricornio y escorpio son compatiples ------------------------- ❌ ', end='')
        self.assertEqual(capricornioescorpio, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos capricornio y escorpio son compatiples -------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario capricornio y sagitario

        capricorniosagitario = cb.signo_es_compatible(capricornio, sagitario)
        print('verificando si los signos capricornio y sagitario son compatiples ------------------------- ❌ ', end='')
        self.assertEqual(capricorniosagitario, False, 'La función determinó erradamente que eran compatibles')
        print(
            '\rVerificando si los signos capricornio y sagitario son compatiples ------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario capricornio y capricornio

        capricorniocapricornio = cb.signo_es_compatible(capricornio, capricornio)
        print('verificando si los signos capricornio y capricornio son compatiples ----------------------- ❌ ', end='')
        self.assertEqual(capricorniocapricornio, False, 'La función determinó erradamente que eran compatibles')
        print(
            '\rVerificando si los signos capricornio y capricornio son compatiples ----------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario capricornio y acuario

        capricornioacuario = cb.signo_es_compatible(capricornio, acuario)
        print('verificando si los signos capricornio y acuario son compatiples --------------------------- ❌ ', end='')
        self.assertEqual(capricornioacuario, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos capricornio y acuario son compatiples --------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario capricornio y piscis

        capricorniopiscis = cb.signo_es_compatible(capricornio, piscis)
        print('verificando si los signos capricornio y piscis son compatiples ---------------------------- ❌ ', end='')
        self.assertEqual(capricorniopiscis, True, 'La función determinó erradamente que eran compatibles')
        print(
            '\rVerificando si los signos capricornio y piscis son compatiples ---------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario acuario y aries

        acuarioaries = cb.signo_es_compatible(acuario, aries)
        print('verificando si los signos acuario y aries son compatiples --------------------------------- ❌ ', end='')
        self.assertEqual(acuarioaries, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos acuario y aries son compatiples --------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario acuario y tauro

        acuariotauro = cb.signo_es_compatible(acuario, tauro)
        print('verificando si los signos acuario y tauro son compatiples --------------------------------- ❌ ', end='')
        self.assertEqual(acuariotauro, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos acuario y tauro son compatiples --------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario acuario y geminis

        acuariogeminis = cb.signo_es_compatible(acuario, geminis)
        print('verificando si los signos acuario y geminis son compatiples ------------------------------- ❌ ', end='')
        self.assertEqual(acuariogeminis, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos acuario y geminis son compatiples ------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario acuario y cancer

        acuariocancer = cb.signo_es_compatible(acuario, cancer)
        print('verificando si los signos acuario y cancer son compatiples -------------------------------- ❌ ', end='')
        self.assertEqual(acuariocancer, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos acuario y cancer son compatiples -------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario acuario y leo

        acuarioleo = cb.signo_es_compatible(acuario, leo)
        print('verificando si los signos acuario y leo son compatiples ----------------------------------- ❌ ', end='')
        self.assertEqual(acuarioleo, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos acuario y leo son compatiples ----------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario acuario y virgo

        acuariovirgo = cb.signo_es_compatible(acuario, virgo)
        print('verificando si los signos acuario y virgo son compatiples --------------------------------- ❌ ', end='')
        self.assertEqual(acuariovirgo, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos acuario y virgo son compatiples --------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario acuario y libra

        acuariolibra = cb.signo_es_compatible(acuario, libra)
        print('verificando si los signos acuario y libra son compatiples --------------------------------- ❌ ', end='')
        self.assertEqual(acuariolibra, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos acuario y libra son compatiples --------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario acuario y escorpio

        acuarioescorpio = cb.signo_es_compatible(acuario, escorpio)
        print('verificando si los signos acuario y escorpio son compatiples ------------------------------ ❌ ', end='')
        self.assertEqual(acuarioescorpio, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos acuario y escorpio son compatiples ------------------------------ ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario acuario y sagitario

        acuariosagitario = cb.signo_es_compatible(acuario, sagitario)
        print('verificando si los signos acuario y sagitario son compatiples ----------------------------- ❌ ', end='')
        self.assertEqual(acuariosagitario, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos acuario y sagitario son compatiples ----------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario acuario y capricornio

        acuariocapricornio = cb.signo_es_compatible(acuario, capricornio)
        print('verificando si los signos acuario y capricornio son compatiples --------------------------- ❌ ', end='')
        self.assertEqual(acuariocapricornio, False, 'La función determinó erradamente que eran compatibles')
        print(
            '\rVerificando si los signos acuario y capricornio son compatiples --------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario acuario y acuario

        acuarioacuario = cb.signo_es_compatible(acuario, acuario)
        print('verificando si los signos acuario y acuario son compatiples ------------------------------- ❌ ', end='')
        self.assertEqual(acuarioacuario, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos acuario y acuario son compatiples ------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario acuario y piscis

        acuariopiscis = cb.signo_es_compatible(acuario, piscis)
        print('verificando si los signos acuario y piscis son compatiples -------------------------------- ❌ ', end='')
        self.assertEqual(acuariopiscis, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos acuario y piscis son compatiples -------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario piscis y aries

        piscisaries = cb.signo_es_compatible(piscis, aries)
        print('verificando si los signos piscis y aries son compatiples ---------------------------------- ❌ ', end='')
        self.assertEqual(piscisaries, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos piscis y aries son compatiples ---------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario piscis y tauro

        piscistauro = cb.signo_es_compatible(piscis, tauro)
        print('verificando si los signos piscis y tauro son compatiples ---------------------------------- ❌ ', end='')
        self.assertEqual(piscistauro, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos piscis y tauro son compatiples ---------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario piscis y geminis

        piscisgeminis = cb.signo_es_compatible(piscis, geminis)
        print('verificando si los signos piscis y geminis son compatiples -------------------------------- ❌ ', end='')
        self.assertEqual(piscisgeminis, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos piscis y geminis son compatiples -------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario piscis y cancer

        pisciscancer = cb.signo_es_compatible(piscis, cancer)
        print('verificando si los signos piscis y cancer son compatiples --------------------------------- ❌ ', end='')
        self.assertEqual(pisciscancer, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos piscis y cancer son compatiples --------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario piscis y leo

        piscisleo = cb.signo_es_compatible(piscis, leo)
        print('verificando si los signos piscis y leo son compatiples ------------------------------------ ❌ ', end='')
        self.assertEqual(piscisleo, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos piscis y leo son compatiples ------------------------------------ ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario piscis y virgo

        piscisvirgo = cb.signo_es_compatible(piscis, virgo)
        print('verificando si los signos piscis y virgo son compatiples ---------------------------------- ❌ ', end='')
        self.assertEqual(piscisvirgo, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos piscis y virgo son compatiples ---------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario piscis y libra

        piscislibra = cb.signo_es_compatible(piscis, libra)
        print('verificando si los signos piscis y libra son compatiples ---------------------------------- ❌ ', end='')
        self.assertEqual(piscislibra, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos piscis y libra son compatiples ---------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario piscis y escorpio

        piscisescorpio = cb.signo_es_compatible(piscis, escorpio)
        print('verificando si los signos piscis y escorpio son compatiples ------------------------------- ❌ ', end='')
        self.assertEqual(piscisescorpio, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos piscis y escorpio son compatiples ------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario piscis y sagitario

        piscissagitario = cb.signo_es_compatible(piscis, sagitario)
        print('verificando si los signos piscis y sagitario son compatiples ------------------------------ ❌ ', end='')
        self.assertEqual(piscissagitario, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos piscis y sagitario son compatiples ------------------------------ ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario piscis y capricornio

        pisciscapricornio = cb.signo_es_compatible(piscis, capricornio)
        print('verificando si los signos piscis y capricornio son compatiples ---------------------------- ❌ ', end='')
        self.assertEqual(pisciscapricornio, True, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos piscis y capricornio son compatiples ---------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario piscis y acuario

        piscisacuario = cb.signo_es_compatible(piscis, acuario)
        print('verificando si los signos piscis y acuario son compatiples -------------------------------- ❌ ', end='')
        self.assertEqual(piscisacuario, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos piscis y acuario son compatiples -------------------------------- ✅ ')
        test += 1
        # --------------------------------------------------------------------------------------------------------------
        # Escenario piscis y piscis

        piscispiscis = cb.signo_es_compatible(piscis, piscis)
        print('verificando si los signos piscis y piscis son compatiples --------------------------------- ❌ ', end='')
        self.assertEqual(piscispiscis, False, 'La función determinó erradamente que eran compatibles')
        print('\rVerificando si los signos piscis y piscis son compatiples --------------------------------- ✅ ')
        test += 1

    def test_usuario_mas_compatibilidad(self):
        print()
        print(
            "################### Test usuario_mas_compatibilidad #####################################################")

        global test

        amigo_con_puntaje0 = {'amigos_en_comun': 5, 'bloqueado': False, "genero_musical_favorito": "rock",
                              "genero_literario_favorito": "lírico"}
        amigo_con_puntajem10 = {'amigos_en_comun': 0, 'bloqueado': True, "genero_musical_favorito": "rock",
                                "genero_literario_favorito": "Terror"}
        amigo_con_puntaje2 = {'amigos_en_comun': 0, 'bloqueado': False, "genero_musical_favorito": "pop",
                              "genero_literario_favorito": "Terror"}
        amigo_con_puntaje7 = {'amigos_en_comun': 6, 'bloqueado': False, "genero_musical_favorito": "salsa",
                              "genero_literario_favorito": "drama"}

        mas_compatible_en_1 = cb.usuario_mas_compatibilidad(amigo_con_puntaje7, amigo_con_puntaje0,
                                                            amigo_con_puntajem10,
                                                            amigo_con_puntaje2)

        print("Verificando la busqueda del amigo en la posicion 1 ---------------------------------------- ❌", end='')
        self.assertEqual(mas_compatible_en_1, amigo_con_puntaje7, "La función no calculó correctamente el puntaje o no encontró el mayor")
        print("\rVerificando la busqueda del amigo en la posicion 1 ---------------------------------------- ✅")
        test += 1

        mas_compatible_en_2 = cb.usuario_mas_compatibilidad(amigo_con_puntaje0, amigo_con_puntaje7,
                                                            amigo_con_puntajem10,
                                                            amigo_con_puntaje2)

        print("Verificando la busqueda del amigo en la posicion 2 ---------------------------------------- ❌", end='')
        self.assertEqual(mas_compatible_en_2, amigo_con_puntaje7, "La función no calculó correctamente el puntaje o no encontró el mayor")
        print("\rVerificando la busqueda del amigo en la posicion 2 ---------------------------------------- ✅")
        test += 1

        mas_compatible_en_3 = cb.usuario_mas_compatibilidad(amigo_con_puntajem10, amigo_con_puntaje0,
                                                            amigo_con_puntaje7,
                                                            amigo_con_puntaje2)

        print("Verificando la busqueda del amigo en la posicion 3 ---------------------------------------- ❌", end='')
        self.assertEqual(mas_compatible_en_3, amigo_con_puntaje7, "La función no calculó correctamente el puntaje o no encontró el mayor")
        print("\rVerificando la busqueda del amigo en la posicion 3 ---------------------------------------- ✅")
        test += 1

        mas_compatible_en_4 = cb.usuario_mas_compatibilidad(amigo_con_puntaje2, amigo_con_puntaje0,
                                                            amigo_con_puntajem10,
                                                            amigo_con_puntaje7)

        print("Verificando la busqueda del amigo en la posicion 4 ---------------------------------------- ❌", end='')
        self.assertEqual(mas_compatible_en_4, amigo_con_puntaje7, "La función no calculó correctamente el puntaje o no encontró el mayor")
        print("\rVerificando la busqueda del amigo en la posicion 4 ---------------------------------------- ✅")
        test += 1

    def test_contar_usuarios_con_generos(self):
        print()
        print(
            "################### Test contar_usuarios_con_generos ####################################################")

        global test

        amigo1 = {"genero_musical_favorito": "rock", "genero_literario_favorito": "lírico"}
        amigo2 = {"genero_musical_favorito": "rock", "genero_literario_favorito": "lírico"}
        amigo3 = {"genero_musical_favorito": "rock", "genero_literario_favorito": "lírico"}
        amigo4 = {"genero_musical_favorito": "rock", "genero_literario_favorito": "lírico"}

        conteo4 = cb.contar_usuarios_con_generos(amigo1, amigo2, amigo3, amigo4, "rock", "lírico")
        conteo0 = cb.contar_usuarios_con_generos(amigo1, amigo2, amigo3, amigo4, "pop", "drama")

        print("Verificando la suma de todos los amigos con el mismo genero musical y literario ----------- ❌", end='')
        self.assertEqual(conteo4, 4, "La función no calculó correctamente el conteo")
        print("\rVerificando la suma de todos los amigos con el mismo genero musical y literario ----------- ✅")
        test += 1

        print("Verificando la suma de todos los amigos con el diferente genero musical y literario ------- ❌", end='')
        self.assertEqual(conteo0, 0, "La función no calculó correctamente el conteo")
        print("\rVerificando la suma de todos los amigos con el diferente genero musical y literario ------- ✅")
        test += 1


if __name__ == '__main__':
    unittest.main()


def print_percent_done(index, total, bar_len=202):
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
    print_percent_done(test, 202)
