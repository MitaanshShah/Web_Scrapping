from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/Users/Dell/Downloads/chromedriver_win32(2)")
browser.get(START_URL)
time.sleep(10)

def Scrape():
    headers = ["name", "distance", "mass", "radius"]
    planet_data = []
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for ul_tag in soup.find_all("ul", attrs = {"class", "List of Brightest Stars"}):
        li_tags = ul_tag.find_all("li")
        templist = []
        for index, li_tag in enumerate(li_tags):
            if index == 0:
                templist.append(li_tag.find_all("a")[0].contents[0])

            else:
                try:
                    templist.append(li_tag.contents[0])
                
                except:
                    templist.append("")
        
        planet_data.append(templist)
    
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    
    with open("name.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
Scrape()