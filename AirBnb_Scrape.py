from ctypes import Union
import sys
import requests
import bs4
import json
import datetime as dt

from pymongo import MongoClient
import certifi

params = {
    'location': "",
    'Check-in': "",
    'Check-out': "",
    'adults': "",
    'children': "",
    'infants': "",
}

# TODO --> Offset to handle the webpages

"""
Consturct the URL to scrape from the parameters
https://www.airbnb.com/s/Charlottesville--Virginia--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=march&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Charlottesville%2C%20Virginia%2C%20United%20States&place_id=ChIJj6RQ6i2Gs4kR_HSLw5bwhpA&adults=1&children=1&infants=1
"""


def construct_url(location, Checkin, Checkout, adults, children, infants):
    params["location"] = location
    params["Check-in"] = Checkin
    params["Check-out"] = Checkout
    params["adults"] = adults
    params["children"] = children
    params["infants"] = infants

    url = f"https://www.airbnb.com/s/{params['location']}/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D={params['Check-in']}&flexible_trip_dates%5B%5D={params['Check-out']}&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query={params['location']}&{params['adults']}&children={params['children']}&infants={params['infants']}"

    return url


def construct_location(loc):
    #order is city, state, country

    loc = loc.split(",")
    # remove all the spaces
    loc = [x.strip() for x in loc]

    location = f"{loc[0]}--{loc[1]}--USA"

    return location


"""
get price of the property parse string and get the price

given $122\xa0/ night$122 per night' is $122 per night
"""


def get_price(str_price):
    ppn = str_price.split(" ")
    str_price = (f"{ppn[-3][5::]} {ppn[-2]} {ppn[-1]}")

    return str_price


def scrape_page(url):
    # print(url)
    # print(params)

    # get all the names of the properties and store in json file
    # content seems to be stored in a nested class called _8ssblpx and _gig1e7 cause that make sense somehow???????

    # get the html of the page
    page = requests.get(url)
    # print(page.text) dont run that, fucking takes forever
    # parse the html
    content = page.content
    # print(content)
    soup = bs4.BeautifulSoup(content, "html.parser")

    # get all attributes of the class _8ssblpx and its child _gig1e7
    parent = soup.find_all("div", class_="_8ssblpx")
    child = soup.find_all("div", class_="_gig1e7")

    full_rentals = []

    for prop in child:
        header = prop.find("div", class_="mj1p6c8 dir dir-ltr").text
        name = prop.find("div", class_="c1bx80b8 dir dir-ltr").text
        price = get_price(prop.find("div", class_="p1qe1cgb dir dir-ltr").text)
        try:
            ratings = prop.find("div", class_="sglmc5a dir dir-ltr").text
        except:
            ratings = "No ratings"

        amen_r1 = prop.find_all(
            "div", class_="i1wgresd dir dir-ltr")[0].text.split("·")

        try:
            amen_r2 = prop.find_all(
                "div", class_="i1wgresd dir dir-ltr")[1].text.split("·")
        except:
            amen_r2 = "No amenities"

        room_link = prop.find(
            "div", class_="cm4lcvy dir dir-ltr").find("a").get("href")
        room_link = f"https://www.airbnb.com{room_link}"

        image_link = prop.find("div", class_="_4626ulj").find("img").get("src")

        tmp = [header, name, price, ratings,
               amen_r1, amen_r2, room_link, image_link]
        full_rentals.append(tmp)

    # pprint(full_rentals)
    return full_rentals


def make_json(full_rentals, location):
    """
    make a json file of the scraped data
    """
    # make a json file of the scraped data each property should have its own section all index 0 are tougether
    with open(f"JSON_Outputs\{location}_airbnb_scrape.json", "a") as f:

        for rentals in full_rentals:
            json.dump({"property": rentals}, f)
            f.write("\n")

    # close the file
    f.close()


