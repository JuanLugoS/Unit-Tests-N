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
 * Proyecto de nivel 3
 * 12 de Noviembre de 2021
 *
 * @author Juan Lugo Sánchez
 * jd.lugo@uniandes.edu.co
 * 201913094
"""
import unittest
import cupicoin as cupi

test = 0


class MyTestCase(unittest.TestCase):
    def test_cargar_datos(self):
        print()
        print("################### Test cargar_datos #################################################################")

        global test

        f = open("test_GENERATEDFILE.csv", "w")
        f.write("codigo,block_number,from_address,to_address,value,block_timestamp\n")
        f.write("0x0760,0,0x0881,0x120ad,6.07e+18,141\n")
        f.write("0x0761,0,0x0881,0x120ad,1000.0,142\n")
        f.write("0x0762,1,0x0881,0x120ad,6.07E+18,143\n")
        f.write("0x0763,2,0x0881,0x120ad,1e+18,144")
        f.close()

        lista = [{'numero_bloque': 0, 'cantidad_transacciones': 2, 'timestamp': '142', 'abierto': False, 'hash': 37,
                  'hash_anterior': None,
                  0: {'codigo_transaccion': '0x0760', 'remitente': '0x0881', 'destinatario': '0x120ad',
                      'valor': 6070000000000000000, 'operacion': 'transferencia'},
                  1: {'codigo_transaccion': '0x0761', 'remitente': '0x0881', 'destinatario': '0x120ad',
                      'valor': 1000, 'operacion': 'transferencia'}},
                 {'numero_bloque': 1, 'cantidad_transacciones': 1, 'timestamp': '143', 'abierto': False, 'hash': 7,
                  'hash_anterior': 37,
                  0: {'codigo_transaccion': '0x0762', 'remitente': '0x0881', 'destinatario': '0x120ad',
                      'valor': 6070000000000000000, 'operacion': 'transferencia'}},
                 {'numero_bloque': 2, 'cantidad_transacciones': 1, 'timestamp': '144', 'abierto': True, 'hash': 64,
                  'hash_anterior': 7,
                  0: {'codigo_transaccion': '0x0763', 'remitente': '0x0881', 'destinatario': '0x120ad',
                      'valor': 1000000000000000000, 'operacion': 'transferencia'}}]

        datos_cargados = cupi.cargar_archivo("test_GENERATEDFILE.csv")

        print("Verificando la carga de un archivo ---------------------------------------------------------- ❌", end='')
        self.assertEqual(datos_cargados, lista, "No se cargan los datos segun la manera establecida.")
        print("\rVerificando la carga de un archivo ---------------------------------------------------------- ✅")
        test += 1

    def test_agregar_bloque(self):
        print()
        print("################### Test agregar_bloque ###############################################################")

        global test

        lista = [{'numero_bloque': 0, 'cantidad_transacciones': 2, 'timestamp': '142', 'abierto': False, 'hash': 118,
                  'hash_anterior': None,
                  0: {'codigo_transaccion': '0x0760', 'remitente': '0x0881', 'destinatario': '0x120ad', 'valor': 109,
                      'operacion': 'transferencia'},
                  1: {'codigo_transaccion': '0x0761', 'remitente': '0x0881', 'destinatario': '0x120ad', 'valor': 1000,
                      'operacion': 'transferencia'}},
                 {'numero_bloque': 1, 'cantidad_transacciones': 1, 'timestamp': '143', 'abierto': False, 'hash': 142,
                  'hash_anterior': 118,
                  0: {'codigo_transaccion': '0x0762', 'remitente': '0x0881', 'destinatario': '0x120ad', 'valor': 109,
                      'operacion': 'transferencia'}},
                 {'numero_bloque': 2, 'cantidad_transacciones': 1, 'timestamp': '144', 'abierto': True, 'hash': 72,
                  'hash_anterior': 142,
                  0: {'codigo_transaccion': '0x0763', 'remitente': '0x0881', 'destinatario': '0x120ad', 'valor': 18,
                      'operacion': 'transferencia'}}]

        lista_n = [{'numero_bloque': 0, 'cantidad_transacciones': 2, 'timestamp': '142', 'abierto': False, 'hash': 118,
                    'hash_anterior': None,
                    0: {'codigo_transaccion': '0x0760', 'remitente': '0x0881', 'destinatario': '0x120ad', 'valor': 109,
                        'operacion': 'transferencia'},
                    1: {'codigo_transaccion': '0x0761', 'remitente': '0x0881', 'destinatario': '0x120ad', 'valor': 1000,
                        'operacion': 'transferencia'}},
                   {'numero_bloque': 1, 'cantidad_transacciones': 1, 'timestamp': '143', 'abierto': False, 'hash': 142,
                    'hash_anterior': 118,
                    0: {'codigo_transaccion': '0x0762', 'remitente': '0x0881', 'destinatario': '0x120ad', 'valor': 109,
                        'operacion': 'transferencia'}},
                   {'numero_bloque': 2, 'cantidad_transacciones': 1, 'timestamp': '144', 'abierto': False, 'hash': 72,
                    'hash_anterior': 142,
                    0: {'codigo_transaccion': '0x0763', 'remitente': '0x0881', 'destinatario': '0x120ad', 'valor': 18,
                        'operacion': 'transferencia'}},
                   {"numero_bloque": 3, "cantidad_transacciones": 0, "timestamp": 0, "abierto": True,
                    "hash": None, "hash_anterior": 72}]

        lista_con_bloque = cupi.anadir_bloque(lista)
        lista_n[3]["timestamp"] = lista_con_bloque[3]["timestamp"]

        print("Verificando la adición de un bloque --------------------------------------------------------- ❌", end='')
        self.assertEqual(lista_n, lista_con_bloque, "La información del nuevo bloque o bloque anterior no concuerda")
        print("\rVerificando la adición de un bloque --------------------------------------------------------- ✅")
        test += 1

    def test_agregar_transaccion(self):
        print()
        print("################### Test agregar_transaccion ##########################################################")

        global test

        lista = {'numero_bloque': 2, 'cantidad_transacciones': 1, 'timestamp': '144', 'abierto': True, 'hash': 72,
                 'hash_anterior': 142,
                 0: {'codigo_transaccion': '0x0763', 'remitente': '0x0881', 'destinatario': '0x120ad', 'valor': 18,
                     'operacion': 'transferencia'}}

        lista_n = {'numero_bloque': 2, 'cantidad_transacciones': 2, 'timestamp': '144', 'abierto': True, 'hash': 32,
                   'hash_anterior': 142,
                   0: {'codigo_transaccion': '0x0763', 'remitente': '0x0881', 'destinatario': '0x120ad', 'valor': 18,
                       'operacion': 'transferencia'},
                   1: {'codigo_transaccion': '0x0764', 'remitente': '0x0881', 'destinatario': '0x120ad', 'valor': 1000,
                       'operacion': 'transferencia'}}

        lista_con_transaccion = cupi.anadir_transaccion(lista, "0x0764", "0x0881", "0x120ad", 1000, "144")

        print("Verificando la adición de una transacción --------------------------------------------------- ❌", end='')
        self.assertEqual(lista_n, lista_con_transaccion, "El metodo no añadió correctamente la transacción")
        print("\rVerificando la adición de una transacción --------------------------------------------------- ✅")
        test += 1

    def test_consultar_numero_de_transacciones(self):
        print()
        print("################### Test consultar_numero_de_transacciones ############################################")

        global test

        lista = [{'numero_bloque': 0, 'cantidad_transacciones': 2, 'timestamp': '142', 'abierto': False, 'hash': 118,
                  'hash_anterior': None,
                  0: {'codigo_transaccion': '0x0760', 'remitente': '0x0760', 'destinatario': '0x120ad', 'valor': 109,
                      'operacion': 'transferencia'},
                  1: {'codigo_transaccion': '0x0761', 'remitente': '0x0881', 'destinatario': '0x0760', 'valor': 1000,
                      'operacion': 'transferencia'}},
                 {'numero_bloque': 1, 'cantidad_transacciones': 1, 'timestamp': '143', 'abierto': False, 'hash': 142,
                  'hash_anterior': 118,
                  0: {'codigo_transaccion': '0x0762', 'remitente': '0x0881', 'destinatario': '0x0760', 'valor': 109,
                      'operacion': 'transferencia'}},
                 {'numero_bloque': 2, 'cantidad_transacciones': 1, 'timestamp': '144', 'abierto': True, 'hash': 72,
                  'hash_anterior': 142,
                  0: {'codigo_transaccion': '0x0763', 'remitente': '0x0881', 'destinatario': '0x0760', 'valor': 18,
                      'operacion': 'transferencia'}}]

        dict_esperado = {"remitente": 1, "destinatario": 3}

        numero_de_transacciones = cupi.consultar_numero_transacciones(lista, "0x0760")

        print("Verificando el numero de transaccióne existentes -------------------------------------------- ❌", end='')
        self.assertEqual(numero_de_transacciones, dict_esperado)
        print("\rVerificando el numero de transaccióne existentes -------------------------------------------- ✅")
        test += 1

    def test_consultar_informacion_transaccion_por_codigo(self):
        print()
        print("################### Test consultar_informacion_transaccion_por_codigo #################################")

        global test

        lista = [{'numero_bloque': 0, 'cantidad_transacciones': 2, 'timestamp': '142', 'abierto': False, 'hash': 118,
                  'hash_anterior': None,
                  0: {'codigo_transaccion': '0x0760', 'remitente': '0x0760', 'destinatario': '0x120ad', 'valor': 109,
                      'operacion': 'transferencia'},
                  1: {'codigo_transaccion': '0x0761', 'remitente': '0x0881', 'destinatario': '0x0760', 'valor': 1000,
                      'operacion': 'transferencia'}},
                 {'numero_bloque': 1, 'cantidad_transacciones': 1, 'timestamp': '143', 'abierto': False, 'hash': 142,
                  'hash_anterior': 118,
                  0: {'codigo_transaccion': '0x0762', 'remitente': '0x0881', 'destinatario': '0x0760', 'valor': 109,
                      'operacion': 'transferencia'}},
                 {'numero_bloque': 2, 'cantidad_transacciones': 1, 'timestamp': '144', 'abierto': True, 'hash': 72,
                  'hash_anterior': 142,
                  0: {'codigo_transaccion': '0x0763', 'remitente': '0x0881', 'destinatario': '0x0760', 'valor': 18,
                      'operacion': 'transferencia'}}]

        buscado = {'codigo_transaccion': '0x0763', 'remitente': '0x0881', 'destinatario': '0x0760', 'valor': 18,
                   'operacion': 'transferencia'}

        encontrado = cupi.consultar_informacion_transaccion_por_codigo(lista, "0x0763")
        encontrado_falso = cupi.consultar_informacion_transaccion_por_codigo(lista, "0x0768")

        print("Verificando la busqueda de una transacción -------------------------------------------------- ❌", end='')
        self.assertEqual(buscado, encontrado, "No se buscó correctamenete la transacción")
        print("\rVerificando la busqueda de una transacción -------------------------------------------------- ✅")
        test += 1

        print("Verificando la busqueda de una transacción que NO existe ------------------------------------ ❌", end='')
        self.assertIsNone(encontrado_falso, "Se encontró in diccionario que no exisye")
        print("\rVerificando la busqueda de una transacción que NO existe ------------------------------------ ✅")
        test += 1

    def test_encontrar_transacciones_por_remitente_y_destinatario(self):
        print()
        print("################### Test encontrar_transacciones_por_remitente_y_destinatario #########################")

        global test

        lista = [{'numero_bloque': 0, 'cantidad_transacciones': 2, 'timestamp': '142', 'abierto': False, 'hash': 118,
                  'hash_anterior': None,
                  0: {'codigo_transaccion': '0x0760', 'remitente': '0x0760', 'destinatario': '0x120ad', 'valor': 109,
                      'operacion': 'transferencia'},
                  1: {'codigo_transaccion': '0x0761', 'remitente': '0x0881', 'destinatario': '0x0760', 'valor': 1000,
                      'operacion': 'transferencia'}},
                 {'numero_bloque': 1, 'cantidad_transacciones': 1, 'timestamp': '143', 'abierto': False, 'hash': 142,
                  'hash_anterior': 118,
                  0: {'codigo_transaccion': '0x0762', 'remitente': '0x0881', 'destinatario': '0x0760', 'valor': 109,
                      'operacion': 'transferencia'}},
                 {'numero_bloque': 2, 'cantidad_transacciones': 1, 'timestamp': '144', 'abierto': True, 'hash': 72,
                  'hash_anterior': 142,
                  0: {'codigo_transaccion': '0x0763', 'remitente': '0x0760', 'destinatario': '0x120ad', 'valor': 18,
                      'operacion': 'transferencia'}}]

        lista_esperada = [
            {'codigo_transaccion': '0x0760', 'remitente': '0x0760', 'destinatario': '0x120ad', 'valor': 109,
             'operacion': 'transferencia'},
            {'codigo_transaccion': '0x0763', 'remitente': '0x0760', 'destinatario': '0x120ad', 'valor': 18,
             'operacion': 'transferencia'}]

        encontrados = cupi.encontrar_transacciones_por_remitente_y_destinatario(lista, "0x0760", "0x120ad")

        print("Verificando busqueda de una transaccion entre destinatario y remitente ---------------------- ❌", end='')
        self.assertEqual(lista_esperada, encontrados, "No se encontraron todas las transacciones buscadas.")
        print("\rVerificando busqueda de una transaccion entre destinatario y remitente  --------------------- ✅")
        test += 1

    def test_consultar_transaccion_valor_maximo(self):
        print()
        print("################### Test consultar_transaccion_valor_maximo ###########################################")

        global test

        lista = [{'numero_bloque': 0, 'cantidad_transacciones': 2, 'timestamp': '142', 'abierto': False, 'hash': 118,
                  'hash_anterior': None,
                  0: {'codigo_transaccion': '0x0760', 'remitente': '0x0760', 'destinatario': '0x120ad', 'valor': 109,
                      'operacion': 'transferencia'},
                  1: {'codigo_transaccion': '0x0761', 'remitente': '0x0881', 'destinatario': '0x0760', 'valor': 1000,
                      'operacion': 'transferencia'}},
                 {'numero_bloque': 1, 'cantidad_transacciones': 1, 'timestamp': '143', 'abierto': False, 'hash': 142,
                  'hash_anterior': 118,
                  0: {'codigo_transaccion': '0x0762', 'remitente': '0x0881', 'destinatario': '0x0760', 'valor': 109,
                      'operacion': 'transferencia'}},
                 {'numero_bloque': 2, 'cantidad_transacciones': 1, 'timestamp': '144', 'abierto': True, 'hash': 72,
                  'hash_anterior': 142,
                  0: {'codigo_transaccion': '0x0763', 'remitente': '0x0760', 'destinatario': '0x120ad', 'valor': 18,
                      'operacion': 'transferencia'}}]

        buscado = {'codigo_transaccion': '0x0761', 'remitente': '0x0881', 'destinatario': '0x0760', 'valor': 1000,
                   'operacion': 'transferencia'}

        encontrado = cupi.consultar_transaccion_valor_maximo(lista)

        print("Verificando la busqueda del la transacción con mayor valor ---------------------------------- ❌", end='')
        self.assertEqual(buscado, encontrado, "No se encontró la transacción con valor máximo.")
        print("\rVerificando la busqueda del la transacción con mayor valor ---------------------------------- ✅")
        test += 1

    def test_calcular_saldo_cuenta(self):
        print()
        print("################### Test calcular_saldo_cuenta ########################################################")

        global test

        lista = [{'numero_bloque': 0, 'cantidad_transacciones': 2, 'timestamp': '142', 'abierto': False, 'hash': 118,
                  'hash_anterior': None,
                  0: {'codigo_transaccion': '0x0760', 'remitente': '0x0760', 'destinatario': '', 'valor': 10000,
                      'operacion': 'contrato'},
                  1: {'codigo_transaccion': '0x0761', 'remitente': '0x0760', 'destinatario': '0x0761', 'valor': 1000,
                      'operacion': 'transferencia'}},
                 {'numero_bloque': 1, 'cantidad_transacciones': 1, 'timestamp': '143', 'abierto': False, 'hash': 142,
                  'hash_anterior': 118,
                  0: {'codigo_transaccion': '0x0762', 'remitente': '0x0881', 'destinatario': '0x0760', 'valor': 1000,
                      'operacion': 'transferencia'}},
                 {'numero_bloque': 2, 'cantidad_transacciones': 1, 'timestamp': '144', 'abierto': True, 'hash': 72,
                  'hash_anterior': 142,
                  0: {'codigo_transaccion': '0x0763', 'remitente': '0x0760', 'destinatario': '0x120ad', 'valor': 200,
                      'operacion': 'transferencia'}}]

        saldo_calculado = cupi.calcular_saldo_cuenta(lista, "0x0760")

        print("Verificando el calculo de saldo de una billetera -------------------------------------------- ❌", end='')
        self.assertEqual(saldo_calculado, 9800, "El saldo no corresponde al saldo real de la cuenta")
        print("\rVerificando el calculo de saldo de una billetera -------------------------------------------- ✅")
        test += 1

    def test_validar_integridad(self):
        print()
        print("################### Test validar_integridad ###########################################################")

        global test

        hash_inc = [{'numero_bloque': 0, 'cantidad_transacciones': 2, 'timestamp': '142', 'abierto': False, 'hash': 128,
                     'hash_anterior': None,
                     0: {'codigo_transaccion': '0x0760', 'remitente': '0x0760', 'destinatario': '', 'valor': 10000,
                         'operacion': 'contrato'},
                     1: {'codigo_transaccion': '0x0761', 'remitente': '0x0760', 'destinatario': '0x0761', 'valor': 1000,
                         'operacion': 'transferencia'}},
                    {'numero_bloque': 1, 'cantidad_transacciones': 1, 'timestamp': '143', 'abierto': False, 'hash': 142,
                     'hash_anterior': 118,
                     0: {'codigo_transaccion': '0x0762', 'remitente': '0x0881', 'destinatario': '0x0760', 'valor': 1000,
                         'operacion': 'transferencia'}},
                    {'numero_bloque': 2, 'cantidad_transacciones': 1, 'timestamp': '144', 'abierto': True, 'hash': 72,
                     'hash_anterior': 142,
                     0: {'codigo_transaccion': '0x0763', 'remitente': '0x0760', 'destinatario': '0x120ad', 'valor': 200,
                         'operacion': 'transferencia'}}]

        bloq_ab = [{'numero_bloque': 0, 'cantidad_transacciones': 2, 'timestamp': '142', 'abierto': True, 'hash': 118,
                    'hash_anterior': None,
                    0: {'codigo_transaccion': '0x0760', 'remitente': '0x0760', 'destinatario': '', 'valor': 10000,
                        'operacion': 'contrato'},
                    1: {'codigo_transaccion': '0x0761', 'remitente': '0x0760', 'destinatario': '0x0761', 'valor': 1000,
                        'operacion': 'transferencia'}},
                   {'numero_bloque': 1, 'cantidad_transacciones': 1, 'timestamp': '143', 'abierto': False, 'hash': 142,
                    'hash_anterior': 118,
                    0: {'codigo_transaccion': '0x0762', 'remitente': '0x0881', 'destinatario': '0x0760', 'valor': 1000,
                        'operacion': 'transferencia'}},
                   {'numero_bloque': 2, 'cantidad_transacciones': 1, 'timestamp': '144', 'abierto': True, 'hash': 72,
                    'hash_anterior': 142,
                    0: {'codigo_transaccion': '0x0763', 'remitente': '0x0760', 'destinatario': '0x120ad', 'valor': 200,
                        'operacion': 'transferencia'}}]

        ante_inc = [{'numero_bloque': 0, 'cantidad_transacciones': 2, 'timestamp': '142', 'abierto': False, 'hash': 118,
                     'hash_anterior': None,
                     0: {'codigo_transaccion': '0x0760', 'remitente': '0x0760', 'destinatario': '', 'valor': 10000,
                         'operacion': 'contrato'},
                     1: {'codigo_transaccion': '0x0761', 'remitente': '0x0760', 'destinatario': '0x0761', 'valor': 1000,
                         'operacion': 'transferencia'}},
                    {'numero_bloque': 1, 'cantidad_transacciones': 1, 'timestamp': '143', 'abierto': False, 'hash': 142,
                     'hash_anterior': 218,
                     0: {'codigo_transaccion': '0x0762', 'remitente': '0x0881', 'destinatario': '0x0760', 'valor': 1000,
                         'operacion': 'transferencia'}},
                    {'numero_bloque': 2, 'cantidad_transacciones': 1, 'timestamp': '144', 'abierto': True, 'hash': 72,
                     'hash_anterior': 142,
                     0: {'codigo_transaccion': '0x0763', 'remitente': '0x0760', 'destinatario': '0x120ad', 'valor': 200,
                         'operacion': 'transferencia'}}]

        integro = [{'numero_bloque': 0, 'cantidad_transacciones': 2, 'timestamp': '142', 'abierto': False, 'hash': 37,
                    'hash_anterior': None,
                    0: {'codigo_transaccion': '0x0760', 'remitente': '0x0881', 'destinatario': '0x120ad',
                        'valor': 6070000000000000000, 'operacion': 'transferencia'},
                    1: {'codigo_transaccion': '0x0761', 'remitente': '0x0881', 'destinatario': '0x120ad',
                        'valor': 1000, 'operacion': 'transferencia'}},
                   {'numero_bloque': 1, 'cantidad_transacciones': 1, 'timestamp': '143', 'abierto': False, 'hash': 7,
                    'hash_anterior': 37,
                    0: {'codigo_transaccion': '0x0762', 'remitente': '0x0881', 'destinatario': '0x120ad',
                        'valor': 6070000000000000000, 'operacion': 'transferencia'}},
                   {'numero_bloque': 2, 'cantidad_transacciones': 1, 'timestamp': '144', 'abierto': True, 'hash': 64,
                    'hash_anterior': 7,
                    0: {'codigo_transaccion': '0x0763', 'remitente': '0x0881', 'destinatario': '0x120ad',
                        'valor': 1000000000000000000, 'operacion': 'transferencia'}}]

        integridad_hash = cupi.validar_integridad(hash_inc)
        integridad_abierto = cupi.validar_integridad(bloq_ab)
        integridad_anterior = cupi.validar_integridad(ante_inc)
        integridad = cupi.validar_integridad(integro)

        print("Verificando integridad de los hash ---------------------------------------------------------- ❌", end='')
        self.assertFalse(integridad_hash, "La función no comprobó que la integridad de los hash de los bloques "
                                          "no era correcta.")
        print("\rVerificando integridad de los hash ---------------------------------------------------------- ✅")
        test += 1

        print("Verificando la ingtegridad de más de un bloque abierto -------------------------------------- ❌", end='')
        self.assertFalse(integridad_abierto, "La función no comprobó que uno de los bloques, que no"
                                             " era el último, estaba abierto.")
        print("\rVerificando la ingtegridad de más de un bloque abierto -------------------------------------- ✅")
        test += 1

        print("Verificando la correspondencia del hash anterior -------------------------------------------- ❌", end='')
        self.assertFalse(integridad_anterior, "La función no comprobó que los hash de los bloques anteriores "
                                              "no era correcto")
        print("\rVerificando la correspondencia del hash anterior -------------------------------------------- ✅")
        test += 1

        print("Verificando la integridad correcta ---------------------------------------------------------- ❌", end='')
        self.assertTrue(integridad, "La función no comprobó que la integridad era correcta.")
        print("\rVerificando la integridad correcta ---------------------------------------------------------- ✅")
        test += 1


if __name__ == '__main__':
    unittest.main()


def print_percent_done(index, total, bar_len=14, title='Please wait'):
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
    print_percent_done(test, 14)
