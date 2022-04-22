import datetime
import selenium
import time
import json

from calendar import month
from selenium import webdriver
from selenium.webdriver.chromium import options

from multiprocessing import Pool

from pymongo import MongoClient 
import certifi

# https://www.pythonfixing.com/2021/10/fixed-webdriverexception-unknown-error.html
# pls work i hate this

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


def url_gen(offset, location, check_in, check_out, adults, children, pets):
    check_in = check_in
    check_out = check_out

    if(check_in == "" and check_out == ""):
        today = datetime.date.today()
        tomorow = today + datetime.timedelta(days=30)
        check_in = today.strftime("%Y-%m-%d")
        check_out = tomorow.strftime("%Y-%m-%d")

    # https://www.vrbo.com/search/keywords:dallas-texas-united-states/arrival:2022-04-22/departure:2022-04-30/minNightlyPrice/0/minTotalPrice/0?    filterByTotalPrice=true&petIncluded=false&ssr=true&adultsCount=1&childrenCount=1&petsCount=false

    for i in range(1, offset+1):
        url = f"https://www.vrbo.com/search/keywords:{location}/page:{i}/arrival:{check_in}/departure:{check_out}/minNightlyPrice/0/minTotalPrice/0?filterByTotalPrice=true&petIncluded=false&ssr=true&adultsCount={adults}&childrenCount={children}&petsCount=false"

        all_urls.append(url)

    return all_urls


def location_gen():
    #order is city, state, country
    input_city = input("Enter the city: ")
    input_state = input("Enter the state: ")
    input_country = "united-states"

    location = f"{input_city.lower()}-{input_state.lower()}-{input_country.lower()}"

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
    options.add_argument('--user-data-dir= /home/saikommuri')

    # when on linux use this
    #driver = webdriver.Chrome()

    driver = webdriver.Chrome(options=options)

    driver.get(url)

    curPoint = 0
    for i in range(0, 14600, 100):
        driver.execute_script(f"window.scrollTo(0,{i});")
        curPoint = i
        time.sleep(.05)

    #rental_images = driver.execute_script("return document.getElementsByClassName(\"SimpleImageCarousel__image SimpleImageCarousel__image--cur\");")
    # rental_images = driver.execute_script(
    #     "return x = document.getElementsByClassName(\"SimpleImageCarousel__image SimpleImageCarousel__image--cur\"); for(let i = 0; i<x.length; i++){ console.log(x[i].style.backgroundImage)}")

    rental_url = driver.execute_script(
        "return document.getElementsByClassName(\"media-flex__content\");")

    # get all the listings
    rental_images = driver.execute_script(
        "return document.getElementsByClassName(\"SimpleImageCarousel__image SimpleImageCarousel__image--cur\");")

    rental_names = driver.execute_script(
        "return document.getElementsByClassName(\"HitInfo__headline hover-text\");")

    rental_type = driver.execute_script(
        "return document.getElementsByClassName(\"HitInfo__type-place-details\");")

    rental_beds = driver.execute_script(
        "return document.getElementsByClassName(\"HitInfo__room-beds-details\");")

    rentals = []

    for url, image, name, type_place, beds in zip(rental_url, rental_images, rental_names, rental_type, rental_beds):
        tmp = []

        tmp.append(url.get_attribute("href"))
        tmp.append(image.get_attribute("style"))
        tmp.append(name.text)
        tmp.append(type_place.text)
        tmp.append(beds.text)

        rentals.append(tmp)

    time.sleep(.05)
    driver.close()

    return rentals


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

def database_insert(rental_actual, city1):
    # https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb
    client = MongoClient(
        "mongodb+srv://skom:access123@cluster0.5vezi.mongodb.net/test", tlsCAFile=certifi.where())
    # make a database of rentals
    db = client.rentals_test_drop

    data = city1.split(", ")
    city = data[0]
    state = data[1]

    #title, neighboorhood, review, numRev, price, price_actual, redirect, image
    for data in rental_actual:
        rental_info = {}
        rental_info["key"] = city1

        rental_info["rental_name"] = data[0]
        rental_info["neighboorhood"] = data[1]
        rental_info["rental_rating"] = data[2]

        if data[3] == []:
            rental_info["n_reviews"] = 0
        else:
            rental_info["n_reviews"] = data[3][0]

        rental_info["rental_price"] = data[4]
        rental_info["rental_amenities"] = "N/A"
        rental_info["rental_image"] = data[6]
        rental_info["room_link"] = data[7]

        rental_info["platform"] = "Hotels.com"

        db.rentals_final.insert_one(rental_info)


