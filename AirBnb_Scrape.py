from pprint import pprint
import requests
import bs4
import json
import time
import datetime as dt

params = {
    'location': "",
    'Check-in': "",
    'Check-out': "",
    'adults': "",
    'children': "",
    'infants': "",
}

# params['location'] = "Charlottesville--Virginia--United States"
# params['Check-in'] = "april"
# params['Check-out'] = "march"
# params['adults'] = "1"
# params['children'] = "1"
# params['infants'] = "1"

# url = f"https://www.airbnb.com/s/{params['location']}/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D={params['Check-in']}&flexible_trip_dates%5B%5D={params['Check-out']}&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query={params['location']}&{params['adults']}&children={params['children']}&infants={params['infants']}"
# print(url)
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

def get_text(element):
    to_text = []
    for text in element:
        to_text.append(text.text)

    return to_text

"""
get price of the property parse string and get the price

given $122\xa0/ night$122 per night' is $122 per night
"""
def get_price(string):
    plist = []
    for prices in string:
        ppn = prices.split(" ")
        plist.append(f"{ppn[-3][5::]} {ppn[-2]} {ppn[-1]}")

    return plist

def scrape_page(url):
    # print(url)
    # print(params)

    # get all the names of the properties and store in json file
    print("Scraping page...")
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

    # exteracting data make graceful error handling later TODO
    
    #get the header of the property 
    headers = soup.find_all("div", class_="mj1p6c8 dir dir-ltr")
    #print only the text of the header of the property not the whole header
    headers = get_text(headers)
    # pprint(headers)

    names = soup.find_all("div", class_="c1bx80b8 dir dir-ltr")
    names = get_text(names)
    # pprint(names)
    
    # get the price of the property
    pp_night = soup.find_all("div", class_="p1qe1cgb dir dir-ltr")
    pp_night = get_price(get_text(pp_night))
    # pprint(pp_night)
   

    return headers, names, pp_night

def make_json(headers, names, pp_night):
    """
    make a json file of the scraped data
    """
    # make a json file of the scraped data each property should have its own section all index 0 are tougether
    with open("airbnb_scrape.json", "a") as f:

        # #make each property its own section grab the header and name of the property and the price of the property and write as one json object
        for i in range(20):
            # print(f"{headers[i]}, {names[i]}, {pp_night[i]}")
            if i != 19:
                json.dump({"header": headers[i], "name": names[i], "price": pp_night[i]}, f)
                f.write(",\n")
            else:
                json.dump({"header": headers[i], "name": names[i], "price": pp_night[i]}, f)
                f.write("\n")

    print("JSON file created")
    #close the file
    f.close()



def main():
    
    # location = construct_location()
    # Checkin = input("Enter the checkin date or press enter: ")
    # Checkout = input("Enter the checkout date or press enter: ")
    # adults = input("Enter the number of adults: ")
    # children = input("Enter the number of children: ")
    # infants = input("Enter the number of infants: ")

    location = "Charlottesville--Virginia--United States"
    Checkin = ""
    Checkout = ""
    adults = "1"
    children = "1"
    infants = "1"

    if (Checkin == "" or Checkout == ""):
        # make checkin current month
        Checkin = dt.datetime.now().strftime("%B")
        # make checkout next month
        month_plus = dt.datetime.now() + dt.timedelta(days=30)
        Checkout = month_plus.strftime("%B")

    print(f"Checkin: {Checkin} && Checkout: {Checkout}")

    url = construct_url(location, Checkin, Checkout, adults, children, infants)

    headers, names, pp_night = scrape_page(url)

    make_json(headers, names, pp_night)


if __name__ == "__main__":
    main()
