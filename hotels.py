from distutils.command import check
from urllib import response
import requests
import bs4
import json
import time

params = {
    "Check-in": "",
    "Check-out": "",
    "adults": "",
    "children": "",
    "pets": ""
}

def gen_url(location,Check_in,Check_out,adults,rooms):
    """
    generate the url for the location
    
    https://www.hotels.com/Hotel-Search?adults=2&d1=2022-04-20&d2=2022-04-21&destination=Ocean%20City%2C%20Maryland%2C%20United%20States%20of%20America&endDate=2022-04-21&latLong=38.378116%2C-75.087754&regionId=9151&rooms=1&semdtl=&sort=RECOMMENDED&startDate=2022-04-20&theme=&useRewards=false&userIntent=
    """
    url  = f"https://www.hotels.com/Hotel-Search?adults={adults}&d1={Check_in}&d2={Check_out}&destination={location}&endDate={Check_out}&rooms={rooms}&semdtl=&sort=RECOMMENDED&startDate={Check_in}&theme=&useRewards=false&userIntent="

    return url
    
def gen_location():
    """
    generate the location

    Ocean%20City%2C%20Maryland%2C%20United%20States%20of%20America
    """
    input_city = input("Enter the city: ")
    input_state = input("Enter the state: ")
    input_country = "United%20States%20of%20America"

    input_city = input_city.replace(" ", "%20")
    input_state = input_state.replace(" ", "%20")
    input_country = input_country.replace(" ", "%20")

    location = f"{input_city}%2C%20{input_state}%2C%20{input_country}"

    return location

def scrape_hotels(url):
    response = requests.get(url) 
    content = response.content
    soup = bs4.BeautifulSoup(content, "html.parser")

    hotel_name = soup.get_text()


    print(hotel_name)

    return 0

def main():

    #def gen_url(location,Check_in,Check_out,adults,rooms):
    location = gen_location()
    url = gen_url(location,"2022-04-20","2022-04-21","2","1")

    scrape_hotels(url)


if __name__ == "__main__":
    main()
