import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
import time
import HtmlTestRunner
import os

class H3_insercionDda_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver_path = r"C:\Driver\msedgedriver.exe"
        cls.service = EdgeService(executable_path=cls.driver_path)
        cls.driver = webdriver.Edge(service=cls.service)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("http://localhost:8001/registro.php")
        time.sleep(2)

    def remove_non_ascii(self, text):
        return ''.join(c for c in text if ord(c) < 128)

    def test_insertar_datos_sin_enviar(self):
        try:
            # Insertar datos en el formulario (sin enviar)
            self.driver.find_element(By.NAME, "telefono").send_keys("8294567890")
            self.driver.find_element(By.NAME, "nombre").send_keys("Laura")
            self.driver.find_element(By.NAME, "apellido").send_keys("Martínez")
            self.driver.find_element(By.NAME, "correo_electronico").send_keys("laura.martinez@gmail.com")
            time.sleep(1)

            # Captura de pantalla sin enviar el formulario
            if not os.path.exists("fotos_pr"):
                os.makedirs("fotos_pr")
            self.driver.save_screenshot("fotos_pr\\formulario_llenado.png")

        except Exception as e:
            print(f"Error durante la prueba: {str(e)}")
            raise e

if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output='reportes_pr',
            report_name='Reporte_Formulario_Llenado'
        )
    )
