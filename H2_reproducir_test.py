import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
import time
import HtmlTestRunner
import os

class H2_reproducir_test(unittest.TestCase):

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

    def remove_non_ascii(self, text):
        return ''.join(c for c in text if ord(c) < 128)

    def test_busqueda_youtube_reproducir_video(self):
        try:
            # Aceptar cookies
            try:
                boton_aceptar = self.driver.find_element(
                    By.XPATH, '//*[contains(text(), "Aceptar todo")]'
                )
                boton_aceptar.click()
                time.sleep(1)
            except:
                print("No se encontró el botón de cookies")

            # Buscar "Programacion en python"
            search_box = self.driver.find_element(By.NAME, "search_query")
            search_box.clear()
            search_box.send_keys("Programacion en python")
            search_box.submit()
            time.sleep(3)

            # Obtener resultados
            resultados = self.driver.find_elements(
                By.CSS_SELECTOR, "ytd-video-renderer #video-title"
            )
            self.assertGreater(len(resultados), 0, "ERROR: No se encontraron videos")
            print(f"Videos encontrados: {len(resultados)}")

            # Mostrar títulos sin emojis
            for i, video in enumerate(resultados[:3]):
                titulo_limpio = self.remove_non_ascii(video.text)
                print(f"{i+1}. {titulo_limpio}")

            # Hacer clic en el primer video
            print("Reproduciendo el primer video...")
            resultados[0].click()
            time.sleep(10)  # Espera 10 segundos para que se reproduzca

            # Captura de pantalla del video reproduciéndose
            if not os.path.exists("fotos_pr"):
                os.makedirs("fotos_pr")
            self.driver.save_screenshot("fotos_pr\\H2_video_reproduciendo.png")

        except Exception as e:
            print(f"Error durante la prueba: {str(e)}")
            raise e

if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output='reportes_pr',
            report_name='Reporte_Reproducir_Programacion_Python'
        )
    )
