# -*- coding: utf-8 -*-
"""
Copyright 2023 Juan Lugo Sánchez - jd.lugo@uniandes.edu.co
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
 * 28 de Febrero de 2023
 *
 * @author Juan Lugo Sánchez
 * jd.lugo@uniandes.edu.co
 * 201913094
"""
import unittest
import modulo_peliculas as mod

test = 0

class TestPeliculas(unittest.TestCase):

    def test_crear_pelicula(self):
        print()
        print(
            "################### Test crear_pelicula #####################################################################")

        global test

        pelicula_funcion = mod.crear_pelicula("El Gato con botas",  "Familiar, Comedia", 92, 2001, 'Todos', 1700, "Viernes")
        pelicula = {'nombre': 'El Gato con botas', 'genero': 'Familiar, Comedia', 'duracion': 92, 'anio': 2001, 
                    'clasificacion': 'Todos', 'hora': 1700, 'dia': 'Viernes'}

        print("Verificando la creacion de una pelicula ------------------------------------------------------- ❌", end='')
        self.assertEqual(pelicula_funcion, pelicula, "El diccionario creado no corresponde con los valores dados por "
                                               "parametro; revisar los elementos que tienen + y - para determinar "
                                               "que valores son diferentes")
        print("\rVerificando la creacion de una pelicula ------------------------------------------------------- ✅")
        test += 1

    def test_encontrar_pelicula(self):
        print()
        print(
            "################### Test encontrar_pelicula #################################################################")

        global test

        p1 = {'nombre': 'El Gato con botas'}
        p2 = {'nombre': 'Destino Final'}
        p3 = {'nombre': 'Pinocho'}
        p4 = {'nombre': 'El origen'}
        p5 = {'nombre': 'Severance'}

        print("Verificando la busqueda de la pelicula en la posicion 1 --------------------------------------- ❌", end='')
        p_en_p1 = mod.encontrar_pelicula("El Gato con botas", p1, p2, p3, p4, p5)
        self.assertEqual(p1, p_en_p1, "La función no pudo encontrar el diccionario buscado en la posicion 1")
        print("\rVerificando la busqueda de la pelicula en la posicion 1 --------------------------------------- ✅")
        test += 1

        print("Verificando la busqueda de la pelicula en la posicion 2 --------------------------------------- ❌", end='')
        p_en_p2 = mod.encontrar_pelicula("Destino Final", p1, p2, p3, p4, p5)
        self.assertEqual(p2, p_en_p2, "La función no pudo encontrar el diccionario buscado en la posicion 2")
        print("\rVerificando la busqueda de la pelicula en la posicion 2 --------------------------------------- ✅")
        test += 1

        print("Verificando la busqueda de la pelicula en la posicion 3 --------------------------------------- ❌", end='')
        p_en_p3 = mod.encontrar_pelicula("Pinocho", p1, p2, p3, p4, p5)
        self.assertEqual(p3, p_en_p3, "La función no pudo encontrar el diccionario buscado en la posicion 3")
        print("\rVerificando la busqueda de la pelicula en la posicion 3 --------------------------------------- ✅")
        test += 1

        print("Verificando la busqueda de la pelicula en la posicion 4 --------------------------------------- ❌", end='')
        p_en_p4 = mod.encontrar_pelicula("El origen", p1, p2, p3, p4, p5)
        self.assertEqual(p4, p_en_p4, "La función no pudo encontrar el diccionario buscado en la posicion 4")
        print("\rVerificando la busqueda de la pelicula en la posicion 4 --------------------------------------- ✅")
        test += 1

        print("Verificando la busqueda de la pelicula en la posicion 5 --------------------------------------- ❌", end='')
        p_en_p5 = mod.encontrar_pelicula("Severance", p1, p2, p3, p4, p5)
        self.assertEqual(p5, p_en_p5, "La función no pudo encontrar el diccionario buscado en la posicion 5")
        print("\rVerificando la busqueda de la pelicula en la posicion 5 --------------------------------------- ✅")
        test += 1

        print("Verificando la busqueda de la pelicula que no exisiste ---------------------------------------- ❌", end='')
        p_en_p5 = mod.encontrar_pelicula("El aro", p1, p2, p3, p4, p5)
        self.assertIsNone(p_en_p5, "El programa encontró una pelicula que no existe")
        print("\rVerificando la busqueda de la pelicula que no exisiste ---------------------------------------- ✅")
        test += 1

    def test_encontrar_pelicula_mas_larga(self):
        print()
        print(
            "################### Test encontrar_pelicula_mas_larga #######################################################")

        global test

        p1 = {'duracion': 99}
        p2 = {'duracion': 12}
        p3 = {'duracion': 165}
        p4 = {'duracion': 30}
        p5 = {'duracion': 120}

        print("Verificando la busqueda de la pelicula más larga en la posicion 1 ----------------------------- ❌", end='')
        p_en_p1 = mod.encontrar_pelicula_mas_larga(p3, p2, p1, p4, p5)
        self.assertEqual(p3, p_en_p1, "La función no pudo encontrar la pelicula más larga en la posicion 1")
        print("\rVerificando la busqueda de la pelicula más larga en la posicion 1 ----------------------------- ✅")
        test += 1

        print("Verificando la busqueda de la pelicula más larga en la posicion 2 ----------------------------- ❌", end='')
        p_en_p2 = mod.encontrar_pelicula_mas_larga(p1, p3, p2, p4, p5)
        self.assertEqual(p3, p_en_p2, "La función no pudo encontrar la pelicula más larga en la posicion 2")
        print("\rVerificando la busqueda de la pelicula más larga en la posicion 2 ----------------------------- ✅")
        test += 1

        print("Verificando la busqueda de la pelicula más larga en la posicion 3 ----------------------------- ❌", end='')
        p_en_p3 = mod.encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
        self.assertEqual(p3, p_en_p3, "La función no pudo encontrar la pelicula más larga en la posicion 3")
        print("\rVerificando la busqueda de la pelicula más larga en la posicion 3 ----------------------------- ✅")
        test += 1

        print("Verificando la busqueda de la pelicula más larga en la posicion 4 ----------------------------- ❌", end='')
        p_en_p4 = mod.encontrar_pelicula_mas_larga(p1, p2, p4, p3, p5)
        self.assertEqual(p3, p_en_p4, "La función no pudo encontrar la pelicula más larga en la posicion 4")
        print("\rVerificando la busqueda de la pelicula más larga en la posicion 4 ----------------------------- ✅")
        test += 1

        print("Verificando la busqueda de la pelicula más larga en la posicion 5 ----------------------------- ❌", end='')
        p_en_p5 = mod.encontrar_pelicula_mas_larga(p1, p2, p5, p4, p3)
        self.assertEqual(p3, p_en_p5, "La función no pudo encontrar la pelicula más larga en la posicion 5")
        print("\rVerificando la busqueda de la pelicula más larga en la posicion 5 ----------------------------- ✅")
        test += 1


    def test_duracion_promedio_peliculas(self):
        print()
        print(
            "################### Test duracion_promedio_peliculas #######################################################")

        global test

        p1 = {'duracion': 50}
        p2 = {'duracion': 12}
        p3 = {'duracion': 40}
        p4 = {'duracion': 30}
        p5 = {'duracion': 22}

        print("Verificando la duración promedio de menos de 60 min ------------------------------------------- ❌", end='')
        dur_men_60 = mod.duracion_promedio_peliculas(p3, p2, p1, p4, p5)
        self.assertEqual("00:30", dur_men_60, "La función no calculó correctamente la duracion en HH:MM")
        print("\rVerificando la duración promedio de menos de 60 min ------------------------------------------- ✅")
        test += 1

        p1 = {'duracion': 61}
        p2 = {'duracion': 59}
        p3 = {'duracion': 61}
        p4 = {'duracion': 59}
        p5 = {'duracion': 60}

        print("Verificando la duración promedio de 60 min ---------------------------------------------------- ❌", end='')
        dur_60 = mod.duracion_promedio_peliculas(p1, p3, p2, p4, p5)
        self.assertEqual("01:00", dur_60, "La función no calculó correctamente la duracion en HH:MM")
        print("\rVerificando la duración promedio de 60 min ---------------------------------------------------- ✅")
        test += 1

        p1 = {'duracion': 150}
        p2 = {'duracion': 170}
        p3 = {'duracion': 160}
        p4 = {'duracion': 150}
        p5 = {'duracion': 170}

        print("Verificando la duración promedio de 160 min --------------------------------------------------- ❌", end='')
        dur_160 = mod.duracion_promedio_peliculas(p1, p2, p3, p4, p5)
        self.assertEqual("02:40", dur_160, "La función no calculó correctamente la duracion en HH:MM")
        print("\rVerificando la duración promedio de 160 min --------------------------------------------------- ✅")
        test += 1

    def test_duracion_promedio_peliculas(self):
        print()
        print(
            "################### Test duracion_promedio_peliculas ########################################################")

        global test

        p1 = {'duracion': 50}
        p2 = {'duracion': 12}
        p3 = {'duracion': 40}
        p4 = {'duracion': 30}
        p5 = {'duracion': 22}

        print("Verificando la duración promedio de menos de 60 min ------------------------------------------- ❌", end='')
        dur_men_60 = mod.duracion_promedio_peliculas(p3, p2, p1, p4, p5)
        self.assertEqual("00:30", dur_men_60, "La función no calculó correctamente la duracion en HH:MM")
        print("\rVerificando la duración promedio de menos de 60 min ------------------------------------------- ✅")
        test += 1

        p1 = {'duracion': 61}
        p2 = {'duracion': 59}
        p3 = {'duracion': 61}
        p4 = {'duracion': 59}
        p5 = {'duracion': 60}

        print("Verificando la duración promedio de 60 min ---------------------------------------------------- ❌", end='')
        dur_60 = mod.duracion_promedio_peliculas(p1, p3, p2, p4, p5)
        self.assertEqual("01:00", dur_60, "La función no calculó correctamente la duracion en HH:MM")
        print("\rVerificando la duración promedio de 60 min ---------------------------------------------------- ✅")
        test += 1

        p1 = {'duracion': 150}
        p2 = {'duracion': 170}
        p3 = {'duracion': 160}
        p4 = {'duracion': 150}
        p5 = {'duracion': 170}

        print("Verificando la duración promedio de 160 min --------------------------------------------------- ❌", end='')
        dur_160 = mod.duracion_promedio_peliculas(p1, p2, p3, p4, p5)
        self.assertEqual("02:40", dur_160, "La función no calculó correctamente la duracion en HH:MM")
        print("\rVerificando la duración promedio de 160 min --------------------------------------------------- ✅")
        test += 1

    def test_encontrar_estrenos(self):
        print()
        print(
            "################### Test encontrar_estrenos #################################################################")

        global test

        p1 = {'nombre': 'El Gato con botas', 'anio': 2019}
        p2 = {'nombre': 'Destino Final', 'anio': 2018}
        p3 = {'nombre': 'Pinocho', 'anio': 2018}
        p4 = {'nombre': 'El origen', 'anio': 2018}
        p5 = {'nombre': 'Severance', 'anio': 2018}

        print("Verificando el estreno de la primera pelicula únicamente ------------------------------------- ❌", end='')
        primer_peli = mod.encontrar_estrenos(p1, p2, p3, p4, p5, 2018)
        self.assertEqual("El Gato con botas", primer_peli, "La función no determinó correctamente que únicamente la primera pelicula hacia parte los estrenos o no devuelve la respuesta en el formato esperado.")
        print("\rVerificando el estreno de la primera pelicula únicamente -------------------------------------- ✅")
        test += 1

        p1 = {'nombre': 'El Gato con botas', 'anio': 2018}
        p2 = {'nombre': 'Destino Final', 'anio': 2019}
        p3 = {'nombre': 'Pinocho', 'anio': 2018}
        p4 = {'nombre': 'El origen', 'anio': 2018}
        p5 = {'nombre': 'Severance', 'anio': 2018}

        print("Verificando el estreno de la segunda pelicula únicamente ------------------------------------- ❌", end='')
        segund_peli = mod.encontrar_estrenos(p1, p2, p3, p4, p5, 2018)
        self.assertEqual("Destino Final", segund_peli, "La función no determinó correctamente que únicamente la segunda pelicula hacia parte los estrenos o no devuelve la respuesta en el formato esperado.")
        print("\rVerificando el estreno de la segunda pelicula únicamente -------------------------------------- ✅")
        test += 1

        p1 = {'nombre': 'El Gato con botas', 'anio': 2018}
        p2 = {'nombre': 'Destino Final', 'anio': 2018}
        p3 = {'nombre': 'Pinocho', 'anio': 2019}
        p4 = {'nombre': 'El origen', 'anio': 2018}
        p5 = {'nombre': 'Severance', 'anio': 2018}

        print("Verificando el estreno de la tercera pelicula únicamente ------------------------------------- ❌", end='')
        tercer_peli = mod.encontrar_estrenos(p1, p2, p3, p4, p5, 2018)
        self.assertEqual("Pinocho", tercer_peli, "La función no determinó correctamente que únicamente la primera tercera hacia parte los estrenos o no devuelve la respuesta en el formato esperado.")
        print("\rVerificando el estreno de la tercera pelicula únicamente -------------------------------------- ✅")
        test += 1

        p1 = {'nombre': 'El Gato con botas', 'anio': 2018}
        p2 = {'nombre': 'Destino Final', 'anio': 2018}
        p3 = {'nombre': 'Pinocho', 'anio': 2018}
        p4 = {'nombre': 'El origen', 'anio': 2019}
        p5 = {'nombre': 'Severance', 'anio': 2018}

        print("Verificando el estreno de la cuarta pelicula únicamente -------------------------------------- ❌", end='')
        cuarta_peli = mod.encontrar_estrenos(p1, p2, p3, p4, p5, 2018)
        self.assertEqual("El origen", cuarta_peli, "La función no determinó correctamente que únicamente la cuarta pelicula hacia parte los estrenos o no devuelve la respuesta en el formato esperado.")
        print("\rVerificando el estreno de la cuarta pelicula únicamente --------------------------------------- ✅")
        test += 1

        p1 = {'nombre': 'El Gato con botas', 'anio': 2018}
        p2 = {'nombre': 'Destino Final', 'anio': 2018}
        p3 = {'nombre': 'Pinocho', 'anio': 2018}
        p4 = {'nombre': 'El origen', 'anio': 2018}
        p5 = {'nombre': 'Severance', 'anio': 2019}

        print("Verificando el estreno de la quinta pelicula únicamente -------------------------------------- ❌", end='')
        quinta_peli = mod.encontrar_estrenos(p1, p2, p3, p4, p5, 2018)
        self.assertEqual("Severance", quinta_peli, "La función no determinó correctamente que únicamente la primera quinta hacia parte los estrenos o no devuelve la respuesta en el formato esperado.")
        print("\rVerificando el estreno de la quinta pelicula únicamente --------------------------------------- ✅")
        test += 1

        p1 = {'nombre': 'El Gato con botas', 'anio': 2019}
        p2 = {'nombre': 'Destino Final', 'anio': 2018}
        p3 = {'nombre': 'Pinocho', 'anio': 2019}
        p4 = {'nombre': 'El origen', 'anio': 2018}
        p5 = {'nombre': 'Severance', 'anio': 2018}

        print("Verificando el estreno de la primera y tercera pelicula únicamente --------------------------- ❌", end='')
        pyt_peli = mod.encontrar_estrenos(p1, p2, p3, p4, p5, 2018)
        self.assertEqual("El Gato con botas, Pinocho", pyt_peli, "La función no determinó correctamente que únicamente la primera y tercera pelicula hacia parte los estrenos o no devuelve la respuesta en el formato esperado.")
        print("\rVerificando el estreno de la primera y tercera pelicula únicamente ---------------------------- ✅")
        test += 1

        p1 = {'nombre': 'El Gato con botas', 'anio': 2018}
        p2 = {'nombre': 'Destino Final', 'anio': 2019}
        p3 = {'nombre': 'Pinocho', 'anio': 2018}
        p4 = {'nombre': 'El origen', 'anio': 2019}
        p5 = {'nombre': 'Severance', 'anio': 2018}

        print("Verificando el estreno de la segunda y cuarta pelicula únicamente ---------------------------- ❌", end='')
        syc_peli = mod.encontrar_estrenos(p1, p2, p3, p4, p5, 2018)
        self.assertEqual("Destino Final, El origen", syc_peli, "La función no determinó correctamente que únicamente la segunda y cuarta pelicula hacia parte los estrenos o no devuelve la respuesta en el formato esperado.")
        print("\rVerificando el estreno de la segunda y cuarta pelicula únicamente ----------------------------- ✅")
        test += 1

        p1 = {'nombre': 'El Gato con botas', 'anio': 2019}
        p2 = {'nombre': 'Destino Final', 'anio': 2019}
        p3 = {'nombre': 'Pinocho', 'anio': 2019}
        p4 = {'nombre': 'El origen', 'anio': 2019}
        p5 = {'nombre': 'Severance', 'anio': 2019}

        print("Verificando el estreno todas las peliculas --------------------------------------------------- ❌", end='')
        todas = mod.encontrar_estrenos(p1, p2, p3, p4, p5, 2018)
        self.assertEqual("El Gato con botas, Destino Final, Pinocho, El origen, Severance", todas, "La función no determinó correctamente que todas las peliculas hacia parte los estrenos o no devuelve la respuesta en el formato esperado.")
        print("\rVerificando el estreno todas las peliculas ---------------------------------------------------- ✅")
        test += 1

        p1 = {'nombre': 'El Gato con botas', 'anio': 2018}
        p2 = {'nombre': 'Destino Final', 'anio': 2018}
        p3 = {'nombre': 'Pinocho', 'anio': 2018}
        p4 = {'nombre': 'El origen', 'anio': 2018}
        p5 = {'nombre': 'Severance', 'anio': 2018}

        print("Verificando el estreno ninguna de las peliculas ---------------------------------------------- ❌", end='')
        ninguna = mod.encontrar_estrenos(p1, p2, p3, p4, p5, 2018)
        self.assertEqual("Ninguna", ninguna, "La función no determinó correctamente que únicamente la ninguna de las peliculas hacia parte los estrenos o no devuelve la respuesta en el formato esperado.")
        print("\rVerificando el estreno ninguna de las peliculas ----------------------------------------------- ✅")
        test += 1

    def test_cuantas_peliculas_18_mas(self):
        print()
        print(
            "################### Test cuantas_peliculas_18_mas ###########################################################")

        global test

        p1 = {'clasificacion': '18+'}
        p2 = {'clasificacion': '7+'}
        p3 = {'clasificacion': '7+'}
        p4 = {'clasificacion': '7+'}
        p5 = {'clasificacion': '7+'}

        print("Verificando la clasificación de la primera pelicula únicamente ------------------------------- ❌", end='')
        primer_peli = mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
        self.assertEqual(1, primer_peli, "La función no calculó correctamente el numero de peliculas 18+.")
        print("\rVerificando la clasificación de la primera pelicula únicamente -------------------------------- ✅")
        test += 1

        p1 = {'clasificacion': '7+'}
        p2 = {'clasificacion': '18+'}
        p3 = {'clasificacion': '7+'}
        p4 = {'clasificacion': '7+'}
        p5 = {'clasificacion': '7+'}

        print("Verificando la clasificación de la segunda pelicula únicamente ------------------------------- ❌", end='')
        segund_peli = mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
        self.assertEqual(1, segund_peli, "La función no calculó correctamente el numero de peliculas 18+.")
        print("\rVerificando la clasificación de la segunda pelicula únicamente -------------------------------- ✅")
        test += 1

        p1 = {'clasificacion': '7+'}
        p2 = {'clasificacion': '7+'}
        p3 = {'clasificacion': '18+'}
        p4 = {'clasificacion': '7+'}
        p5 = {'clasificacion': '7+'}

        print("Verificando la clasificación de la tercera pelicula únicamente ------------------------------- ❌", end='')
        tercer_peli = mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
        self.assertEqual(1, tercer_peli, "La función no calculó correctamente el numero de peliculas 18+.")
        print("\rVerificando la clasificación de la tercera pelicula únicamente -------------------------------- ✅")
        test += 1

        p1 = {'clasificacion': '7+'}
        p2 = {'clasificacion': '7+'}
        p3 = {'clasificacion': '7+'}
        p4 = {'clasificacion': '18+'}
        p5 = {'clasificacion': '7+'}

        print("Verificando la clasificación de la cuarta pelicula únicamente -------------------------------- ❌", end='')
        cuarta_peli = mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
        self.assertEqual(1, cuarta_peli, "La función no calculó correctamente el numero de peliculas 18+.")
        print("\rVerificando la clasificación de la cuarta pelicula únicamente --------------------------------- ✅")
        test += 1

        p1 = {'clasificacion': '7+'}
        p2 = {'clasificacion': '7+'}
        p3 = {'clasificacion': '7+'}
        p4 = {'clasificacion': '7+'}
        p5 = {'clasificacion': '18+'}

        print("Verificando la clasificación de la quinta pelicula únicamente -------------------------------- ❌", end='')
        quinta_peli = mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
        self.assertEqual(1, quinta_peli, "La función no calculó correctamente el numero de peliculas 18+.")
        print("\rVerificando la clasificación de la quinta pelicula únicamente --------------------------------- ✅")
        test += 1

        p1 = {'clasificacion': '18+'}
        p2 = {'clasificacion': '7+'}
        p3 = {'clasificacion': '18+'}
        p4 = {'clasificacion': '7+'}
        p5 = {'clasificacion': '7+'}

        print("Verificando la clasificación de la primera y tercera pelicula únicamente --------------------- ❌", end='')
        pyt_peli = mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
        self.assertEqual(2, pyt_peli, "La función no calculó correctamente el numero de peliculas 18+.")
        print("\rVerificando la clasificación de la primera y tercera pelicula únicamente ---------------------- ✅")
        test += 1

        p1 = {'clasificacion': '7+'}
        p2 = {'clasificacion': '18+'}
        p3 = {'clasificacion': '7+'}
        p4 = {'clasificacion': '18+'}
        p5 = {'clasificacion': '7+'}

        print("Verificando la clasificación de la segunda y cuarta pelicula únicamente ---------------------- ❌", end='')
        syc_peli = mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
        self.assertEqual(2, syc_peli, "La función no calculó correctamente el numero de peliculas 18+.")
        print("\rVerificando la clasificación de la segunda y cuarta pelicula únicamente ----------------------- ✅")
        test += 1

        p1 = {'clasificacion': '18+'}
        p2 = {'clasificacion': '18+'}
        p3 = {'clasificacion': '18+'}
        p4 = {'clasificacion': '18+'}
        p5 = {'clasificacion': '18+'}

        print("Verificando la clasificación de todas las peliculas ------------------------------------------ ❌", end='')
        todas = mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
        self.assertEqual(5, todas, "La función no calculó correctamente el numero de peliculas 18+.")
        print("\rVerificando la clasificación de todas las peliculas ------------------------------------------- ✅")
        test += 1

        p1 = {'clasificacion': '7+'}
        p2 = {'clasificacion': '7+'}
        p3 = {'clasificacion': '7+'}
        p4 = {'clasificacion': '7+'}
        p5 = {'clasificacion': '7+'}

        print("Verificando la clasificación de ninguna de las peliculas ------------------------------------- ❌", end='')
        ninguna = mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
        self.assertEqual(0, ninguna, "La función no calculó correctamente el numero de peliculas 18+.")
        print("\rVerificando la clasificación de estreno ninguna de las peliculas ------------------------------ ✅")
        test += 1

    def test_reagendar_pelicula(self):
        print()
        print(
            "################### Test reagendar_pelicula #################################################################")

        global test

        p1 = {'dia': 'Lunes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p2 = {'dia': 'Martes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p3 = {'dia': 'Miercoles', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p4 = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p5 = {'dia': 'Viernes', 'hora':1900, 'genero': 'Documental, Terror, Comedia', 'duracion': 90}

        prag = {'dia': 'Viernes', 'hora':1900, 'genero': 'Documental, Terror, Comedia', 'duracion': 90}
        
        print("Verificando que no cumple el primer control de horario ---------------------------------------- ❌", end='')
        ninguna = mod.reagendar_pelicula(prag, 2200, 'Domingo', True, p1, p2, p3, p4, p5)
        self.assertEqual(False, ninguna, "La función no determinó que no cumplia el control de horario")
        print("\rVerificando que no cumple el primer control de horario ---------------------------------------- ✅")
        test += 1
        
        p1 = {'dia': 'Lunes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p2 = {'dia': 'Martes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p3 = {'dia': 'Miercoles', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p4 = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p5 = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama, Terror, Comedia', 'duracion': 90}

        prag = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama, Terror, Comedia', 'duracion': 90}
        
        print("Verificando que no cumple el segundo control de horario -------------------------------------- ❌", end='')
        ninguna = mod.reagendar_pelicula(prag, 2200, 'Viernes', True, p1, p2, p3, p4, p5)
        self.assertEqual(False, ninguna, "La función no determinó que no cumplia el control de horario")
        print("\rVerificando que no cumple el segundo control de horario --------------------------------------- ✅")
        test += 1
        
        p1 = {'dia': 'Lunes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p2 = {'dia': 'Martes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p3 = {'dia': 'Miercoles', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p4 = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p5 = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama, Terror, Comedia', 'duracion': 90}

        prag = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama, Terror, Comedia', 'duracion': 90}
        
        print("Verificando que no cumple el tercer control de horario noche --------------------------------- ❌", end='')
        ninguna = mod.reagendar_pelicula(prag, 2300, 'Jueves', True, p1, p2, p3, p4, p5)
        self.assertEqual(False, ninguna, "La función no determinó que no cumplia el control de horario")
        print("\rVerificando que no cumple el tercer control de horario noche ---------------------------------- ✅")
        test += 1
        
        p1 = {'dia': 'Lunes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p2 = {'dia': 'Martes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p3 = {'dia': 'Miercoles', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p4 = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p5 = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama, Terror, Comedia', 'duracion': 90}

        prag = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama, Terror, Comedia', 'duracion': 90}
        
        print("Verificando que no cumple el tercer control de horario mañana -------------------------------- ❌", end='')
        ninguna = mod.reagendar_pelicula(prag, 500, 'Jueves', True, p1, p2, p3, p4, p5)
        self.assertEqual(False, ninguna, "La función no determinó que no cumplia el control de horario")
        print("\rVerificando que no cumple el tercer control de horario mañana --------------------------------- ✅")
        test += 1
        
        p1 = {'dia': 'Lunes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p2 = {'dia': 'Martes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p3 = {'dia': 'Miercoles', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p4 = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p5 = {'dia': 'Viernes', 'hora':1900, 'genero': 'Terror, Comedia', 'duracion': 90}

        prag = {'dia': 'Viernes', 'hora':1900, 'genero': 'Terror, Comedia', 'duracion': 90}
        
        print("Verificando que cumple el primer control de horario ------------------------------------------ ❌", end='')
        ninguna = mod.reagendar_pelicula(prag, 2200, 'Domingo', True, p1, p2, p3, p4, p5)
        self.assertEqual(True, ninguna, "La función no determinó que no cumplia el control de horario")
        print("\rVerificando que cumple el primer control de horario ------------------------------------------- ✅")
        test += 1
        
        p1 = {'dia': 'Lunes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p2 = {'dia': 'Martes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p3 = {'dia': 'Miercoles', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p4 = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p5 = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama, Terror, Comedia', 'duracion': 90}

        prag = {'dia': 'Jueves', 'hora':1900, 'genero': 'Terror, Comedia', 'duracion': 90}
        
        print("Verificando que cumple el segundo control de horario ----------------------------------------- ❌", end='')
        ninguna = mod.reagendar_pelicula(prag, 2200, 'Viernes', True, p1, p2, p3, p4, p5)
        self.assertEqual(True, ninguna, "La función no determinó que no cumplia el control de horario")
        print("\rVerificando que cumple el segundo control de horario ------------------------------------------ ✅")
        test += 1
        
        p1 = {'dia': 'Lunes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p2 = {'dia': 'Martes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p3 = {'dia': 'Miercoles', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p4 = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p5 = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama', 'duracion': 90}

        prag = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        
        print("Verificando que cumple el segundo control de horario ----------------------------------------- ❌", end='')
        ninguna = mod.reagendar_pelicula(prag, 2200, 'Miercoles', True, p1, p2, p3, p4, p5)
        self.assertEqual(True, ninguna, "La función no determinó que cumplia el control de horario")
        print("\rVerificando que cumple el segundo control de horario ------------------------------------------ ✅")
        test += 1
        
        p1 = {'dia': 'Lunes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p2 = {'dia': 'Martes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p3 = {'dia': 'Miercoles', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p4 = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p5 = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama', 'duracion': 90}

        prag = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        
        print("Verificando que cumple el tercer control de horario noche ------------------------------------ ❌", end='')
        ninguna = mod.reagendar_pelicula(prag, 2300, 'Sábado', True, p1, p2, p3, p4, p5)
        self.assertEqual(True, ninguna, "La función no determinó que cumplia el control de horario")
        print("\rVerificando que cumple el tercer control de horario noche ------------------------------------- ✅")
        test += 1
        
        p1 = {'dia': 'Lunes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p2 = {'dia': 'Martes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p3 = {'dia': 'Miercoles', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p4 = {'dia': 'Miercoles', 'hora':1300, 'genero': 'Drama', 'duracion': 90}
        p5 = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama', 'duracion': 90}

        prag = {'dia': 'Jueves', 'hora':1900, 'genero': 'Terror', 'duracion': 90}
        
        print("Verificando que cumple el tercer control de horario mañana ----------------------------------- ❌", end='')
        ninguna = mod.reagendar_pelicula(prag, 500, 'Domingo', True, p1, p2, p3, p4, p5)
        self.assertEqual(True, ninguna, "La función no determinó que cumplia el control de horario")
        print("\rVerificando que cumple el tercer control de horario mañana ------------------------------------ ✅")
        test += 1
        
        p1 = {'dia': 'Lunes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p2 = {'dia': 'Martes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p3 = {'dia': 'Miercoles', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p4 = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p5 = {'dia': 'Viernes', 'hora':1900, 'genero': 'Documental, Terror, Comedia', 'duracion': 90}

        prag = {'dia': 'Viernes', 'hora':1900, 'genero': 'Documental, Terror, Comedia', 'duracion': 90}
        
        print("Verificando que ignora el primer control de horario con control de horario en False ----------- ❌", end='')
        ninguna = mod.reagendar_pelicula(prag, 2200, 'Domingo', False, p1, p2, p3, p4, p5)
        self.assertEqual(True, ninguna, "La función no determinó que no cumplia el control de horario")
        print("\rVerificando que ignora el primer control de horario con control de horario en False ----------- ✅")
        test += 1
        
        p1 = {'dia': 'Lunes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p2 = {'dia': 'Martes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p3 = {'dia': 'Miercoles', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p4 = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p5 = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama, Terror, Comedia', 'duracion': 90}

        prag = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama, Terror, Comedia', 'duracion': 90}
        
        print("Verificando que ignora el segundo control de horario con control de horario en False ---------- ❌", end='')
        ninguna = mod.reagendar_pelicula(prag, 2200, 'Viernes', False, p1, p2, p3, p4, p5)
        self.assertEqual(True, ninguna, "La función no determinó que no cumplia el control de horario")
        print("\rVerificando que ignora el segundo control de horario con control de horario en False ---------- ✅")
        test += 1
        
        p1 = {'dia': 'Lunes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p2 = {'dia': 'Martes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p3 = {'dia': 'Miercoles', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p4 = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p5 = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama, Terror, Comedia', 'duracion': 90}

        prag = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama, Terror, Comedia', 'duracion': 90}
        
        print("Verificando que ignora el tercer control de horario noche con control de horario en False ----- ❌", end='')
        ninguna = mod.reagendar_pelicula(prag, 2300, 'Jueves', False, p1, p2, p3, p4, p5)
        self.assertEqual(True, ninguna, "La función no determinó que no cumplia el control de horario")
        print("\rVerificando que ignora el tercer control de horario noche con control de horario en False ----- ✅")
        test += 1
        
        p1 = {'dia': 'Lunes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p2 = {'dia': 'Martes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p3 = {'dia': 'Miercoles', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p4 = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p5 = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama, Terror, Comedia', 'duracion': 90}

        prag = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama, Terror, Comedia', 'duracion': 90}
        
        print("Verificando que ignora el tercer control de horario mañana con control de horario en False ---- ❌", end='')
        ninguna = mod.reagendar_pelicula(prag, 500, 'Jueves', False, p1, p2, p3, p4, p5)
        self.assertEqual(True, ninguna, "La función no determinó que no cumplia el control de horario")
        print("\rVerificando que ignora el tercer control de horario mañana con control de horario en False ---- ✅")
        test += 1
        
        p1 = {'dia': 'Lunes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p2 = {'dia': 'Martes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p3 = {'dia': 'Miercoles', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p4 = {'dia': 'Jueves', 'hora':1430, 'genero': 'Drama', 'duracion': 90}
        p5 = {'dia': 'Viernes', 'hora':1900, 'genero': 'Drama, Terror, Comedia', 'duracion': 90}

        prag = {'dia': 'Viernes', 'hora':1430, 'genero': 'Drama, Terror, Comedia', 'duracion': 90}
        
        print("Verificando que se cruza con la primera pelicula ---------------------------------------------- ❌", end='')
        ninguna = mod.reagendar_pelicula(prag, 1500, 'Jueves', False, p4, p2, p3, p5, p1)
        self.assertEqual(False, ninguna, "La función no determinó la pelicula se cruza con otras peliculas o determina que se cruza con ella misma")
        print("\rVerificando que se cruza con la primera pelicula ---------------------------------------------- ✅")
        test += 1
        
        print("Verificando que se cruza con la segunda pelicula --------------------------------------------- ❌", end='')
        ninguna = mod.reagendar_pelicula(prag, 1500, 'Jueves', False, p1, p4, p3, p5, p2)
        self.assertEqual(False, ninguna, "La función no determinó la pelicula se cruza con otras peliculas o determina que se cruza con ella misma")
        print("\rVerificando que se cruza con la segunda pelicula ---------------------------------------------- ✅")
        test += 1
        
        print("Verificando que se cruza con la tercera pelicula --------------------------------------------- ❌", end='')
        ninguna = mod.reagendar_pelicula(prag, 1500, 'Jueves', False, p1, p2, p4, p5, p3)
        self.assertEqual(False, ninguna, "La función no determinó la pelicula se cruza con otras peliculas o determina que se cruza con ella misma")
        print("\rVerificando que se cruza con la tercera pelicula ---------------------------------------------- ✅")
        test += 1
        
        print("Verificando que se cruza con la cuarta pelicula ---------------------------------------------- ❌", end='')
        ninguna = mod.reagendar_pelicula(prag, 1500, 'Jueves', False, p1, p2, p3, p4, p5)
        self.assertEqual(False, ninguna, "La función no determinó la pelicula se cruza con otras peliculas o determina que se cruza con ella misma")
        print("\rVerificando que se cruza con la cuarta pelicula ----------------------------------------------- ✅")
        test += 1
        
        print("Verificando que se cruza con la quinta pelicula ---------------------------------------------- ❌", end='')
        ninguna = mod.reagendar_pelicula(prag, 1500, 'Jueves', False, p1, p2, p3, p5, p4)
        self.assertEqual(False, ninguna, "La función no determinó la pelicula se cruza con otras peliculas o determina que se cruza con ella misma")
        print("\rVerificando que se cruza con la quinta pelicula ----------------------------------------------- ✅")
        test += 1
        
        p1 = {'dia': 'Lunes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p2 = {'dia': 'Martes', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p3 = {'dia': 'Miercoles', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p4 = {'dia': 'Jueves', 'hora':1900, 'genero': 'Drama', 'duracion': 90}
        p5 = {'dia': 'Viernes', 'hora':1430, 'genero': 'Drama, Terror, Comedia', 'duracion': 90}

        prag = {'dia': 'Viernes', 'hora':1430, 'genero': 'Drama, Terror, Comedia', 'duracion': 90}
        
        print("Verificando que no se cruza con ella misma ---------------------------------------------------- ❌", end='')
        ninguna = mod.reagendar_pelicula(prag, 1500, 'Viernes', False, p1, p2, p3, p5, p4)
        self.assertEqual(True, ninguna, "La función determinó que la pelicula se puede cruzar con el horario anterior de la misma pelicula")
        print("\rVerificando que no se cruza con ella misma ---------------------------------------------------- ✅")
        test += 1
        
    def test_decidir_invitar(self):
        print()
        print(
            "################### Test decidir_invitar #################################################################")

        global test

        prag = {'clasificacion': '18+', 'genero': 'Terror'}
        
        print("Verificando que no se cruza con ella misma ---------------------------------------------------- ❌", end='')
        ninguna = mod.decidir_invitar(prag, 18, True)
        self.assertEqual(True, ninguna, "La función determinó que la pelicula se puede cruzar con el horario anterior de la misma pelicula")
        print("\rVerificando que no se cruza con ella misma ---------------------------------------------------- ✅")
        test += 1

        prag = {'clasificacion': '15+', 'genero': 'Terror'}
        
        print("Verificando que no se cruza con ella misma ---------------------------------------------------- ❌", end='')
        ninguna = mod.decidir_invitar(prag, 15, True)
        self.assertEqual(False, ninguna, "La función determinó que la pelicula se puede cruzar con el horario anterior de la misma pelicula")
        print("\rVerificando que no se cruza con ella misma ---------------------------------------------------- ✅")
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
