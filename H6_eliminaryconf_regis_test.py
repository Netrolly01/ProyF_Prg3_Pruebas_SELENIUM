import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
import time
import HtmlTestRunner
import os
import re

class H6_eliminaryconf_regis_test(unittest.TestCase):

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

    def remove_non_ascii(self, text):
        """ Elimina caracteres no ASCII del texto """
        return ''.join(c for c in text if ord(c) < 128)

    def test_eliminar_contacto(self):
        try:
            # Hacer clic en el primer botón de eliminar
            boton_eliminar = self.driver.find_element(By.CLASS_NAME, "btn-eliminar")
            boton_eliminar.click()
            time.sleep(1)

            # Esperar el alert de confirmación y tomar la captura
            alert = self.driver.switch_to.alert

            # Tomar captura antes de aceptar la alerta
            if not os.path.exists("fotos_pr"):
                os.makedirs("fotos_pr")
            self.driver.save_screenshot("fotos_pr\\H4_confirmacion_eliminar_contacto.png")

            # Confirmar eliminación
            alert.accept()
            time.sleep(2)

        except Exception as e:
            print(f"Error durante la eliminación del contacto: {str(e)}")
            raise e

if __name__ == '__main__':

    def clean_report_name(report_name):
        return re.sub(r'[^\x00-\x7F]+', '', report_name)  # 
    report_name_clean = clean_report_name('Reporte_Eliminar_Contacto📝❌')

    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output='reportes_pr',
            report_name=report_name_clean
        )
    )
