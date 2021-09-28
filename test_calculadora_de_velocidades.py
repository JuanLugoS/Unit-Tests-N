# -*- coding: utf-8 -*-
"""
Copyright 2021 Juan Lugo Sánchez - jd.lugo@uniandes.edu.co
Permission is hereby granted, free of charge, to any person obtaining a copy 
of this software and associated documentation files (the "Software"), to deal 
in the Software without restriction, including without limitation the rights 
to use, copy, modify, merge, publish and/or distribute copies of the Software, 
and to permit persons to whom the Software is furnished to do so, subject to 
the following conditions:
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
 * 26 de Septiembre de 2021
 *
 * @author Juan Lugo Sánchez
 * jd.lugo@uniandes.edu.co
 * 201913094
"""

import unittest
import calculadora_de_velocidades as mod

test = 0


class TestAnalizador(unittest.TestCase):

    def test_crear_sector(self):
        print()
        print("################### Test crear_sector ##################################################################")

        global test

        sector1_funcion = mod.crear_sector("sector a", 3, 0.05, 7.3, 2.5, True, False, "Total", False, False, True)

        sector1 = {"nombre": "sector a", "carriles": 3, "pendiente": 0.05,
                   "ancho_calzada": 7.3, "ancho_berma": 2.5, "separador": True,
                   "peatones": False, "control_accesos": "Total",
                   "zona_recreacional": False, "cuello_de_botella": False,
                   "zona_escolar": True}
        print("Verificando la creacion de un sector -------------------------------------------------------- ❌", end='')

        self.assertEqual(sector1, sector1_funcion,
                         "El diccionario creado no corresponde con los valores dados por parametro; "
                         "revisar los elementos que tienen + y - para determinar que valores son diferentes")
        print("\rVerificando la creacion de un sector -------------------------------------------------------- ✅")
        test += 1

    def test_buscar_sector(self):
        print()
        print("################### Test buscar_sector #################################################################")

        global test

        s1 = {"nombre": "sector a", "carriles": 3, "pendiente": 0.05, "ancho_calzada": 7.3, "ancho_berma": 2.5,
              "separador": True, "peatones": False, "control_accesos": "Total", "zona_recreacional": False,
              "cuello_de_botella": False, "zona_escolar": True}

        s2 = {"nombre": "sector b", "carriles": 3, "pendiente": 0.06, "ancho_calzada": 7.3, "ancho_berma": 1.5,
              "separador": True, "peatones": False, "control_accesos": "Parcial", "zona_recreacional": False,
              "cuello_de_botella": False, "zona_escolar": True}

        s3 = {"nombre": "sector c", "carriles": 2, "pendiente": 0.06, "ancho_calzada": 7.3, "ancho_berma": 1.8,
              "separador": False, "peatones": False, "control_accesos": "Nulo", "zona_recreacional": False,
              "cuello_de_botella": False, "zona_escolar": True}

        s4 = {"nombre": "sector d", "carriles": 2, "pendiente": 0.09, "ancho_calzada": 7.0, "ancho_berma": 0.4,
              "separador": False, "peatones": True, "control_accesos": "Nulo", "zona_recreacional": False,
              "cuello_de_botella": False, "zona_escolar": False}

        encontrado1 = mod.buscar_sector("sector a", s1, s2, s3, s4)

        print("Verificando la busqueda de un sector existente ---------------------------------------------- ❌", end='')
        self.assertEqual(s1, encontrado1, "La funcion no encontró el sector buscado")
        print("\rVerificando la busqueda de un sector existente ---------------------------------------------- ✅")
        test += 1

        encontrado2 = mod.buscar_sector("sector x", s1, s2, s3, s4)

        print("Verificando la busqueda de un sector NO existente ------------------------------------------- ❌", end='')
        self.assertIsNone(encontrado2, "La funcion encontró un sector que no existe")
        print("\rVerificando la busqueda de un sector NO existente ------------------------------------------- ✅")
        test += 1

    def test_clasificar_sector(self):
        print()
        print("################### Test clasificar_sector #############################################################")
        global test

        # --------------------------------------------------------------------------------------------------------------
        # Casos en los que se comprueba el tipo A1
        s1 = {"nombre": "sector a", "carriles": 3, "pendiente": 0.05, "ancho_calzada": 7.3, "ancho_berma": 2.5}
        s1_mep = {"nombre": "sector a", "carriles": 3, "pendiente": 0.045, "ancho_calzada": 7.3, "ancho_berma": 2.5}
        s1_map = {"nombre": "sector a", "carriles": 3, "pendiente": 0.055, "ancho_calzada": 7.3, "ancho_berma": 2.5}

        sec1_r = mod.clasificar_sector(s1)
        sec1_mep_r = mod.clasificar_sector(s1_mep)
        sec1_map_r = mod.clasificar_sector(s1_map)

        print("Verificando la clasificación de un sector A1 con pendiente máxima --------------------------- ❌", end='')
        self.assertEqual(sec1_r, "A1", "La función no determinó correctamente la geometría del sector")
        print("\rVerificando la clasificación de un sector A1 con pendiente máxima --------------------------- ✅")
        test += 1

        print("Verificando la clasificación de sector A1 con pendiente arriba del máximo ------------------- ❌", end='')
        self.assertNotEquals(sec1_map_r, "A1", "La función no determinó correctamente la geometría del sector")
        print("\rVerificando la clasificación de sector A1 con pendiente arriba del máximo ------------------- ✅")
        test += 1

        print("Verificando la clasificación de un sector A1 ------------------------------------------------ ❌", end='')
        self.assertEqual(sec1_mep_r, "A1", "La función no determinó correctamente la geometría del sector")
        print("\rVerificando la clasificación de un sector A1 ------------------------------------------------ ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Casos en los que se comprueba el tipo B1
        s2 = {"nombre": "sector b", "carriles": 3, "pendiente": 0.06, "ancho_calzada": 7.3, "ancho_berma": 1.5}
        s2_mep = {"nombre": "sector b", "carriles": 3, "pendiente": 0.055, "ancho_calzada": 7.3, "ancho_berma": 1.5}
        s2_map = {"nombre": "sector b", "carriles": 3, "pendiente": 0.065, "ancho_calzada": 7.3, "ancho_berma": 1.5}

        sec2_r = mod.clasificar_sector(s2)
        sec2_mep_r = mod.clasificar_sector(s2_mep)
        sec2_map_r = mod.clasificar_sector(s2_map)

        print("Verificando la clasificación de un sector B1 con pendiente máxima --------------------------- ❌", end='')
        self.assertEqual(sec2_r, "B1", "La función no determinó correctamente la geometría del sector")
        print("\rVerificando la clasificación de un sector B1 con pendiente máxima --------------------------- ✅")
        test += 1

        print("Verificando la clasificación de un sector B1 ------------------------------------------------ ❌", end='')
        self.assertEquals(sec2_mep_r, "B1", "La función no determinó correctamente la geometría del sector")
        print("\rVerificando la clasificación de un sector B1 ------------------------------------------------ ✅")
        test += 1

        print("Verificando la clasificación de sector B1 con pendiente arriba del máximo ------------------- ❌", end='')
        self.assertNotEquals(sec2_map_r, "B1", "La función no determinó correctamente la geometría del sector")
        print("\rVerificando la clasificación de sector B1 con pendiente arriba del máximo ------------------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Casos en los que se comprueba el tipo C1
        s3 = {"nombre": "sector c", "carriles": 3, "pendiente": 0.08, "ancho_calzada": 7.0, "ancho_berma": 1.3}
        s3_mep = {"nombre": "sector c", "carriles": 3, "pendiente": 0.075, "ancho_calzada": 7.0, "ancho_berma": 1.3}
        s3_map = {"nombre": "sector c", "carriles": 3, "pendiente": 0.085, "ancho_calzada": 7.0, "ancho_berma": 1.3}

        sec3_r = mod.clasificar_sector(s3)
        sec3_mep_r = mod.clasificar_sector(s3_mep)
        sec3_map_r = mod.clasificar_sector(s3_map)

        print("Verificando la clasificación de un sector C1 con pendiente máxima --------------------------- ❌", end='')
        self.assertEqual(sec3_r, "C1", "La función no determinó correctamente la geometría del sector")
        print("\rVerificando la clasificación de un sector C1 con pendiente máxima --------------------------- ✅")
        test += 1

        print("Verificando la clasificación de un sector C1 ------------------------------------------------ ❌", end='')
        self.assertEquals(sec3_mep_r, "C1", "La función no determinó correctamente la geometría del sector")
        print("\rVerificando la clasificación de un sector C1 ------------------------------------------------ ✅")
        test += 1

        print("Verificando la clasificación de sector C1 con pendiente arriba del máximo ------------------- ❌", end='')
        self.assertNotEquals(sec3_map_r, "C1", "La función no determinó correctamente la geometría del sector")
        print("\rVerificando la clasificación de sector C1 con pendiente arriba del máximo ------------------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Casos en los que se comprueba el tipo A2
        s4 = {"nombre": "sector d", "carriles": 2, "pendiente": 0.06, "ancho_calzada": 7.3, "ancho_berma": 1.8}
        s4_mep = {"nombre": "sector d", "carriles": 2, "pendiente": 0.055, "ancho_calzada": 7.3, "ancho_berma": 1.8}
        s4_map = {"nombre": "sector d", "carriles": 2, "pendiente": 0.065, "ancho_calzada": 7.3, "ancho_berma": 1.8}

        sec4_r = mod.clasificar_sector(s4)
        sec4_mep_r = mod.clasificar_sector(s4_mep)
        sec4_map_r = mod.clasificar_sector(s4_map)

        print("Verificando la clasificación de un sector A2 con pendiente máxima --------------------------- ❌", end='')
        self.assertEqual(sec4_r, "A2", "La función no determinó correctamente la geometría del sector")
        print("\rVerificando la clasificación de un sector A2 con pendiente máxima --------------------------- ✅")
        test += 1

        print("Verificando la clasificación de un sector A2 ------------------------------------------------ ❌", end='')
        self.assertEquals(sec4_mep_r, "A2", "La función no determinó correctamente la geometría del sector")
        print("\rVerificando la clasificación de un sector A2 ------------------------------------------------ ✅")
        test += 1

        print("Verificando la clasificación de sector A2 con pendiente arriba del máximo ------------------- ❌", end='')
        self.assertNotEquals(sec4_map_r, "A2", "La función no determinó correctamente la geometría del sector")
        print("\rVerificando la clasificación de sector A2 con pendiente arriba del máximo ------------------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Casos en los que se comprueba el tipo B2
        s5 = {"nombre": "sector b", "carriles": 2, "pendiente": 0.08, "ancho_calzada": 7.3, "ancho_berma": 1.0}
        s5_mep = {"nombre": "sector b", "carriles": 2, "pendiente": 0.075, "ancho_calzada": 7.3, "ancho_berma": 1.0}
        s5_map = {"nombre": "sector b", "carriles": 2, "pendiente": 0.085, "ancho_calzada": 7.3, "ancho_berma": 1.0}

        sec5_r = mod.clasificar_sector(s5)
        sec5_mep_r = mod.clasificar_sector(s5_mep)
        sec5_map_r = mod.clasificar_sector(s5_map)

        print("Verificando la clasificación de un sector B2 con pendiente máxima --------------------------- ❌", end='')
        self.assertEqual(sec5_r, "B2", "La función no determinó correctamente la geometría del sector")
        print("\rVerificando la clasificación de un sector B2 con pendiente máxima --------------------------- ✅")
        test += 1

        print("Verificando la clasificación de un sector B2 ------------------------------------------------ ❌", end='')
        self.assertEquals(sec5_mep_r, "B2", "La función no determinó correctamente la geometría del sector")
        print("\rVerificando la clasificación de un sector B2 ------------------------------------------------ ✅")
        test += 1

        print("Verificando la clasificación de sector B2 con pendiente arriba del máximo ------------------- ❌", end='')
        self.assertNotEquals(sec5_map_r, "B2", "La función no determinó correctamente la geometría del sector")
        print("\rVerificando la clasificación de sector B2 con pendiente arriba del máximo ------------------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Casos en los que se comprueba el tipo C2
        s6 = {"nombre": "sector c", "carriles": 2, "pendiente": 0.09, "ancho_calzada": 7.0, "ancho_berma": 0.5}
        s6_mep = {"nombre": "sector c", "carriles": 2, "pendiente": 0.085, "ancho_calzada": 7.0, "ancho_berma": 0.5}
        s6_map = {"nombre": "sector c", "carriles": 2, "pendiente": 0.095, "ancho_calzada": 7.0, "ancho_berma": 0.5}

        sec6_r = mod.clasificar_sector(s6)
        sec6_mep_r = mod.clasificar_sector(s6_mep)
        sec6_map_r = mod.clasificar_sector(s6_map)

        print("Verificando la clasificación de un sector C2 con pendiente máxima --------------------------- ❌", end='')
        self.assertEqual(sec6_r, "C2", "La función no determinó correctamente la geometría del sector")
        print("\rVerificando la clasificación de un sector C2 con pendiente máxima --------------------------- ✅")
        test += 1

        print("Verificando la clasificación de un sector C2 ------------------------------------------------ ❌", end='')
        self.assertEquals(sec6_mep_r, "C2", "La función no determinó correctamente la geometría del sector")
        print("\rVerificando la clasificación de un sector C2 ------------------------------------------------ ✅")
        test += 1

        print("Verificando la clasificación de sector C2 con pendiente arriba del máximo ------------------- ❌", end='')
        self.assertNotEquals(sec6_map_r, "C2", "La función no determinó correctamente la geometría del sector")
        print("\rVerificando la clasificación de sector C2 con pendiente arriba del máximo ------------------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Casos en los que se comprueba el tipo D2
        s7 = {"nombre": "sector d", "carriles": 2, "pendiente": 0.09, "ancho_calzada": 7.0, "ancho_berma": 0.4}
        s7_mep = {"nombre": "sector d", "carriles": 2, "pendiente": 0.085, "ancho_calzada": 7.0, "ancho_berma": 0.4}
        s7_map = {"nombre": "sector d", "carriles": 2, "pendiente": 0.095, "ancho_calzada": 7.0, "ancho_berma": 0.4}

        sec7_r = mod.clasificar_sector(s7)
        sec7_mep_r = mod.clasificar_sector(s7_mep)
        sec7_map_r = mod.clasificar_sector(s7_map)

        print("Verificando la clasificación de un sector D2 con pendiente máxima --------------------------- ❌", end='')
        self.assertEqual(sec7_r, "D2", "La función no determinó correctamente la geometría del sector")
        print("\rVerificando la clasificación de un sector D2 con pendiente máxima --------------------------- ✅")
        test += 1

        print("Verificando la clasificación de un sector D2 ------------------------------------------------ ❌", end='')
        self.assertEquals(sec7_mep_r, "D2", "La función no determinó correctamente la geometría del sector")
        print("\rVerificando la clasificación de un sector D2 ------------------------------------------------ ✅")
        test += 1

        print("Verificando la clasificación de sector D2 con pendiente arriba del máximo ------------------- ❌", end='')
        self.assertNotEquals(sec7_map_r, "D2", "La función no determinó correctamente la geometría del sector")
        print("\rVerificando la clasificación de sector D2 con pendiente arriba del máximo ------------------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Casos en los que se comprueba el que el acho de berma y calzada no corresponden
        s_berma = {"nombre": "sector d", "carriles": 2, "pendiente": 0.09, "ancho_calzada": 7.0, "ancho_berma": 0.8}
        s_ancho = {"nombre": "sector d", "carriles": 2, "pendiente": 0.09, "ancho_calzada": 6.0, "ancho_berma": 0.4}

        s_berma_r = mod.clasificar_sector(s_berma)
        s_ancho_r = mod.clasificar_sector(s_ancho)

        print("Verificando la clasificación de un sector con berma incorrecta ------------------------------ ❌", end='')
        self.assertIsNone(s_berma_r, "La función calculó una geometría para un sector que no cumple ninguna de las "
                                     "condiciones")
        print("\rVerificando la clasificación de un sector con berma incorrecta ------------------------------ ✅")
        test += 1

        print("Verificando la clasificación de un sector con ancho incorrecto ------------------------------ ❌", end='')
        self.assertIsNone(s_ancho_r, "La función calculó una geometría para un sector que no cumple ninguna de las "
                                     "condiciones")
        print("\rVerificando la clasificación de un sector con ancho incorrecto ------------------------------ ✅")
        test += 1

    def test_determinar_velocidad_generica(self):
        print()
        print("################### Test determinar_velocidad_generica #################################################")
        
        global test

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # ---------------------Multicarril Separador----------------------------
        # Caso en el que la velocidad generica es 120 para A1
        a1_120 = {"carriles": 3, "pendiente": 0.05, "ancho_calzada": 7.3, "ancho_berma": 2.5,
              "separador": True, "peatones": False, "control_accesos": "Total"}

        vel_gen_a1120 = mod.determinar_velocidad_generica(a1_120)

        print("Verificando la determinacion de una velocidad generica de 120 para A1 ----------------------- ❌", end='')
        self.assertEquals(vel_gen_a1120, 120, "La función calculó incorrectamente la velocidad generica")
        print("\rVerificando la determinacion de una velocidad generica de 120 para A1 ----------------------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Caso en el que la velocidad generica es 100 para B1
        b1_100 = {"carriles": 3, "pendiente": 0.06, "ancho_calzada": 7.3, "ancho_berma": 1.5,
                  "separador": True, "peatones": False, "control_accesos": "Parcial"}

        vel_gen_b1100 = mod.determinar_velocidad_generica(b1_100)

        print("Verificando la determinacion de una velocidad generica de 100 para B1 ----------------------- ❌", end='')
        self.assertEquals(vel_gen_b1100, 100, "La función calculó incorrectamente la velocidad generica")
        print("\rVerificando la determinacion de una velocidad generica de 100 para B1 ----------------------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Caso en el que la velocidad generica es 90 para B1
        b1_90 = {"carriles": 3, "pendiente": 0.06, "ancho_calzada": 7.3, "ancho_berma": 1.5,
              "separador": True, "peatones": False, "control_accesos": "Nulo"}

        vel_gen_b190 = mod.determinar_velocidad_generica(b1_90)

        print("Verificando la determinacion de una velocidad generica de 90 para B1 ------------------------ ❌", end='')
        self.assertEquals(vel_gen_b190, 90, "La función calculó incorrectamente la velocidad generica")
        print("\rVerificando la determinacion de una velocidad generica de 90 para B1 ------------------------ ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Caso en el que la velocidad generica es 80 para C1
        c1_80 = {"carriles": 3, "pendiente": 0.08, "ancho_calzada": 7.0, "ancho_berma": 1.3,
              "separador": True, "peatones": False, "control_accesos": "Nulo"}

        vel_gen_c180 = mod.determinar_velocidad_generica(c1_80)

        print("Verificando la determinacion de una velocidad generica de 80 para C1 ------------------------ ❌", end='')
        self.assertEquals(vel_gen_c180, 80, "La función calculó incorrectamente la velocidad generica")
        print("\rVerificando la determinacion de una velocidad generica de 80 para C1 ------------------------ ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Caso en el que la velocidad generica es 70 para C1
        c1_70 = {"carriles": 3, "pendiente": 0.08, "ancho_calzada": 7.0, "ancho_berma": 1.3,
              "separador": True, "peatones": True, "control_accesos": "Nulo"}

        vel_gen_c170 = mod.determinar_velocidad_generica(c1_70)

        print("Verificando la determinacion de una velocidad generica de 70 para C1 ------------------------ ❌", end='')
        self.assertEquals(vel_gen_c170, 70, "La función calculó incorrectamente la velocidad generica")
        print("\rVerificando la determinacion de una velocidad generica de 70 para C1 ------------------------ ✅")
        test += 1

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # ---------------------Multicarril sin Separador----------------------------
        # Caso en el que la velocidad generica es none para A1
        a1_none = {"carriles": 3, "pendiente": 0.05, "ancho_calzada": 7.3, "ancho_berma": 2.5,
                  "separador": False, "peatones": False, "control_accesos": "Total"}

        vel_gen_a1none = mod.determinar_velocidad_generica(a1_none)

        print("Verificando la determinacion de una velocidad generica de nula para A1 ---------------------- ❌", end='')
        self.assertIsNone(vel_gen_a1none, "La función calculó una velocidad generica para un sector que no tiene")
        print("\rVerificando la determinacion de una velocidad generica de nula para A1 ---------------------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Caso en el que la velocidad generica es 90 para B1
        b1_90_s = {"carriles": 3, "pendiente": 0.06, "ancho_calzada": 7.3, "ancho_berma": 1.5,
                  "separador": False, "peatones": False, "control_accesos": "Parcial"}

        vel_gen_b190s = mod.determinar_velocidad_generica(b1_90_s)

        print("Verificando la determinacion de una velocidad generica de 90 para B1 sin separador ---------- ❌", end='')
        self.assertEquals(vel_gen_b190s, 90, "La función calculó incorrectamente la velocidad generica")
        print("\rVerificando la determinacion de una velocidad generica de 90 para B1 sin separador ---------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Caso en el que la velocidad generica es 80 para B1
        b1_80 = {"carriles": 3, "pendiente": 0.06, "ancho_calzada": 7.3, "ancho_berma": 1.5,
                 "separador": False, "peatones": False, "control_accesos": "Nulo"}

        vel_gen_b180 = mod.determinar_velocidad_generica(b1_80)

        print("Verificando la determinacion de una velocidad generica de 80 para B1 ------------------------ ❌", end='')
        self.assertEquals(vel_gen_b180, 80, "La función calculó incorrectamente la velocidad generica")
        print("\rVerificando la determinacion de una velocidad generica de 80 para B1 ------------------------ ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Caso en el que la velocidad generica es 70 para C1
        c1_70 = {"carriles": 3, "pendiente": 0.08, "ancho_calzada": 7.0, "ancho_berma": 1.3,
                 "separador": False, "peatones": False, "control_accesos": "Nulo"}

        vel_gen_c170 = mod.determinar_velocidad_generica(c1_70)

        print("Verificando la determinacion de una velocidad generica de 70 para C1 ------------------------ ❌", end='')
        self.assertEquals(vel_gen_c170, 70, "La función calculó incorrectamente la velocidad generica")
        print("\rVerificando la determinacion de una velocidad generica de 70 para C1 ------------------------ ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Caso en el que la velocidad generica es 60 para C1
        c1_60 = {"carriles": 3, "pendiente": 0.08, "ancho_calzada": 7.0, "ancho_berma": 1.3,
                 "separador": False, "peatones": True, "control_accesos": "Nulo"}

        vel_gen_c160 = mod.determinar_velocidad_generica(c1_60)

        print("Verificando la determinacion de una velocidad generica de 60 para C1 ------------------------ ❌", end='')
        self.assertEquals(vel_gen_c160, 60, "La función calculó incorrectamente la velocidad generica")
        print("\rVerificando la determinacion de una velocidad generica de 60 para C1 ------------------------ ✅")
        test += 1

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # ---------------------Dos carriles sin Separador----------------------------
        # Caso en el que la velocidad generica es 80 para A2
        a2_80 = {"carriles": 2, "pendiente": 0.06, "ancho_calzada": 7.3, "ancho_berma": 1.8,
              "separador": False, "peatones": False, "control_accesos": "Nulo"}

        vel_gen_a280 = mod.determinar_velocidad_generica(a2_80)

        print("Verificando la determinacion de una velocidad generica de 80 para A2 ------------------------ ❌", end='')
        self.assertEquals(vel_gen_a280, 80, "La función calculó incorrectamente la velocidad generica")
        print("\rVerificando la determinacion de una velocidad generica de 80 para A2 ------------------------ ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Caso en el que la velocidad generica es 70 para A2
        a2_70 = {"carriles": 2, "pendiente": 0.06, "ancho_calzada": 7.3, "ancho_berma": 1.8,
                 "separador": False, "peatones": True, "control_accesos": "Nulo"}

        vel_gen_a270 = mod.determinar_velocidad_generica(a2_70)

        print("Verificando la determinacion de una velocidad generica de 70 para A2 ------------------------ ❌", end='')
        self.assertEquals(vel_gen_a270, 70, "La función calculó incorrectamente la velocidad generica")
        print("\rVerificando la determinacion de una velocidad generica de 70 para A2 ------------------------ ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Caso en el que la velocidad generica es 70 para B2
        b2_70 = {"carriles": 2, "pendiente": 0.08, "ancho_calzada": 7.3, "ancho_berma": 1.0,
                 "separador": False, "peatones": False, "control_accesos": "Nulo"}

        vel_gen_b270 = mod.determinar_velocidad_generica(b2_70)

        print("Verificando la determinacion de una velocidad generica de 70 para B2 ------------------------ ❌", end='')
        self.assertEquals(vel_gen_b270, 70, "La función calculó incorrectamente la velocidad generica")
        print("\rVerificando la determinacion de una velocidad generica de 70 para B2 ------------------------ ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Caso en el que la velocidad generica es 60 para B2
        b2_60 = {"carriles": 2, "pendiente": 0.08, "ancho_calzada": 7.3, "ancho_berma": 1.0,
                 "separador": False, "peatones": True, "control_accesos": "Nulo"}

        vel_gen_b260 = mod.determinar_velocidad_generica(b2_60)

        print("Verificando la determinacion de una velocidad generica de 60 para B2 ------------------------ ❌", end='')
        self.assertEquals(vel_gen_b260, 60, "La función calculó incorrectamente la velocidad generica")
        print("\rVerificando la determinacion de una velocidad generica de 60 para B2 ------------------------ ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Caso en el que la velocidad generica es 50 para C2
        c2_50 = {"carriles": 2, "pendiente": 0.09, "ancho_calzada": 7.0, "ancho_berma": 0.5,
              "separador": False, "peatones": True, "control_accesos": "Nulo"}

        vel_gen_c250 = mod.determinar_velocidad_generica(c2_50)

        print("Verificando la determinacion de una velocidad generica de 50 para C2 ------------------------ ❌", end='')
        self.assertEquals(vel_gen_c250, 50, "La función calculó incorrectamente la velocidad generica")
        print("\rVerificando la determinacion de una velocidad generica de 50 para C2 ------------------------ ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Caso en el que la velocidad generica es 40 para D2
        d2_40 = {"carriles": 2, "pendiente": 0.09, "ancho_calzada": 7.0, "ancho_berma": 0.4,
              "separador": False, "peatones": True, "control_accesos": "Nulo"}

        vel_gen_d240 = mod.determinar_velocidad_generica(d2_40)

        print("Verificando la determinacion de una velocidad generica de 40 para D2 ------------------------ ❌", end='')
        self.assertEquals(vel_gen_d240, 40, "La función calculó incorrectamente la velocidad generica")
        print("\rVerificando la determinacion de una velocidad generica de 40 para D2 ------------------------ ✅")
        test += 1

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # ---------------------Dos carriles Separador----------------------------
        # Caso en el que la velocidad generica es None para A2
        a2_80 = {"carriles": 2, "pendiente": 0.06, "ancho_calzada": 7.3, "ancho_berma": 1.8,
                 "separador": True, "peatones": False, "control_accesos": "Nulo"}

        vel_gen_a280 = mod.determinar_velocidad_generica(a2_80)

        print("Verificando la determinacion de una velocidad generica de None para A2 ---------------------- ❌", end='')
        self.assertIsNone(vel_gen_a280, "La función calculó la velocidad generica para un sector sin con caracteristicas"
                                        " inconsistentes, los sectores multicarril no poseen separador")
        print("\rVerificando la determinacion de una velocidad generica de None para A2 ---------------------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Caso en el que la velocidad generica es None para A2
        a2_70 = {"carriles": 2, "pendiente": 0.06, "ancho_calzada": 7.3, "ancho_berma": 1.8,
                 "separador": True, "peatones": True, "control_accesos": "Nulo"}

        vel_gen_a270 = mod.determinar_velocidad_generica(a2_70)

        print("Verificando la determinacion de una velocidad generica de None para A2 ---------------------- ❌", end='')
        self.assertIsNone(vel_gen_a270, "La función calculó la velocidad generica para un sector sin con caracteristicas"
                                        " inconsistentes, los sectores multicarril no poseen separador")
        print("\rVerificando la determinacion de una velocidad generica de None para A2 ---------------------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Caso en el que la velocidad generica es None para B2
        b2_70 = {"carriles": 2, "pendiente": 0.08, "ancho_calzada": 7.3, "ancho_berma": 1.0,
                 "separador": True, "peatones": False, "control_accesos": "Nulo"}

        vel_gen_b270 = mod.determinar_velocidad_generica(b2_70)

        print("Verificando la determinacion de una velocidad generica de None para B2 ---------------------- ❌", end='')
        self.assertIsNone(vel_gen_b270, "La función calculó la velocidad generica para un sector sin con caracteristicas"
                                        " inconsistentes, los sectores multicarril no poseen separador")
        print("\rVerificando la determinacion de una velocidad generica de None para B2 ---------------------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Caso en el que la velocidad generica es None para B2
        b2_60 = {"carriles": 2, "pendiente": 0.08, "ancho_calzada": 7.3, "ancho_berma": 1.0,
                 "separador": True, "peatones": True, "control_accesos": "Nulo"}

        vel_gen_b260 = mod.determinar_velocidad_generica(b2_60)

        print("Verificando la determinacion de una velocidad generica de None para B2 ---------------------- ❌", end='')
        self.assertIsNone(vel_gen_b260, "La función calculó la velocidad generica para un sector sin con caracteristicas"
                                        " inconsistentes, los sectores multicarril no poseen separador")
        print("\rVerificando la determinacion de una velocidad generica de None para B2 ---------------------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Caso en el que la velocidad generica es None para C2
        c2_50 = {"carriles": 2, "pendiente": 0.09, "ancho_calzada": 7.0, "ancho_berma": 0.5,
                 "separador": True, "peatones": True, "control_accesos": "Nulo"}

        vel_gen_c250 = mod.determinar_velocidad_generica(c2_50)

        print("Verificando la determinacion de una velocidad generica de None para C2 ---------------------- ❌", end='')
        self.assertIsNone(vel_gen_c250,"La función calculó la velocidad generica para un sector sin con caracteristicas "
                                       "inconsistentes, los sectores multicarril no poseen separador")
        print("\rVerificando la determinacion de una velocidad generica de None para C2 ---------------------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Caso en el que la velocidad generica es None para D2
        d2_40 = {"carriles": 2, "pendiente": 0.09, "ancho_calzada": 7.0, "ancho_berma": 0.4,
                 "separador": True, "peatones": True, "control_accesos": "Nulo"}

        vel_gen_d240 = mod.determinar_velocidad_generica(d2_40)

        print("Verificando la determinacion de una velocidad generica de None para D2 ---------------------- ❌", end='')
        self.assertIsNone(vel_gen_d240, "La función calculó la velocidad generica para un sector sin con caracteristicas"
                                        " inconsistentes, los sectores multicarril no poseen separador")
        print("\rVerificando la determinacion de una velocidad generica de None para D2 ---------------------- ✅")
        test += 1


    def test_calcular_velocidad_promedio(self):
        print()
        print("################### Test calcular_velocidad_promedio ###################################################")

        global test

        # --------------------------------------------------------------------------------------------------------------
        # Sector sin zonas especiales
        s1 = {"carriles": 2, "pendiente": 0.09, "ancho_calzada": 7.0, "ancho_berma": 0.4,
                   "separador": False, "peatones": True, "control_accesos": "Nulo",
                   "zona_recreacional": False, "cuello_de_botella": False, "zona_escolar": False}

        s1_r = mod.calcular_velocidad_promedio(s1)

        print("Verificando el calculo correcto de la velocidad promedio 40 sin zonas ----------------------- ❌", end='')
        self.assertEquals(s1_r, 40, "La función calculó incorrectamente la velocidad promedio")
        print("\rVerificando el calculo correcto de la velocidad promedio 40 sin zonas ----------------------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Sector con Zona recreacional
        s2 = {"carriles": 2, "pendiente": 0.09, "ancho_calzada": 7.0, "ancho_berma": 0.4,
              "separador": False, "peatones": True, "control_accesos": "Nulo",
              "zona_recreacional": True, "cuello_de_botella": False, "zona_escolar": False}

        s2_r = mod.calcular_velocidad_promedio(s2)

        print("Verificando el calculo correcto de la velocidad promedio 35 con Z.R ------------------------- ❌", end='')
        self.assertEquals(s2_r, 35, "La función calculó incorrectamente la velocidad promedio")
        print("\rVerificando el calculo correcto de la velocidad promedio 35 con Z.R ------------------------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Sector con Zona recreacional y cuello de botella
        s3 = {"carriles": 2, "pendiente": 0.09, "ancho_calzada": 7.0, "ancho_berma": 0.4,
              "separador": False, "peatones": True, "control_accesos": "Nulo",
              "zona_recreacional": True, "cuello_de_botella": True, "zona_escolar": False}

        s3_r = mod.calcular_velocidad_promedio(s3)
        vel =110/3

        print("Verificando el calculo correcto de la velocidad promedio 36.6 con Z.R y C.B ----------------- ❌", end='')
        self.assertEquals(s3_r, vel, "La función calculó incorrectamente la velocidad promedio")
        print("\rVerificando el calculo correcto de la velocidad promedio 36.6 con Z.R y C.B ----------------- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Sector con Zona recreacional, cuello de botella y zona escolar
        s4 = {"carriles": 2, "pendiente": 0.09, "ancho_calzada": 7.0, "ancho_berma": 0.4,
              "separador": False, "peatones": True, "control_accesos": "Nulo",
              "zona_recreacional": True, "cuello_de_botella": True, "zona_escolar": True}

        s4_r = mod.calcular_velocidad_promedio(s4)

        print("Verificando el calculo correcto de la velocidad promedio 35 con Z.R, C.B y Z.E -------------- ❌", end='')
        self.assertEquals(s4_r, 35, "La función calculó incorrectamente la velocidad promedio")
        print("\rVerificando el calculo correcto de la velocidad promedio 35 con Z.R, C.B y Z.E -------------- ✅")
        test += 1


    def test_contar_libres_de_restriccion(self):
        print()
        print("################### Test contar_libres_de_restriccion ##################################################")

        global test

        s1 = {"zona_recreacional": False, "cuello_de_botella": False, "zona_escolar": False}
        s2 = {"zona_recreacional": True,  "cuello_de_botella": False, "zona_escolar": False}
        s3 = {"zona_recreacional": True,  "cuello_de_botella": True,  "zona_escolar": False}
        s4 = {"zona_recreacional": True,  "cuello_de_botella": True,  "zona_escolar": True }

        res = mod.contar_libres_de_restriccion(s1, s2, s3, s4)

        print("Verificando el calculo correcto del conteo de zonas libres de restricciones ----------------- ❌", end='')
        self.assertEquals(res, 1, "La función calculó incorrectamente el contreo de zonas libres de restricciones")
        print("\rVerificando el calculo correcto del conteo de zonas libres de restricciones ----------------- ✅")


    def test_determinar_pendiente_menor(self):
        print()
        print("################### Test determinar_pendiente_menor ####################################################")

        global test

        # --------------------------------------------------------------------------------------------------------------
        # 1 con menor pendiente
        s1 = {"nombre": "sector 1", "pendiente": 0.09}
        s2 = {"nombre": "sector 2", "pendiente": 0.02}
        s3 = {"nombre": "sector 3", "pendiente": 0.09}
        s4 = {"nombre": "sector 4", "pendiente": 0.09}

        s1_r = mod.determinar_pendiente_menor(0.07, s1, s2, s3, s4)

        print("Verificando la correcta determinacion de sectores con pendiente manor a la dada: 1 sector --- ❌", end='')
        self.assertEquals(s1_r, "sector 2", "La función calculó incorrectamente los sectores que cumplen con la condicion")
        print("\rVerificando la correcta determinacion de sectores con pendiente manor a la dada: 1 sector --- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # 2 con menor pendiente
        s5 = {"nombre": "sector 5", "pendiente": 0.02}
        s6 = {"nombre": "sector 6", "pendiente": 0.09}
        s7 = {"nombre": "sector 7", "pendiente": 0.02}
        s8 = {"nombre": "sector 8", "pendiente": 0.09}

        s2_r = mod.determinar_pendiente_menor(0.07, s5, s6, s7, s8)

        print("Verificando la correcta determinacion de sectores con pendiente manor a la dada: 2 sectores - ❌", end='')
        self.assertEquals(s2_r, "sector 5, sector 7", "La función calculó incorrectamente los sectores que cumplen con la condicion")
        print("\rVerificando la correcta determinacion de sectores con pendiente manor a la dada: 2 sectores - ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # 3 con menor pendiente
        s9 = {"nombre": "sector 9", "pendiente": 0.09}
        s10 = {"nombre": "sector 10", "pendiente": 0.02}
        s11 = {"nombre": "sector 11", "pendiente": 0.02}
        s12 = {"nombre": "sector 12", "pendiente": 0.02}

        s3_r = mod.determinar_pendiente_menor(0.07, s9, s10, s11, s12)

        print("Verificando la correcta determinacion de sectores con pendiente manor a la dada: 3 sectores - ❌", end='')
        self.assertEquals(s3_r, "sector 10, sector 11, sector 12", "La función calculó incorrectamente los sectores que cumplen con la condicion")
        print("\rVerificando la correcta determinacion de sectores con pendiente manor a la dada: 3 sectores - ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # 4 con menor pendiente
        s13 = {"nombre": "sector 13", "pendiente": 0.01}
        s14 = {"nombre": "sector 14", "pendiente": 0.02}
        s15 = {"nombre": "sector 15", "pendiente": 0.03}
        s16 = {"nombre": "sector 16", "pendiente": 0.04}

        s4_r = mod.determinar_pendiente_menor(0.07, s13, s14, s15, s16)

        print("Verificando la correcta determinacion de sectores con pendiente manor a la dada: 4 sectores - ❌", end='')
        self.assertEquals(s4_r, "sector 13, sector 14, sector 15, sector 16", "La función calculó incorrectamente los sectores que cumplen con la condicion")
        print("\rVerificando la correcta determinacion de sectores con pendiente manor a la dada: 4 sectores - ✅")
        test += 1


    def test_velocidad_maxima(self):
        print()
        print("################### Test velocidad_maxima ##############################################################")

        global test

        # --------------------------------------------------------------------------------------------------------------
        # velocidades
        vel40_a = {"nombre": "a", "carriles": 2, "pendiente": 0.09, "ancho_calzada": 7.0, "ancho_berma": 0.4,
                   "separador": False, "peatones": True, "control_accesos": "Nulo"}

        vel40_b = {"nombre": "b", "carriles": 2, "pendiente": 0.09, "ancho_calzada": 7.0, "ancho_berma": 0.4,
                 "separador": False, "peatones": True, "control_accesos": "Nulo"}

        vel50 = {"nombre": "a", "carriles": 2, "pendiente": 0.09, "ancho_calzada": 7.0, "ancho_berma": 0.5,
                 "separador": False, "peatones": True, "control_accesos": "Nulo"}

        # --------------------------------------------------------------------------------------------------------------
        # primero con mayor velocidad

        s1_r = mod.velocidad_maxima(vel50, vel40_a, vel40_a, vel40_a)

        print("Verificando la correcta determinacion del sector con mayor velocidad generica: sector 1 ----- ❌", end='')
        self.assertEquals(s1_r, vel50, "La función calculó incorrectamente el sector con mayor velocidad")
        print("\rVerificando la correcta determinacion del sector con mayor velocidad generica: sector 1 ----- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # segundo con mayor velocidad

        s2_r = mod.velocidad_maxima(vel40_a, vel50, vel40_a, vel40_a)

        print("Verificando la correcta determinacion del sector con mayor velocidad generica: sector 2 ----- ❌", end='')
        self.assertEquals(s2_r, vel50, "La función calculó incorrectamente el sector con mayor velocidad")
        print("\rVerificando la correcta determinacion del sector con mayor velocidad generica: sector 2 ----- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # tercero con mayor velocidad

        s3_r = mod.velocidad_maxima(vel40_a, vel40_a, vel50, vel40_a)

        print("Verificando la correcta determinacion del sector con mayor velocidad generica: sector 3 ----- ❌", end='')
        self.assertEquals(s3_r, vel50, "La función calculó incorrectamente el sector con mayor velocidad")
        print("\rVerificando la correcta determinacion del sector con mayor velocidad generica: sector 3 ----- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # cuarto con mayor velocidad

        s4_r = mod.velocidad_maxima(vel40_a, vel40_a, vel40_a, vel50)

        print("Verificando la correcta determinacion del sector con mayor velocidad generica: sector 4 ----- ❌", end='')
        self.assertEquals(s4_r, vel50, "La función calculó incorrectamente el sector con mayor velocidad")
        print("\rVerificando la correcta determinacion del sector con mayor velocidad generica: sector 4 ----- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # misma velocidad, distinción por nombre con mayor velocidad

        s5_r = mod.velocidad_maxima(vel40_b, vel40_a, vel40_b, vel40_b)

        print("Verificando la correcta determinacion del sector con mayor velocidad generica: sector a ----- ❌", end='')
        self.assertEquals(s5_r, vel40_a, "La función calculó incorrectamente el sector con mayor velocidad")
        print("\rVerificando la correcta determinacion del sector con mayor velocidad generica: sector a ----- ✅")
        test += 1


    def test_contar_sitios_especiales(self):
        print()
        print("################### Test contar_sitios_especiales ######################################################")

        global test

        # --------------------------------------------------------------------------------------------------------------
        # Diccionarios de prueba
        s1 = {"zona_recreacional": False, "cuello_de_botella": False, "zona_escolar": False}
        s2 = {"zona_recreacional": True,  "cuello_de_botella": False, "zona_escolar": False}
        s3 = {"zona_recreacional": True,  "cuello_de_botella": True,  "zona_escolar": False}
        s4 = {"zona_recreacional": True,  "cuello_de_botella": True,  "zona_escolar": True }

        # --------------------------------------------------------------------------------------------------------------
        # Respuestas esperadas
        numero_sitos_1 = {"zona_recreacional": 0, "cuello_de_botella": 0, "zona_escolar": 0}
        numero_sitos_2 = {"zona_recreacional": 4, "cuello_de_botella": 0, "zona_escolar": 0}
        numero_sitos_3 = {"zona_recreacional": 4, "cuello_de_botella": 4, "zona_escolar": 0}
        numero_sitos_4 = {"zona_recreacional": 4, "cuello_de_botella": 4, "zona_escolar": 4}

        # --------------------------------------------------------------------------------------------------------------
        # Numero sitios: 1

        res_1 = mod.contar_sitios_especiales(s1, s1, s1, s1)

        print("Verificando el calculo correcto del conteo de sitios especiales: esperados 0 en cada llave -- ❌", end='')
        self.assertEquals(res_1, numero_sitos_1, "La función calculó incorrectamente el contreo de especiales")
        print("\rVerificando el calculo correcto del conteo de sitios especiales: esperados 0 en cada llave -- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Numero sitios: 2

        res_2 = mod.contar_sitios_especiales(s2, s2, s2, s2)

        print("Verificando el calculo correcto del conteo de sitios especiales: esperados 1 en cada llave -- ❌", end='')
        self.assertEquals(res_2, numero_sitos_2, "La función calculó incorrectamente el contreo de especiales")
        print("\rVerificando el calculo correcto del conteo de sitios especiales: esperados 1 en cada llave -- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Numero sitios: 3

        res_3 = mod.contar_sitios_especiales(s3, s3, s3, s3)

        print("Verificando el calculo correcto del conteo de sitios especiales: esperados 2 en cada llave -- ❌", end='')
        self.assertEquals(res_3, numero_sitos_3, "La función calculó incorrectamente el contreo de especiales")
        print("\rVerificando el calculo correcto del conteo de sitios especiales: esperados 2 en cada llave -- ✅")
        test += 1

        # --------------------------------------------------------------------------------------------------------------
        # Numero sitios: 4

        res_4 = mod.contar_sitios_especiales(s4, s4, s4, s4)

        print("Verificando el calculo correcto del conteo de sitios especiales: esperados 3 en cada llave -- ❌", end='')
        self.assertEquals(res_4, numero_sitos_4, "La función calculó incorrectamente el contreo de especiales")
        print("\rVerificando el calculo correcto del conteo de sitios especiales: esperados 3 en cada llave -- ✅")
        test += 1


if __name__ == '__main__':
    unittest.main()


def print_percent_done(index, total, bar_len=66, title='Please wait'):
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
    print_percent_done(test, 66)