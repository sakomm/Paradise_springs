import datetime
import selenium
import time
import json

from calendar import month
from selenium import webdriver
from selenium.webdriver.chromium import options

from multiprocessing import Pool

params = {
    'location': "",
    'Check-in': "",
    'Check-out': "",
    'adults': "",
    'children': "",
    'pets': "",
}

all_urls = []
location = ""

def url_gen(offset,location, check_in, check_out, adults, children, pets):
    check_in = check_in
    check_out = check_out

    if(check_in == "" and check_out == ""):
        today = datetime.date.today()
        tomorow = today + datetime.timedelta(days=30)
        check_in = today.strftime("%Y-%m-%d")
        check_out = tomorow.strftime("%Y-%m-%d")

    # https://www.vrbo.com/search/keywords:dallas-texas-united-states/arrival:2022-04-22/departure:2022-04-30/minNightlyPrice/0/minTotalPrice/0?    filterByTotalPrice=true&petIncluded=false&ssr=true&adultsCount=1&childrenCount=1&petsCount=false

    for i in range(1, offset):
        url = f"https://www.vrbo.com/search/keywords:{location}/page:{i}/arrival:{check_in}/departure:{check_out}/minNightlyPrice/0/minTotalPrice/0?filterByTotalPrice=true&petIncluded=false&ssr=true&adultsCount={adults}&childrenCount={children}&petsCount=false"
    
        all_urls.append(url)

def location_gen():
    #order is city, state, country
    input_city = input("Enter the city: ")
    input_state = input("Enter the state: ")
    input_country = input("Enter the country: ")

    location = f"{input_city.lower()}--{input_state.lower()}--{input_country.lower()}"

    return location


def prompt_user():
    check_in = input("Enter the check in date (mm/dd/yyyy): ")
    check_out = input("Enter the check out date (mm/dd/yyyy): ")
    adults = input("Enter the number of adults: ")
    children = input("Enter the number of children: ")
    pets = input("Enter the number of pets: ")

    params["Check-in"] = check_in
    params["Check-out"] = check_out
    params["adults"] = adults
    params["children"] = children
    params["pets"] = pets

    return params


# scraping is impossible with requests library because of the way the website is designed and the way it is coded
# moving to selenium
def scrape_vrbo(url):

    # https://stackoverflow.com/questions/46744968/how-to-suppress-console-error-warning-info-messages-when-executing-selenium-pyth

    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')
    driver = webdriver.Chrome(
        executable_path=r'C:\bin\chromedriver.exe', options=options)
    driver.get(url)

    # wait for page to load

    # use selenium to scroll down the page

    # scroll through the page to load all the listings
    curPoint = 0
    for i in range(0, 14600, 100):
        driver.execute_script(f"window.scrollTo(0,{i});")
        curPoint = i
        time.sleep(.05)

    #rental_images = driver.execute_script("return document.getElementsByClassName(\"SimpleImageCarousel__image SimpleImageCarousel__image--cur\");")
    # rental_images = driver.execute_script(
    #     "return x = document.getElementsByClassName(\"SimpleImageCarousel__image SimpleImageCarousel__image--cur\"); for(let i = 0; i<x.length; i++){ console.log(x[i].style.backgroundImage)}")

    rental_images = driver.execute_script(
        "return document.getElementsByClassName(\"SimpleImageCarousel__image SimpleImageCarousel__image--cur\");")

    rental_names = driver.execute_script(
        "return document.getElementsByClassName(\"HitInfo__headline hover-text\");")

    rental_type = driver.execute_script(
        "return document.getElementsByClassName(\"HitInfo__type-place-details\");")

    rental_beds = driver.execute_script(
        "return document.getElementsByClassName(\"HitInfo__room-beds-details\");")

    rentals = []

    for image, name, type_place, beds in zip(rental_images, rental_names, rental_type, rental_beds):
        tmp = []

        tmp.append(image.get_attribute("style"))
        tmp.append(name.text)
        tmp.append(type_place.text)
        tmp.append(beds.text)

        rentals.append(tmp)

    time.sleep(.05)
    driver.close()

    make_json(rentals,location)


def make_json(full_rentals, location):
    """
    make a json file of the scraped data
    """
    # make a json file of the scraped data each property should have its own section all index 0 are tougether
    with open(f"JSON_Outputs/{location}_vrbo_scrape.json", "a") as f:

        for rentals in full_rentals:
            json.dump({"property": rentals}, f)
            f.write("\n")

    # close the file
    f.close()


def main():
    # prompt_user()
    # location = location_gen()
    location = "dallas-texas-united-states"
    params["Check-in"] = "2022-04-22"
    params["Check-out"] = "2022-04-30"
    params["adults"] = "1"
    params["children"] = "1"
    params["pets"] = "false"

    url = url_gen(3,location, params["Check-in"], params["Check-out"],
                  params["adults"], params["children"], params["pets"])

    print(url)

    #https://medium.datadriveninvestor.com/speed-up-web-scraping-using-multiprocessing-in-python-af434ff310c5
    #multi proccessing
    # with Pool(processes=3) as pool:
    #     #each process will get a url to scrape from offest 1 to 3
    #     pool.map(scrape_vrbo, all_urls)
    #     pool.terminate()
    #     pool.join()
    #     make_json(rentals, location)

    # # single process
    for url in all_urls:
        scrape_vrbo(url)
    #     make_json(rentals, location)




if __name__ == "__main__":
    main()
