from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import pandas as pd
from datetime import datetime, timedelta

browser = webdriver.Chrome(executable_path="chromedriver.exe")
url = "https://covid19.gov.vn/"
if __name__ == "__main__":
    browser.get(url)
    sleep(2)

    try:
        list_city = []
        total = [] 
        daynow = []
        die = []
        
        browser.switch_to.frame(1)
        all_rows = browser.find_elements_by_class_name("row")
        for row in all_rows:
            list_city.append(row.find_element_by_class_name("city").text)
            total.append(row.find_element_by_class_name("total").text.replace('.',''))
            daynow.append(row.find_element_by_class_name("daynow").text.replace('.','').replace('+', ''))
            die.append(row.find_element_by_class_name("die").text.replace('.',''))
        # print(total)
        df = pd.DataFrame({"Thành phố": list_city, "Tổng số ca": total, "Tổng số ca(24h)": daynow, "Tử vong": die})
        df[1:].to_csv('covid.csv')
    except Exception as e:
        print("Error: {}".format(e))