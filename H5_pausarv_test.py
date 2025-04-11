import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
import time
import HtmlTestRunner
import os

class H5_pausarv_test(unittest.TestCase):

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
        self.driver.get("https://www.youtube.com")
        time.sleep(2)

    def test_pausar_video(self):
        try:
            # Aceptar cookies si aparecen
            try:
                boton_aceptar = self.driver.find_element(
                    By.XPATH, '//*[contains(text(), "Aceptar todo")]'
                )
                boton_aceptar.click()
                time.sleep(1)
            except:
                print("No se encontró el botón de cookies")

            # Buscar un video
            search_box = self.driver.find_element(By.NAME, "search_query")
            search_box.clear()
            search_box.send_keys("Programacion en python")
            search_box.submit()
            time.sleep(3)

            # Reproducir el primer video
            primer_video = self.driver.find_elements(By.CSS_SELECTOR, "ytd-video-renderer #video-title")[0]
            primer_video.click()
            time.sleep(5)

            # Pausar el video con la tecla 'k'
            body = self.driver.find_element(By.TAG_NAME, "body")
            body.send_keys("k")
            print("Video pausado con la tecla 'k'.")

            # Esperar unos segundos antes de tomar la captura
            time.sleep(2)

            # Captura de pantalla
            if not os.path.exists("fotos_pr"):
                os.makedirs("fotos_pr")
            self.driver.save_screenshot("fotos_pr\\H5_pausarv_programacion_python.png")

        except Exception as e:
            print(f"Error durante la prueba: {str(e)}")
            raise e

if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output='reportes_pr',
            report_name='Reporte_Pausar_Video_Programacion_Python',
            report_title='Reporte Pausar Video',
            descriptions=True
        )
    )
