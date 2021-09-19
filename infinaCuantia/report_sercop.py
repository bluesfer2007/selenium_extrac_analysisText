#generar la logica para el reporte y la colecccion de datos
import pandas
from selenium.common import exceptions
from selenium.webdriver.remote import webelement
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException


class SercopReport:
    def __init__(self, table_content_page:webelement):
        self.table_content_page=table_content_page
        self.table_row=self.pull_table()

    def pull_table(self):
        tr=[]
        for row in self.table_content_page:
            contenido=row.find_elements_by_tag_name('tr')
            for x in contenido:
                try:
                    tr.append(x.find_elements_by_tag_name('td'))
                except StaleElementReferenceException:
                    print('No encuentra en elemento td')
        return tr

    def pull_row(self):
        data=[]

        for i in range(len(self.table_row)):
            try:
                data.append([x.text for x in self.table_row[i]])
            except:
                print('Error no encuentro elemento')
        return data