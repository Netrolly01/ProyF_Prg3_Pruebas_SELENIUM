import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
import time
import HtmlTestRunner
import os

class H1_inicio_index_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver_path = r"C:\Driver\msedgedriver.exe"
        cls.service = EdgeService(executable_path=cls.driver_path)
        cls.driver = webdriver.Edge(service=cls.service)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def remove_non_ascii(self, text):
        return ''.join(c for c in text if ord(c) < 128)

    def test_inicio_index(self):
        try:
            # Ir al sitio local
            self.driver.get("http://localhost:8001/listadeVis.php")
            time.sleep(2)

            titulo = self.driver.title
            titulo_limpio = self.remove_non_ascii(titulo)

            print("Título de la página (limpio):", titulo_limpio)

            # Captura de pantalla del listado de datos
            if not os.path.exists("fotos_pr"):
                os.makedirs("fotos_pr")
            self.driver.save_screenshot("fotos_pr\\listado_datos.png")

        except Exception as e:
            print("Error al abrir index.php:", str(e))
            raise e

if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output='reportes_pr',
            report_name='Reporte_listado_datos_Proyecto_Personal',
            report_title='Reporte de prueba - Listado de Datos del sistema',
            combine_reports=True
        )
    )
