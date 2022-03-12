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

def main():
    location = construct_location()
    Checkin = input("Enter the checkin date or press enter: ")
    Checkout = input("Enter the checkout date or press enter: ")
    adults = input("Enter the number of adults: ")
    children = input("Enter the number of children: ")
    infants = input("Enter the number of infants: ")

    if (Checkin == "" or Checkout == ""):
        # make checkin current month
        Checkin = dt.datetime.now().strftime("%B")
        # make checkout next month
        month_plus = dt.datetime.now() + dt.timedelta(days=30)
        Checkout = month_plus.strftime("%B")
    
    print(f"Checkin: {Checkin} && Checkout: {Checkout}")

    url = construct_url(location, Checkin, Checkout, adults, children, infants)

    print(url)
    


if __name__ == "__main__":
    main()