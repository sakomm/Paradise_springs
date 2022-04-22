from multiprocessing.connection import wait
import time
import re

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pymongo import MongoClient
import certifi

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


def gen_location(city_state):
    """
    generate the location

    Ocean%20City%2C%20Maryland%2C%20United%20States%20of%20America
    """
    data = city_state.split(", ")

    input_city = data[0]
    input_state = data[1]

    input_country = "United%20States%20of%20America"

    input_city = input_city.replace(" ", "%20")
    input_state = input_state.replace(" ", "%20")

    location = f"{input_city}%2C%20{input_state}%2C%20{input_country}"

    return location


def scrape_hotels(url):

    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')

    driver = webdriver.Chrome(
        executable_path=r'C:\bin\chromedriver.exe', options=options)

    driver.get(url)

    time.sleep(.5)
    curPoint = 0
    # load all the stupid ajax
    for i in range(0, 19000, 100):
        driver.execute_script(f"window.scrollTo(0,{i});")
        curPoint = i
        time.sleep(.2)

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
        n_reviews.append((re.findall("\(([^()]+)", text)))

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

    for title, neighboorhood, review, numRev, price, price_actual, redirect, image in zip(title_hotel, hotel_neighboorhood, hotel_review, n_reviews, price, price_actual, url_redirect, image_redirect):
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

    # def gen_url(location,Check_in,Check_out,adults,rooms):

    # city_state = [
    #     'New York, New York', 'Honolulu, Hawaii', 'Miami, Florida', 'Hialeah, Florida', 'Miami Gardens, Florida', 'Miramar, Florida', 'Brownsville, Texas', 'Pembroke Pines, Florida', 'Hollywood, Florida', 'Davie, Florida', 'Fort Lauderdale, Florida', 'Pompano Beach, Florida', 'McAllen, Texas', 'Coral Springs, Florida', 'Edinburg, Texas', 'Cape Coral, Florida', 'West Palm Beach, Florida', 'Port St. Lucie, Florida', 'Laredo, Texas', 'Corpus Christi, Texas', 'St. Petersburg, Florida', 'Tampa, Florida', 'Clearwater, Florida', 'Palm Bay, Florida', 'Lakeland, Florida', 'Orlando, Florida', 'San Antonio, Texas', 'League City, Texas', 'Pearland, Texas', 'Sugar Land, Texas', 'Pasadena, Texas', 'Gainesville, Florida', 'Houston, Texas', 'New Orleans, Louisiana', 'Beaumont, Texas', 'Lafayette, Louisiana', 'Austin, Texas', 'Jacksonville, Florida', 'Baton Rouge, Louisiana', 'Tallahassee, Florida', 'Round Rock, Texas', 'College Station, Texas', 'Mobile, Alabama', 'Killeen, Texas', 'Waco, Texas', 'El Paso, Texas', 'Odessa, Texas', 'Savannah, Georgia', 'Midland, Texas', 'Tucson, Arizona', 'Las Cruces, New Mexico', 'Jackson, Mississippi', 'Tyler, Texas', 'Montgomery, Alabama', 'Abilene, Texas', 'Shreveport, Louisiana', 'Columbus, Georgia', 'Chula Vista, California', 'Grand Prairie, Texas', 'Arlington, Texas', 'Mesquite, Texas', 'Dallas, Texas', 'Fort Worth, Texas', 'El Cajon, California', 'Macon, Georgia', 'San Diego, California', 'Charleston, South Carolina', 'Irving, Texas', 'Garland, Texas', 'North Charleston, South Carolina', 'Richardson, Texas', 'Carrollton, Texas', 'Lewisville, Texas', 'Plano, Texas', 'Allen, Texas', 'Carlsbad, California', 'Escondido, California', 'Frisco, Texas', 'McKinney, Texas', 'Oceanside, California', 'Denton, Texas', 'Chandler, Arizona', 'Gilbert, Arizona', 'Augusta, Georgia', 'Tempe, Arizona', 'Mesa, Arizona', 'Temecula, California', 'Birmingham, Alabama', 'Glendale, Arizona', 'Lubbock, Texas', 'Phoenix, Arizona', 'Murrieta, California', 'South Fulton, Georgia', 'Surprise, Arizona', 'Irvine, California', 'Costa Mesa, California', 'Scottsdale, Arizona', 'Menifee, California', 'Huntington Beach, California', 'Santa Ana, California', 'Garden Grove, California', 'Atlanta, Georgia', 'Peoria, Arizona', 'Orange, California', 'Long Beach, California', 'Torrance, California', 'Anaheim, California', 'Corona, California', 'Fullerton, California', 'Norwalk, California', 'Wichita Falls, Texas', 'Moreno Valley, California', 'Riverside, California', 'Downey, California', 'Athens, Georgia', 'Sandy Springs, Georgia', 'Inglewood, California', 'Jurupa Valley, California', 'Los Angeles, California', 'Columbia, South Carolina', 'Ontario, California', 'Pomona, California', 'West Covina, California', 'El Monte, California', 'Fontana, California', 'Rialto, California', 'Rancho Cucamonga, California', 'San Bernardino, California', 'Pasadena, California', 'Glendale, California', 'Burbank, California', 'Thousand Oaks, California', 'Oxnard, California', 'Wilmington, North Carolina', 'Simi Valley, California', 'Ventura, California', 'Santa Clarita, California', 'Victorville, California', 'Palmdale, California', 'Lancaster, California', 'Huntsville, Alabama', 'Little Rock, Arkansas', 'Santa Maria, California', 'Chattanooga, Tennessee', 'Fayetteville, North Carolina', 'Albuquerque, New Mexico', 'Memphis, Tennessee', 'Amarillo, Texas', 'Charlotte, North Carolina', 'Norman, Oklahoma', 'Rio Rancho, New Mexico', 'Bakersfield, California', 'Concord, North Carolina', 'Oklahoma City, Oklahoma', 'Cary, North Carolina', 'Raleigh, North Carolina', 'Murfreesboro, Tennessee', 'Knoxville, Tennessee', 'Durham, North Carolina', 'High Point, North Carolina', 'Henderson, Nevada', 'Broken Arrow, Oklahoma', 'Greensboro, North Carolina', 'Winston�Salem, North Carolina', 'Tulsa, Oklahoma', 'Nashville, Tennessee', 'Las Vegas, Nevada', 'North Las Vegas, Nevada', 'Visalia, California', 'Clarksville, Tennessee', 'Chesapeake, Virginia', 'Salinas, California', 'Fresno, California', 'Virginia Beach, Virginia', 'Clovis, California', 'Norfolk, Virginia', 'Hampton, Virginia', 'Newport News, Virginia', 'Springfield, Missouri', 'Roanoke, Virginia', 'San Jose, California', 'Santa Clara, California', 'Sunnyvale, California', 'Fremont, California', 'Richmond, Virginia', 'San Mateo, California', 'Hayward, California', 'Modesto, California', 'Wichita, Kansas', 'Daly City, California', 'San Francisco, California', 'Oakland, California', 'Berkeley, California', 'Richmond, California', 'Stockton, California', 'Antioch, California', 'Concord, California', 'Evansville, Indiana', 'Lexington, Kentucky', 'Vallejo, California', 'Louisville, Kentucky', 'Fairfield, California', 'Pueblo, Colorado', 'Vacaville, California', 'Elk Grove, California', 'Santa Rosa, California', 'Sacramento, California', 'St. Louis, Missouri', 'Roseville, California', 'Alexandria, Virginia', 'Colorado Springs, Colorado', 'Overland Park, Kansas', 'Olathe, Kansas', 'Washington, District of Columbia', "Lee's Summit, Missouri", 'Columbia, Missouri', 'Topeka, Kansas', 'Independence, Missouri', 'Kansas City, Missouri', 'Kansas City, Kansas', 'Cincinnati, Ohio', 'Baltimore, Maryland', 'Reno, Nevada', 'Sparks, Nevada', 'Centennial, Colorado', 'Aurora, Colorado', 'Lakewood, Colorado', 'Chico, California', 'Denver, Colorado', 'Dayton, Ohio', 'Indianapolis, Indiana', 'Springfield, Illinois', 'Arvada, Colorado', 'Westminster, Colorado', 'Thornton, Colorado', 'Columbus, Ohio', 'Philadelphia, Pennsylvania', 'Boulder, Colorado', 'Lakewood, New Jersey', 'Provo, Utah', 'Greeley, Colorado', 'Pittsburgh, Pennsylvania', 'Edison, New Jersey', 'Fort Collins, Colorado', 'Woodbridge, New Jersey', 'Allentown, Pennsylvania', 'West Jordan, Utah', 'Elizabeth, New Jersey', 'West Valley City, Utah', 'Jersey City, New Jersey', 'Newark, New Jersey', 'Peoria, Illinois', 'Salt Lake City, Utah', 'Lincoln, Nebraska', 'Paterson, New Jersey', 'Yonkers, New York', 'Stamford, Connecticut', 'Akron, Ohio', 'Fort Wayne, Indiana', 'Bridgeport, Connecticut', 'Omaha, Nebraska', 'New Haven, Connecticut', 'Cleveland, Ohio', 'Joliet, Illinois', 'Waterbury, Connecticut', 'Davenport, Iowa', 'Des Moines, Iowa', 'New Bedford, Massachusetts', 'Toledo, Ohio', 'South Bend, Indiana', 'Naperville, Illinois', 'Hartford, Connecticut', 'Aurora, Illinois', 'Providence, Rhode Island', 'Chicago, Illinois', 'Cedar Rapids, Iowa', 'Elgin, Illinois', 'Brockton, Massachusetts', 'Springfield, Massachusetts', 'Quincy, Massachusetts', 'Rockford, Illinois', 'Worcester, Massachusetts', 'Ann Arbor, Michigan', 'Dearborn, Michigan', 'Boston, Massachusetts', 'Cambridge, Massachusetts', 'Detroit, Michigan', 'Lynn, Massachusetts', 'Warren, Michigan', 'Clinton, Michigan', 'Sterling Heights, Michigan', 'Lowell, Massachusetts', 'Lansing, Michigan', 'Buffalo, New York', 'Grand Rapids, Michigan', 'Manchester, New Hampshire', 'Syracuse, New York', 'Milwaukee, Wisconsin', 'Madison, Wisconsin', 'Rochester, New York', 'Sioux Falls, South Dakota', 'Nampa, Idaho', 'Boise, Idaho', 'Meridian, Idaho', 'Rochester, Minnesota', 'Eugene, Oregon', 'Green Bay, Wisconsin', 'Salem, Oregon', 'Saint Paul, Minnesota', 'Minneapolis, Minnesota', 'Gresham, Oregon', 'Hillsboro, Oregon', 'Portland, Oregon', 'Vancouver, Washington', 'Billings, Montana', 'Fargo, North Dakota', 'Tacoma, Washington', 'Federal Way, Washington', 'Kent, Washington', 'Renton, Washington', 'Bellevue, Washington', 'Seattle, Washington', 'Spokane Valley, Washington', 'Spokane, Washington', 'Everett, Washington', 'Anchorage, Alaska'
    # ]
    #'Davie, Florida', 'Fort Lauderdale, Florida', 'Pompano Beach, Florida', 'McAllen, Texas', 'Coral Springs, Florida', 'Edinburg, Texas', 'Cape Coral, Florida', 'West Palm Beach, Florida', 'Port St. Lucie, Florida', 'Laredo, Texas',

    city_state = ['Oklahoma City, Oklahoma', 'Cary, North Carolina', 'Raleigh, North Carolina', 'Murfreesboro, Tennessee', 'Knoxville, Tennessee'
    ]
     #'Durham, North Carolina', 'High Point, North Carolina', 'Henderson, Nevada', 'Broken Arrow, Oklahoma', 'Greensboro, North Carolina', 'Winston Salem, North Carolina', 'Tulsa, Oklahoma', 'Nashville, Tennessee', 'Las Vegas, Nevada', 'North Las Vegas, Nevada', 'Visalia, California', 'Clarksville, Tennessee', 'Chesapeake, Virginia', 'Salinas, California', 'Fresno, California', 'Virginia Beach, Virginia', 'Clovis, California', 'Norfolk, Virginia', 'Hampton, Virginia', 'Newport News, Virginia', 'Springfield, Missouri', 'Roanoke, Virginia', 'San Jose, California', 'Santa Clara, California', 'Sunnyvale, California', 'Fremont, California', 'Richmond, Virginia', 'San Mateo, California', 'Hayward, California', 'Modesto, California', 'Wichita, Kansas', 'Daly City, California', 'San Francisco, California', 'Oakland, California', 'Berkeley, California', 'Richmond, California', 'Stockton, California', 'Antioch, California', 'Concord, California', 'Evansville, Indiana', 'Lexington, Kentucky', 'Vallejo, California', 'Louisville, Kentucky', 'Fairfield, California', 'Pueblo, Colorado', 'Vacaville, California', 'Elk Grove, California', 'Santa Rosa, California', 'Sacramento, California', 'St. Louis, Missouri', 'Roseville, California', 'Alexandria, Virginia', 'Colorado Springs, Colorado', 'Overland Park, Kansas', 'Olathe, Kansas', 'Washington, District of Columbia', "Lee's Summit, Missouri", 'Columbia, Missouri', 'Topeka, Kansas', 'Independence, Missouri', 'Kansas City, Missouri', 'Kansas City, Kansas', 'Cincinnati, Ohio', 'Baltimore, Maryland', 'Reno, Nevada', 'Sparks, Nevada', 'Centennial, Colorado', 'Aurora, Colorado', 'Lakewood, Colorado', 'Chico, California', 'Denver, Colorado', 'Dayton, Ohio', 'Indianapolis, Indiana', 'Springfield, Illinois', 'Arvada, Colorado', 'Westminster, Colorado', 'Thornton, Colorado', 'Columbus, Ohio', 'Philadelphia, Pennsylvania', 'Boulder, Colorado', 'Lakewood, New Jersey', 'Provo, Utah', 'Greeley, Colorado', 'Pittsburgh, Pennsylvania', 'Edison, New Jersey', 'Fort Collins, Colorado', 'Woodbridge, New Jersey', 'Allentown, Pennsylvania', 'West Jordan, Utah', 'Elizabeth, New Jersey', 'West Valley City, Utah', 'Jersey City, New Jersey', 'Newark, New Jersey', 'Peoria, Illinois', 'Salt Lake City, Utah', 'Lincoln, Nebraska', 'Paterson, New Jersey', 'Yonkers, New York', 'Stamford, Connecticut', 'Akron, Ohio', 'Fort Wayne, Indiana', 'Bridgeport, Connecticut', 'Omaha, Nebraska', 'New Haven, Connecticut', 'Cleveland, Ohio', 'Joliet, Illinois', 'Waterbury, Connecticut', 'Davenport, Iowa', 'Des Moines, Iowa', 'New Bedford, Massachusetts', 'Toledo, Ohio', 'South Bend, Indiana', 'Naperville, Illinois', 'Hartford, Connecticut', 'Aurora, Illinois', 'Providence, Rhode Island', 'Chicago, Illinois', 'Cedar Rapids, Iowa', 'Elgin, Illinois', 'Brockton, Massachusetts', 'Springfield, Massachusetts', 'Quincy, Massachusetts', 'Rockford, Illinois', 'Worcester, Massachusetts', 'Ann Arbor, Michigan', 'Dearborn, Michigan', 'Boston, Massachusetts', 'Cambridge, Massachusetts', 'Detroit, Michigan', 'Lynn, Massachusetts', 'Warren, Michigan', 'Clinton, Michigan', 'Sterling Heights, Michigan', 'Lowell, Massachusetts', 'Lansing, Michigan', 'Buffalo, New York', 'Grand Rapids, Michigan', 'Manchester, New Hampshire', 'Syracuse, New York', 'Milwaukee, Wisconsin', 'Madison, Wisconsin', 'Rochester, New York', 'Sioux Falls, South Dakota', 'Nampa, Idaho', 'Boise, Idaho', 'Meridian, Idaho', 'Rochester, Minnesota', 'Eugene, Oregon', 'Green Bay, Wisconsin', 'Salem, Oregon', 'Saint Paul, Minnesota', 'Minneapolis, Minnesota', 'Gresham, Oregon', 'Hillsboro, Oregon', 'Portland, Oregon', 'Vancouver, Washington', 'Billings, Montana', 'Fargo, North Dakota', 'Tacoma, Washington', 'Federal Way, Washington', 'Kent, Washington', 'Renton, Washington', 'Bellevue, Washington', 'Seattle, Washington', 'Spokane Valley, Washington', 'Spokane, Washington', 'Everett, Washington', 'Anchorage, Alaska'
    for city in city_state:
        location = gen_location(city)
        url = gen_url(location, "2022-04-23", "2022-04-24", "2", "1")

        data = scrape_hotels(url)
        database_insert(data, city)

        print(f"{city} is done")


if __name__ == "__main__":
    main()