def main():
    # prompt_user()
    # location = location_gen()
    city_state = [
    'New York, New York', 'Honolulu, Hawaii', 'Miami, Florida', 'Hialeah, Florida', 'Miami Gardens, Florida', 'Miramar, Florida', 'Brownsville, Texas', 'Pembroke Pines, Florida', 'Hollywood, Florida', 'Davie, Florida', 'Fort Lauderdale, Florida', 'Pompano Beach, Florida', 'McAllen, Texas', 'Coral Springs, Florida', 'Edinburg, Texas', 'Cape Coral, Florida', 'West Palm Beach, Florida', 'Port St. Lucie, Florida', 'Laredo, Texas', 'Corpus Christi, Texas', 'St. Petersburg, Florida', 'Tampa, Florida', 'Clearwater, Florida', 'Palm Bay, Florida', 'Lakeland, Florida', 'Orlando, Florida', 'San Antonio, Texas', 'League City, Texas', 'Pearland, Texas', 'Sugar Land, Texas', 'Pasadena, Texas', 'Gainesville, Florida', 'Houston, Texas', 'New Orleans, Louisiana', 'Beaumont, Texas', 'Lafayette, Louisiana', 'Austin, Texas', 'Jacksonville, Florida', 'Baton Rouge, Louisiana', 'Tallahassee, Florida', 'Round Rock, Texas', 'College Station, Texas', 'Mobile, Alabama', 'Killeen, Texas', 'Waco, Texas', 'El Paso, Texas', 'Odessa, Texas', 'Savannah, Georgia', 'Midland, Texas', 'Tucson, Arizona', 'Las Cruces, New Mexico', 'Jackson, Mississippi', 'Tyler, Texas', 'Montgomery, Alabama', 'Abilene, Texas', 'Shreveport, Louisiana', 'Columbus, Georgia', 'Chula Vista, California', 'Grand Prairie, Texas', 'Arlington, Texas', 'Mesquite, Texas', 'Dallas, Texas', 'Fort Worth, Texas', 'El Cajon, California', 'Macon, Georgia', 'San Diego, California', 'Charleston, South Carolina', 'Irving, Texas', 'Garland, Texas', 'North Charleston, South Carolina', 'Richardson, Texas', 'Carrollton, Texas', 'Lewisville, Texas', 'Plano, Texas', 'Allen, Texas', 'Carlsbad, California', 'Escondido, California', 'Frisco, Texas', 'McKinney, Texas', 'Oceanside, California', 'Denton, Texas', 'Chandler, Arizona', 'Gilbert, Arizona', 'Augusta, Georgia', 'Tempe, Arizona', 'Mesa, Arizona', 'Temecula, California', 'Birmingham, Alabama', 'Glendale, Arizona', 'Lubbock, Texas', 'Phoenix, Arizona', 'Murrieta, California', 'South Fulton, Georgia', 'Surprise, Arizona', 'Irvine, California', 'Costa Mesa, California', 'Scottsdale, Arizona', 'Menifee, California', 'Huntington Beach, California', 'Santa Ana, California', 'Garden Grove, California', 'Atlanta, Georgia', 'Peoria, Arizona', 'Orange, California', 'Long Beach, California', 'Torrance, California', 'Anaheim, California', 'Corona, California', 'Fullerton, California', 'Norwalk, California', 'Wichita Falls, Texas', 'Moreno Valley, California', 'Riverside, California', 'Downey, California', 'Athens, Georgia', 'Sandy Springs, Georgia', 'Inglewood, California', 'Jurupa Valley, California', 'Los Angeles, California', 'Columbia, South Carolina', 'Ontario, California', 'Pomona, California', 'West Covina, California', 'El Monte, California', 'Fontana, California', 'Rialto, California', 'Rancho Cucamonga, California', 'San Bernardino, California', 'Pasadena, California', 'Glendale, California', 'Burbank, California', 'Thousand Oaks, California', 'Oxnard, California', 'Wilmington, North Carolina', 'Simi Valley, California', 'Ventura, California', 'Santa Clarita, California', 'Victorville, California', 'Palmdale, California', 'Lancaster, California', 'Huntsville, Alabama', 'Little Rock, Arkansas', 'Santa Maria, California', 'Chattanooga, Tennessee', 'Fayetteville, North Carolina', 'Albuquerque, New Mexico', 'Memphis, Tennessee', 'Amarillo, Texas', 'Charlotte, North Carolina', 'Norman, Oklahoma', 'Rio Rancho, New Mexico', 'Bakersfield, California', 'Concord, North Carolina', 'Oklahoma City, Oklahoma', 'Cary, North Carolina', 'Raleigh, North Carolina', 'Murfreesboro, Tennessee', 'Knoxville, Tennessee', 'Durham, North Carolina', 'High Point, North Carolina', 'Henderson, Nevada', 'Broken Arrow, Oklahoma', 'Greensboro, North Carolina', 'Winston�Salem, North Carolina', 'Tulsa, Oklahoma', 'Nashville, Tennessee', 'Las Vegas, Nevada', 'North Las Vegas, Nevada', 'Visalia, California', 'Clarksville, Tennessee', 'Chesapeake, Virginia', 'Salinas, California', 'Fresno, California', 'Virginia Beach, Virginia', 'Clovis, California', 'Norfolk, Virginia', 'Hampton, Virginia', 'Newport News, Virginia', 'Springfield, Missouri', 'Roanoke, Virginia', 'San Jose, California', 'Santa Clara, California', 'Sunnyvale, California', 'Fremont, California', 'Richmond, Virginia', 'San Mateo, California', 'Hayward, California', 'Modesto, California', 'Wichita, Kansas', 'Daly City, California', 'San Francisco, California', 'Oakland, California', 'Berkeley, California', 'Richmond, California', 'Stockton, California', 'Antioch, California', 'Concord, California', 'Evansville, Indiana', 'Lexington, Kentucky', 'Vallejo, California', 'Louisville, Kentucky', 'Fairfield, California', 'Pueblo, Colorado', 'Vacaville, California', 'Elk Grove, California', 'Santa Rosa, California', 'Sacramento, California', 'St. Louis, Missouri', 'Roseville, California', 'Alexandria, Virginia', 'Colorado Springs, Colorado', 'Overland Park, Kansas', 'Olathe, Kansas', 'Washington, District of Columbia', "Lee's Summit, Missouri", 'Columbia, Missouri', 'Topeka, Kansas', 'Independence, Missouri', 'Kansas City, Missouri', 'Kansas City, Kansas', 'Cincinnati, Ohio', 'Baltimore, Maryland', 'Reno, Nevada', 'Sparks, Nevada', 'Centennial, Colorado', 'Aurora, Colorado', 'Lakewood, Colorado', 'Chico, California', 'Denver, Colorado', 'Dayton, Ohio', 'Indianapolis, Indiana', 'Springfield, Illinois', 'Arvada, Colorado', 'Westminster, Colorado', 'Thornton, Colorado', 'Columbus, Ohio', 'Philadelphia, Pennsylvania', 'Boulder, Colorado', 'Lakewood, New Jersey', 'Provo, Utah', 'Greeley, Colorado', 'Pittsburgh, Pennsylvania', 'Edison, New Jersey', 'Fort Collins, Colorado', 'Woodbridge, New Jersey', 'Allentown, Pennsylvania', 'West Jordan, Utah', 'Elizabeth, New Jersey', 'West Valley City, Utah', 'Jersey City, New Jersey', 'Newark, New Jersey', 'Peoria, Illinois', 'Salt Lake City, Utah', 'Lincoln, Nebraska', 'Paterson, New Jersey', 'Yonkers, New York', 'Stamford, Connecticut', 'Akron, Ohio', 'Fort Wayne, Indiana', 'Bridgeport, Connecticut', 'Omaha, Nebraska', 'New Haven, Connecticut', 'Cleveland, Ohio', 'Joliet, Illinois', 'Waterbury, Connecticut', 'Davenport, Iowa', 'Des Moines, Iowa', 'New Bedford, Massachusetts', 'Toledo, Ohio', 'South Bend, Indiana', 'Naperville, Illinois', 'Hartford, Connecticut', 'Aurora, Illinois', 'Providence, Rhode Island', 'Chicago, Illinois', 'Cedar Rapids, Iowa', 'Elgin, Illinois', 'Brockton, Massachusetts', 'Springfield, Massachusetts', 'Quincy, Massachusetts', 'Rockford, Illinois', 'Worcester, Massachusetts', 'Ann Arbor, Michigan', 'Dearborn, Michigan', 'Boston, Massachusetts', 'Cambridge, Massachusetts', 'Detroit, Michigan', 'Lynn, Massachusetts', 'Warren, Michigan', 'Clinton, Michigan', 'Sterling Heights, Michigan', 'Lowell, Massachusetts', 'Lansing, Michigan', 'Buffalo, New York', 'Grand Rapids, Michigan', 'Manchester, New Hampshire', 'Syracuse, New York', 'Milwaukee, Wisconsin', 'Madison, Wisconsin', 'Rochester, New York', 'Sioux Falls, South Dakota', 'Nampa, Idaho', 'Boise, Idaho', 'Meridian, Idaho', 'Rochester, Minnesota', 'Eugene, Oregon', 'Green Bay, Wisconsin', 'Salem, Oregon', 'Saint Paul, Minnesota', 'Minneapolis, Minnesota', 'Gresham, Oregon', 'Hillsboro, Oregon', 'Portland, Oregon', 'Vancouver, Washington', 'Billings, Montana', 'Fargo, North Dakota', 'Tacoma, Washington', 'Federal Way, Washington', 'Kent, Washington', 'Renton, Washington', 'Bellevue, Washington', 'Seattle, Washington', 'Spokane Valley, Washington', 'Spokane, Washington', 'Everett, Washington', 'Anchorage, Alaska']

    location = "dallas-texas-united-states"
    params["Check-in"] = "2022-04-22"
    params["Check-out"] = "2022-04-30"
    params["adults"] = "1"
    params["children"] = "1"
    params["pets"] = "false"

    url = url_gen(3, location, params["Check-in"], params["Check-out"],
                  params["adults"], params["children"], params["pets"])

    print(url)

    # # single process
    for url in all_urls:
        scrape_vrbo(url)
        database_insert()
    #     make_json(rentals, location)


if __name__ == "__main__":
    main()
