import requests
import bs4 
import json

params = {
    'location': "",
    'Check-in': "",
    'Check-out': "",
    'adults': "",
    'children': "",
    'infants': "",
}

"""
https://www.airbnb.com/s/Charlottesville--Virginia--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=march&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Charlottesville%2C%20Virginia%2C%20United%20States&place_id=ChIJj6RQ6i2Gs4kR_HSLw5bwhpA&adults=1&children=1&infants=1
"""

params['location'] = "Charlottesville--Virginia--United States"
params['Check-in'] = "april"
params['Check-out'] = "march"
params['adults'] = "1"
params['children'] = "1"
params['infants'] = "1"


"""
Consturct the URL to scrape from the parameters
should look like this:

https://www.airbnb.com/s/Charlottesville--Virginia--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=march&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Charlottesville%2C%20Virginia%2C%20United%20States&place_id=ChIJj6RQ6i2Gs4kR_HSLw5bwhpA&adults=1&children=1&infants=1
"""

url = f"https://www.airbnb.com/s/{params['location']}/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D={params['Check-in']}&flexible_trip_dates%5B%5D={params['Check-out']}&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query={params['location']}&place_id=ChIJj6RQ6i2Gs4kR_HSLw5bwhpA&adults={params['adults']}&children={params['children']}&infants={params['infants']}"
print(url)

