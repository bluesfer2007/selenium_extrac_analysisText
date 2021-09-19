import os
import pandas as pd
import selenium
import infinaCuantia.contants as conts
from selenium import webdriver
from infinaCuantia.report_sercop import SercopReport

class Sercop(webdriver.Chrome):
    def __init__(self, driver_path='D:\driver_sel', teardown=False):
        self.driver_path=driver_path
        self.teardonw=teardown
        os.environ['PATH']+=os.pathsep+self.driver_path
      
        super(Sercop, self).__init__()

        self.maximize_window()
        self.implicitly_wait(8)

    def __exit__(self, exce_type, exc_val, exc_tb):
        if self.teardonw:
            self.quit()

    def get_url_sercop(self):
        self.get(conts.BASE_URL)

    def next_page(self):
        next_button=self.find_element_by_id('table_id_next')
        next_button.click()

    #extraer datos
    def sercop_report(self,i):
        test=[]
        content_table=self.find_elements_by_css_selector('tbody')
        report=SercopReport(content_table)
        data=report.pull_row()
        self._save_in_disk(data,i)
        #data

    def _save_in_disk(self, data,i):
        cols=['Código Necesidad', 'Fecha_Public', 'Provincia','Descripción Necesidad', 'Status', 'Fecha limite', 'EntidadContrato', 'Dir_Entrega', 'Contacto']
        df=pd.DataFrame(data,columns=cols)

        return df.to_csv('basedatos/data'+str(i)+'.csv')
