import requests
from bs4 import BeautifulSoup

class WikiWorker():
    def __init__(self):
        self._url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    # end

    # As we are not using any class properties in this function and still we are
    # sharing it across the class
    @staticmethod
    def _extract_company_symbol(page_html):
        soup = BeautifulSoup(page_html, 'lxml')
        table = soup.find(id='constituents')
        table_rows = table.find_all('tr')

        for table_row in table_rows[1:]:
            symbol = table_row.find('td').text.strip('\n')
            yield symbol

    def get_sp_500_companies(self):
        response = requests.get(self._url)

        if response.status_code != 200:
            print("Could not get entries!")
            return []

        yield from self._extract_company_symbol(response.text)