def database_insert(rental_actual, city):
    # https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb
    client = MongoClient(
        "mongodb+srv://skom:access123@cluster0.5vezi.mongodb.net/test", tlsCAFile=certifi.where())
    # make a database of rentals
    db = client.rentals_test_drop

    # tmp = [header, name, price, ratings,
    #        amen_r1, amen_r2, room_link, image_link]

    for data in rental_actual:
        rental_info = {}
        rental_info["key"] = city

        rental_info["rental_name"] = data[1]
        rental_info["rental_price"] = data[2]
        rental_info["rental_rating"] = data[3]
        amenities = []
        for amen in data[4]:
            amenities.append(amen)
        for amen in data[5]:
            amenities.append(amen)
        rental_info["rental_amenities"] = amenities
        rental_info["room_link"] = data[6]
        rental_info["rental_image"] = data[7]
        rental_info["platform"] = "AirBnb"

        #! CHANGE BACK TO db.rentals.insert_one(rental_info) after testing is complete IMPORTANT
        db.testing.insert_one(rental_info)


def main():

    #city_state = ['Allentown, Pennsylvania', 'West Jordan, Utah', 'Elizabeth, New Jersey', 'West Valley City, Utah', 'Jersey City, New Jersey', 'Newark, New Jersey', 'Peoria, Illinois', 'Salt Lake City, Utah', 'Lincoln, Nebraska', 'Paterson, New Jersey', 'Yonkers, New York', 'Stamford, Connecticut', 'Akron, Ohio', 'Fort Wayne, Indiana', 'Bridgeport, Connecticut', 'Omaha, Nebraska', 'New Haven, Connecticut', 'Cleveland, Ohio', 'Joliet, Illinois', 'Waterbury, Connecticut', 'Davenport, Iowa', 'Des Moines, Iowa', 'New Bedford, Massachusetts', 'Toledo, Ohio', 'South Bend, Indiana', 'Naperville, Illinois', 'Hartford, Connecticut', 'Aurora, Illinois', 'Providence, Rhode Island', 'Chicago, Illinois', 'Cedar Rapids, Iowa', 'Elgin, Illinois', 'Brockton, Massachusetts', 'Springfield, Massachusetts', 'Quincy, Massachusetts', 'Rockford, Illinois', 'Worcester, Massachusetts', 'Ann Arbor, Michigan', 'Dearborn, Michigan', 'Boston, Massachusetts', 'Cambridge, Massachusetts', 'Detroit, Michigan', 'Lynn, Massachusetts', 'Warren, Michigan', 'Clinton, Michigan', 'Sterling Heights, Michigan', 'Lowell, Massachusetts', 'Lansing, Michigan', 'Buffalo, New York', 'Grand Rapids, Michigan', 'Manchester, New Hampshire', 'Syracuse, New York', 'Milwaukee, Wisconsin', 'Madison, Wisconsin', 'Rochester, New York', 'Sioux Falls, South Dakota', 'Nampa, Idaho', 'Boise, Idaho', 'Meridian, Idaho', 'Rochester, Minnesota', 'Eugene, Oregon', 'Green Bay, Wisconsin', 'Salem, Oregon', 'Saint Paul, Minnesota', 'Minneapolis, Minnesota', 'Gresham, Oregon', 'Hillsboro, Oregon', 'Portland, Oregon', 'Vancouver, Washington', 'Billings, Montana', 'Fargo, North Dakota', 'Tacoma, Washington', 'Federal Way, Washington', 'Kent, Washington', 'Renton, Washington', 'Bellevue, Washington', 'Seattle, Washington', 'Spokane Valley, Washington', 'Spokane, Washington', 'Everett, Washington', 'Anchorage, Alaska']
    city_state = ['Allentown, Pennsylvania']

    for city in city_state:
        location = construct_location(city)
        # Checkin = sys.argv[2]
        # Checkout = sys.argv[3]
        adults = "1"
        children = "1"
        infants = "0"

        # make checkin current month
        Checkin = dt.datetime.now().strftime("%B")
        # make checkout next month
        month_plus = dt.datetime.now() + dt.timedelta(days=4)
        Checkout = month_plus.strftime("%B")

        # print(f"Checkin: {Checkin} && Checkout: {Checkout}")

        url = construct_url(location, Checkin, Checkout,
                            adults, children, infants)

        # CHANGE BACK TO 15 after testing is complete
        for i in range(1):
            offset = 20 * i
            url_offset = f"{url}&offset={offset}"

            full_rentals = scrape_page(url_offset)
            database_insert(full_rentals, city)
        print(f"{city} is done\n")

    print("done")


if __name__ == "__main__":
    main()
