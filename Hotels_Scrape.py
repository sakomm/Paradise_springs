import bs4 
import requests 
import json
import datetime

params = {
    'location': "",
    'Check-in': "",
    'Check-out': "",
    'adults': "",
    'children': "",
    'infants': "",
}


def construct_location():
    #order is city, state, country
    input_city = input("Enter the city: ")
    input_state = input("Enter the state: ")
    input_country = input("Enter the country: ")

    location = f"{input_city.lower()}--{input_state.lower()}--{input_country.lower()}"

    return location


def user_input(location, Checkin, Checkout, adults, children, infants):
    params["location"] = location
    params["Check-in"] = Checkin
    params["Check-out"] = Checkout
    params["adults"] = adults
    params["children"] = children
    params["infants"] = infants



def construct_url():
    url = f"https://www.hotels.com/Hotel-Search?adults={params['adults']}&d1={params['Check-in']}&d2={params['Check-out']}&destination={params['location']}&endDate={params['Check-out']}"

    return url