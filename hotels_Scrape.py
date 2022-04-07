import json
from multiprocessing.connection import wait
import time
import re 

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

input_city1 = ""

params = {
    "Check-in": "",
    "Check-out": "",
    "adults": "",
    "children": "",
    "pets": ""
}


def gen_url(location, Check_in, Check_out, adults, rooms):
    """
    generate the url for the location

    https://www.hotels.com/Hotel-Search?adults=2&d1=2022-04-20&d2=2022-04-21&destination=Ocean%20City%2C%20Maryland%2C%20United%20States%20of%20America&endDate=2022-04-21&latLong=38.378116%2C-75.087754&regionId=9151&rooms=1&semdtl=&sort=RECOMMENDED&startDate=2022-04-20&theme=&useRewards=false&userIntent=
    """
    url = f"https://www.hotels.com/Hotel-Search?adults={adults}&d1={Check_in}&d2={Check_out}&destination={location}&endDate={Check_out}&rooms={rooms}&semdtl=&sort=RECOMMENDED&startDate={Check_in}&theme=&useRewards=false&userIntent="

    return url


def gen_location():
    """
    generate the location

    Ocean%20City%2C%20Maryland%2C%20United%20States%20of%20America
    """
    input_city1 = input("Enter the city: ")
    input_state = input("Enter the state: ")
    input_country = "United%20States%20of%20America"

    input_city = input_city1.replace(" ", "%20")
    input_state = input_state.replace(" ", "%20")
    input_country = input_country.replace(" ", "%20")

    location = f"{input_city}%2C%20{input_state}%2C%20{input_country}"

    return location


def scrape_hotels(url):

    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')

    # when on linux use this
    # driver = webdriver.Chrome()

    driver = webdriver.Chrome(
        executable_path=r'C:\bin\chromedriver.exe', options=options)

    driver.get(url)

    time.sleep(.5)
    curPoint = 0
    # load all the stupid ajax
    for i in range(0, 19000, 100):
        driver.execute_script(f"window.scrollTo(0,{i});")
        curPoint = i
        time.sleep(.05)

    rental_package = []

    title_hotel = driver.execute_script(
        "return document.getElementsByClassName(\"uitk-heading-5 is-visually-hidden\")")
    hotel_neighboorhood = driver.execute_script(
        "return document.getElementsByClassName(\"uitk-text overflow-wrap uitk-type-300 uitk-spacing uitk-spacing-padding-blockend-two uitk-text-default-theme\")")
    hotel_review = driver.execute_script(
        "return document.getElementsByClassName(\"uitk-type-300 uitk-type-bold all-r-padding-one\")")

    # get elements between paren()
    num_review = driver.execute_script(
        "return document.getElementsByClassName(\"listing__reviews all-t-margin-two\")")

    n_reviews = []
    for review in num_review:
        # text is 3.1/5 (763 reviews) need 763 reviews
        text = review.text
        n_reviews.append((re.findall("\(([^()]+)",text)))

    price = driver.execute_script(
        "return document.getElementsByClassName(\"uitk-text uitk-type-600 uitk-type-bold uitk-text-emphasis-theme\")")
    
    price_actual = driver.execute_script(
        "return document.getElementsByClassName(\"uitk-text uitk-type-end uitk-type-200 uitk-text-default-theme\")")

    url_redirect = driver.execute_script(
        "return document.getElementsByClassName(\"listing__link uitk-card-link\")"
    )

    image_redirect = driver.execute_script(
        "return document.querySelectorAll('img[alt=\"Primary image\"]')"
    )

    for title, neighboorhood, review, numRev, price, price_actual, redirect, image in zip(title_hotel,hotel_neighboorhood,hotel_review, n_reviews, price,price_actual, url_redirect, image_redirect):
        tmp = []

        tmp.append(title.text)
        tmp.append(neighboorhood.text)
        tmp.append(review.text)
        tmp.append(numRev)
        tmp.append(price.text)
        tmp.append(price_actual.text)
        image_redirect = image.get_attribute("src")
        tmp.append(image_redirect)
        href_target = redirect.get_attribute("href")
        tmp.append(href_target)

        rental_package.append(tmp)

    driver.close()

    return rental_package

def make_json(full_rentals, location):
    """
    make a json file of the scraped data
    """
    # make a json file of the scraped data each property should have its own section all index 0 are tougether
    with open(f"JSON_Outputs/{location}_hotels_scrape.json", "a") as f:

        for rentals in full_rentals:
            json.dump({"property": rentals}, f)
            f.write("\n")

    # close the file
    f.close()

def main():

    # def gen_url(location,Check_in,Check_out,adults,rooms):
    location = gen_location()
    url = gen_url(location, "2022-04-20", "2022-04-21", "2", "1")

    print(url)
    json_data = scrape_hotels(url)
    make_json(json_data, "test")


if __name__ == "__main__":
    main()
