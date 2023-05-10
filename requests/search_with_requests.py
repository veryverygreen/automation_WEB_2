import requests
from bs4 import BeautifulSoup

urls = ["https://www.cbr.ru/dkp/", "https://www.cbr.ru/finstab/", "https://www.cbr.ru/PSystem/", "https://www.cbr.ru/develop/","https://www.cbr.ru/fintech/",
        "https://www.cbr.ru/protection_rights/","https://www.cbr.ru/information_security/", "https://www.cbr.ru/inside/", "https://www.cbr.ru/counteraction_m_ter/",
        "https://www.cbr.ru/admissionfinmarket/", "https://www.cbr.ru/business_reputation/", "https://www.cbr.ru/ec_research/", "https://www.cbr.ru/oper_br/",
        "https://www.cbr.ru/banking_sector/", "https://www.cbr.ru/RSCI/", "https://www.cbr.ru/insurance/", "https://www.cbr.ru/securities_market/",
        "https://www.cbr.ru/issuers_corporate/", "https://www.cbr.ru/microfinance/", "https://www.cbr.ru/finm_infrastructure/", "https://www.cbr.ru/ckki/",
        "https://www.cbr.ru/key-indicators/", "https://www.cbr.ru/params/", "https://www.cbr.ru/statistics/", "https://www.cbr.ru/analytics/",
        "https://www.cbr.ru/strat_doc/", "https://www.cbr.ru/project_na/", "https://www.cbr.ru/analytics/na_vr/", "https://www.cbr.ru/na/", "https://www.cbr.ru/registries/",
        "https://www.cbr.ru/hd_base/", "https://www.cbr.ru/archive/", "https://www.cbr.ru/about_br/", "https://www.cbr.ru/about_br/ip/", "https://www.cbr.ru/about_br/publ/",
        "https://www.cbr.ru/reception/", "https://www.cbr.ru/faq/", "https://www.cbr.ru/fmp_check/", "https://www.cbr.ru/inside/warning-list/",
        "https://www.cbr.ru/lk_uio/", "https://www.cbr.ru/finorg/SiteRequirements/", "https://www.cbr.ru/explan/", "https://www.cbr.ru/certification_center_br/",
        "https://www.cbr.ru/development/"]

with open("C:\\Users\\Алексей\\PycharmProjects\\automation_WEB_task_2\\requests\\links.txt", "w") as file:
    file.write("")

def write_txt(url):
    with open("C:\\Users\\Алексей\\PycharmProjects\\automation_WEB_task_2\\requests\\links.txt", "a") as file:
        file.write(url)
        file.write("\n")

def search_with_requests():
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        for link in soup.find_all('a', href=True):
            if link['href'].endswith('.pdf'):
                pdf_url=url+link['href']
                write_txt(pdf_url)

def main():
    search_with_requests()
    count_links = sum(1 for line in open("C:\\Users\\Алексей\\PycharmProjects\\automation_WEB_task_2\\requests\\links.txt", "r"))
    print (f"Всего найдено ссылок - {count_links}")

if __name__ == '__main__':
    main()