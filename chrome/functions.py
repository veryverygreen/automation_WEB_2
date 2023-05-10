from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from concurrent.futures import ThreadPoolExecutor
import time

"""
i=count_str_l_menu - кол-во элементов в левом меню
y - кол-во элементов в правом подменю 
z - кол-во подменю в правом меню
"""

"""Запись ссылок в файл"""
def write_txt(pdf_url):
    with open("path_to_links.txt", "a") as file:
        file.write(pdf_url)
        file.write("\n")

"""Мультипоток"""
def thread (i):
        service = Service("path_to_driver")
        new_driver = webdriver.Chrome(service=service)
        new_driver.maximize_window()
        new_driver.get("https://www.cbr.ru")
        time.sleep(1)
        new_driver.find_element(By.XPATH,
                            "/html/body/header/div[5]/div/div/div[1]/div/div[1]/div/div").click()
        time.sleep(1)
        new_driver.find_element(By.XPATH,
                        f"/html/body/div[2]/div/div[3]/div[1]/div[1]/a[{i}]").click()
        menu(new_driver, i)
        time.sleep(0.5)
        new_driver.quit()

"""Нахождение ссылок"""
def links (count_str_r_menu, driver, i, z):
    for y in range(1, count_str_r_menu + 1):
        driver.find_element(By.XPATH,
                            f"/html/body/div[2]/div/div[3]/div[{i + 2}]/div/ul[{z}]/li[{y}]/a").click()
        time.sleep(0.5)
        pdf_links = driver.find_elements(By.XPATH, '//a[contains(@href, ".pdf")]')
        for link in pdf_links:
            pdf_url = link.get_attribute('href')
            if pdf_url.endswith('.pdf'):
                write_txt(pdf_url)
        driver.execute_script("window.history.go(-1)")
        time.sleep(1)

"Подсчет подменю в правом меню сайта"
def menu(driver, i):
    for z in range(1, 4):
        try:
            count_str_r_menu = len(driver.find_element(By.XPATH,
                                               f"/html/body/div[2]/div/div[3]/div[{i+2}]/div/ul[{z}]").text.splitlines())  # кол-во строк в правом меню
            links (count_str_r_menu, driver, i, z)
        except Exception:
            pass

"""Переходы в левом меню сайта и подсчет найденного кол-ва ссылок"""
def search_with_selenium():
    service = Service("path_to_driver")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://www.cbr.ru")
    time.sleep(2)
    driver.find_element(By.XPATH,
                        "/html/body/header/div[5]/div/div/div[1]/div/div[1]/div/div").click()
    time.sleep(1)

    count_str_l_menu = len(driver.find_element(By.XPATH,
                                               "/html/body/div[2]/div/div[3]/div[1]/div[1]").text.splitlines())  # кол-во строк в левом меню
    i=list(range(1,count_str_l_menu+1))

    with ThreadPoolExecutor() as executor:
        executor.map(thread, i)

    driver.quit()
