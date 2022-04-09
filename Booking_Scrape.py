
from dis import dis
import requests
import json
import time

import selenium

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# page is fully loaded when url is entered
def gen_location(city, state, country):
    city = city.replace(" ", "+")
    country = country.replace(" ", "+")

    location = f"{city}%2C+{country}"

    return location


def generate_url(location, Check_in, Check_out, adults, children, rooms):
    "https://www.booking.com/ss=Las+Vegas%2C+United+States+of+America&is_ski_area=&checkin_year=2022&checkin_month=4&checkin_monthday=13&checkout_year=2022&checkout_month=4&checkout_monthday=15&group_adults=1&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&dest_type=city&search_selected=true"
    Check_in = Check_in.split("/")
    Check_out = Check_out.split("/")
    url = f"https://www.booking.com/ss={location}&is_ski_area=&checkin_year={Check_in[0]}&checkin_month={Check_in[1]}&checkin_monthday={Check_in[2]}&checkout_year={Check_out[0]}&checkout_month={Check_out[1]}&checkout_monthday={Check_out[2]}&group_adults={adults}&group_children={children}&no_rooms={rooms}&b_h4u_keep_filters=&from_sf=1&dest_type=city&search_selected=true"

    return url


def scrape_hotels(url):

    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')

    driver = webdriver.Chrome(options=options)
    driver.get(url)



    hotel_names = driver.execute_script(
        "return document.getElementsByClassName(\"fcab3ed991 a23c043802\")")
    
    hotel_rating = driver.execute_script("return document.getElementsByClassName(\"b5cd09854e d10a6220b4\")")

    hotel_price = driver.execute_script("return document.getElementsByClassName(\"fcab3ed991 bd73d13072\")")
    
    #will have to every other values
    hotel_distance = driver.execute_script("return document.getElementsByClassName(\"f4bd0794db b4273d69aa\")")
    
    hotel_location = driver.execute_script("return document.getElementsByClassName(\"fc63351294 a168c6f285 e0e11a8307 a25b1d9e47\")") 

    hotel_image = driver.execute_script("return document.getElementsByClassName(\"b8b0793b0e\")")

    hotel_distance_actual = []
    
    for i in range(0,len(hotel_distance),2):
        # print(i)
        hotel_distance_actual.append(hotel_distance[i].text) 

    rental_actual = []
    for name, rating, price, dist, location, img  in zip(hotel_names, hotel_rating, hotel_price, hotel_distance_actual, hotel_location, hotel_image):
        tmp = []
        # rental_actual.append(name.text, rating.text, price.text, dist, location.get_attribute("href"))
        tmp.append(name.text)
        tmp.append(rating.text)
        tmp.append(price.text)
        tmp.append(dist)
        tmp.append(location.get_attribute("href"))
        tmp.append(img.get_attribute("src"))

        rental_actual.append(tmp)
    
    return rental_actual

def json_dump(dump):
    with open("JSON_Outputs\dump.json", "w") as f:
        json.dump(dump, f)

def main():
    location = gen_location("Las Vegas", "Nevada", "United States of America")
    check_in = "2022/4/13"
    check_out = "2022/4/15"
    adults = 1
    children = 0
    rooms = 1

    url = generate_url(location, check_in, check_out, adults, children, rooms)
    print(url)
    dump = scrape_hotels(url)
    json_dump(dump)


if __name__ == "__main__":
    main()
