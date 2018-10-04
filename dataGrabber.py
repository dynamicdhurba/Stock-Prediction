# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 12:58:11 2017

@author: kishor

    Description:
        This module grabs table data from merolagani.com and makes csv files.
        It contains functions only to improve performance related factors.
"""

import logging
import requests
from bs4 import BeautifulSoup
import pandas as pd


module_logger = logging.getLogger('mainApp.dataGrabber')


def grabAllData():
    """Grabs all tables(around 97) and makes corresponding csv files.
       Returns 0 if success.
    """
    
    module_logger.info('Inside dataGrabber.grabAllData()')
    
    try:
        response = requests.get('http://merolagani.com/StockQuote.aspx')
    except Exception as e:
        module_logger.warning('Error occured: {0}'.format(e))
        return 1    
    
    module_logger.info('Parsing table for symbols and their titles from link.')
    
    soup = BeautifulSoup(response.text, 'lxml')
    table_area = soup.find_all("div", {"class": "table-responsive"})
    table = table_area[0]
    links = table.find_all('a')
    
    symbol = [link.text for link in links]
    symbol_fullform = [link.get('title') for link in links]
    
    with open('data/symbol.csv', 'w') as f:
        for i,item in enumerate(symbol):
            if i is len(symbol)-1:
                f.write(item)
            else:
                f.write(item+',')

    with open('data/symbol_fullform.csv', 'w') as f:
        for i,item in enumerate(symbol_fullform):
            if i is len(symbol_fullform)-1:
                f.write(item)
            else:
                f.write(item+',')    
    
    module_logger.info('Done parsing.')
    
    
    module_logger.info('Parsing table for each 97 links.')
    for sym in symbol:
        
        try:
            response = requests.get('http://merolagani.com/CompanyDetail.aspx?symbol=%s' %sym)
        except Exception as e:
            module_logger.warning('Error occured: {0}'.format(e))
            return 1 
        
        soup = BeautifulSoup(response.text, 'lxml')
        table_area = soup.find_all("div", {"class": "table-responsive"})
        table = table_area[2]
        rows = table.find_all('tr')
        
        data_headers = None
        data_rows = list()
        
        for row in rows:
            cells = row.find_all('td')
            if cells:
                data_rows.append([cell.text for cell in cells])
            else:
                data_headers = [cell.text for cell in row.find_all('th')]
        
        df = pd.DataFrame(data_rows, columns=data_headers)
        
        module_logger.info('Completed the for loop.')
        
        df.to_csv('data/company_data/' + sym + '.csv')
        
        module_logger.info('File made.')
        
    
    module_logger.info('Done parsing and making files.')

    return 0, symbol, symbol_fullform   #success


'''
def main():
    import time
    start_time = time.time()
    grabAllData()
    print("%s seconds" %(time.time() - start_time))
    pass

if __name__ == '__main__':
    main()
'''




