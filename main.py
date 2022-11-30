from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from typing import Union
from colorama import Fore


def init_driver() -> Chrome:
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = Chrome(service=Service(ChromeDriverManager().install()))

    return driver


def test_pages(sizes: Union[tuple, list], url: str, driver: Chrome):
    driver.get(url)

    for size in sizes:
        driver.set_window_size(size[0], size[1])

        try:
            header = driver.find_element(By.XPATH, '//header[contains(@class, "header")]')
            if header.size['width'] > size[0]:
                print(Fore.RED, f'[ERROR] Header вылез за пределы страницы для {size[0]}x{size[1]}')
        except NoSuchElementException:
            print(Fore.YELLOW, f'[MISSING] Header не существует на странице для {size[0]}x{size[1]} ')

        try:
            section = driver.find_element(By.XPATH, '//div[contains(@class, "section-wrapper")]')
            if section.size['width'] > size[0]:
                print(Fore.RED, f'[ERROR] Section вылез за пределы страницы для {size[0]}x{size[1]}')
        except NoSuchElementException:
            print(Fore.YELLOW, f'[MISSING] Section не существует на странице для {size[0]}x{size[1]}')

        try:
            footer = driver.find_element(By.XPATH, '//footer[contains(@class, "footer")]')
            if footer.size['width'] > size[0]:
                print(Fore.RED, f'[ERROR] Footer вылез за пределы страницы для {size[0]}x{size[1]}')
        except NoSuchElementException:
            print(Fore.YELLOW, f'[MISSING] Footer не существует на странице для {size[0]}x{size[1]}')

        print(Fore.GREEN, f'[INFO] Тест для {size[0]}x{size[1]} завершён')

    print(Fore.GREEN, '[INFO] Тесты завершены')

    input()


if __name__ == '__main__':
    driver = init_driver()
    url = 'https://ekaterinburg.premium-kuhni-shop.ru/#'

    # минимальный размер 500х875
    sizes = ((500, 875), (1366, 1024), (1920, 1080))

    test_pages(sizes, url, driver)
