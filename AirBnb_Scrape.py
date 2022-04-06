import sys
import requests
import bs4
import json
import datetime as dt

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


def construct_location():
    #order is city, state, country
    input_city = input("Enter the city: ")
    input_state = input("Enter the state: ")
    input_country = input("Enter the country: ")

    location = f"{input_city.lower()}--{input_state.lower()}--{input_country.lower()}"

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
    with open(f"/home/saikommuri/Documents/CoDiNG_GeNiuS/Paradise_springs/JSON_Outputs/{location}_airbnb_scrape.json", "a") as f:

        for rentals in full_rentals:
            json.dump({"property": rentals}, f)
            f.write("\n")

    # close the file
    f.close()


def main():

    # location = construct_location()
    # Checkin = input("Enter the checkin date or press enter: ")
    # Checkout = input("Enter the checkout date or press enter: ")
    # adults = input("Enter the number of adults: ")
    # children = input("Enter the number of children: ")
    # infants = input("Enter the number of infants: ")

    location = sys.argv[1]
    # Checkin = sys.argv[2]
    # Checkout = sys.argv[3]
    adults = sys.argv[2]
    children = sys.argv[3]
    infants = sys.argv[4]

    # make checkin current month
    Checkin = dt.datetime.now().strftime("%B")
    # make checkout next month
    month_plus = dt.datetime.now() + dt.timedelta(days=30)
    Checkout = month_plus.strftime("%B")

    # print(f"Checkin: {Checkin} && Checkout: {Checkout}")

    url = construct_url(location, Checkin, Checkout, adults, children, infants)

    for i in range(15):
        offset = 20 * i
        url_offset = f"{url}&offset={offset}"

        full_rentals = scrape_page(url_offset)
        make_json(full_rentals, location)

    print("complete")


if __name__ == "__main__":
    main()
