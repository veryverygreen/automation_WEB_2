"""driver.execute_script("window.history.go(-1)") Не работает в firefox!!!"""

from functions import *

with open("C:\\Users\\Алексей\\PycharmProjects\\automation_WEB_task_2\\firefox\\links.txt", "w") as file:
    file.write("")

def main():
    search_with_selenium()

if __name__ == '__main__':
    main()