from pprint import pprint
import bs4
import requests 
import json
import datetime
import timeit

start,end = 0,0

params = {
    'location': "",
    'Check-in': "",
    'Check-out': "",
    'adults': "",
    'children': "",
    'pets': "",
}

"""
Consturct the URL to scrape from the parameters

location
Check-in
Check-out
adults
children

if Check-in and Check-out are not provided dont include them in the URL

example:
https://www.vrbo.com/search/keywords:dallas-texas-united-states/minNightlyPrice/0?filterByTotalPrice=false&petIncluded=false&ssr=true&adultsCount=1&childrenCount=1
"""
def url_gen(location, check_in,check_out, adults, children, pets):
    if(check_in == "" and check_out == ""):
        url = f"https://www.vrbo.com/search/keywords:{location}/minNightlyPrice/0?filterByTotalPrice=false&petIncluded={pets}&ssr=true&adultsCount={adults}&childrenCount={children}"
    else:
        url = f"https://www.vrbo.com/search/keywords:{location}/minNightlyPrice/0?filterByTotalPrice=false&petIncluded={pets}&ssr=true&adultsCount={adults}&childrenCount={children}&checkInDate={check_in}&checkOutDate={check_out}"
    return url

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


def scrape_vrbo(url):
    start = timeit.default_timer()

    #get the html
    response = requests.get(url)

    #parse the html
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    #find the div with the data tag Waypoint form 1-10

    rentals = soup.find_all('div', class_="HitCollection")

    for i,x in enumerate(rentals):
        print(i)
        print(x)
        print("\n")


    #firnd the type of place and distance to location


    #find the price
    #find the rating
    #find the number of reviews
    #find the number of bedrooms
    #find the number of bathrooms


    end = timeit.default_timer()


def main():
    # prompt_user()
    # location = location_gen()
    location = "dallas-texas-united-states"
    params["Check-in"] = ""
    params["Check-out"] = ""
    params["adults"] = "1"
    params["children"] = "1"
    params["pets"] = "false"

    url = url_gen(location, params["Check-in"], params["Check-out"], params["adults"], params["children"], params["pets"])

    scrape_vrbo(url)

    print('Time: ', end - start)  
    print(url)

if __name__ == "__main__":
    main()
