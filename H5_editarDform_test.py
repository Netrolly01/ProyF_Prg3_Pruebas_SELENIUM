import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
import time
import HtmlTestRunner
import os

class H5_editarDform_test(unittest.TestCase):

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
        self.driver.get("http://localhost:8001/listadeVis.php")
        time.sleep(2)

    def test_editar_contacto(self):
        try:
            # Hacer clic en el primer botón de editar
            boton_editar = self.driver.find_element(By.CLASS_NAME, "btn-editar")
            boton_editar.click()
            time.sleep(2)

            # Modificar los campos del formulario
            nombre_input = self.driver.find_element(By.NAME, "nombre")
            telefono_input = self.driver.find_element(By.NAME, "telefono")
            correo_input = self.driver.find_element(By.NAME, "correo_electronico")

            nombre_input.clear()
            telefono_input.clear()
            correo_input.clear()

            nombre_input.send_keys("Juan")
            telefono_input.send_keys("8098765436")
            correo_input.send_keys("juan2021@gmail.com")

            # Captura de pantalla
            if not os.path.exists("fotos_pr"):
                os.makedirs("fotos_pr")
            self.driver.save_screenshot("fotos_pr\\editar_datos_formulario.png")

        except Exception as e:
            print(f"Error durante la edición del contacto: {str(e)}")
            raise e

if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output='reportes_pr',
            report_name='Reporte_Editar_Contacto'
        )
    )
