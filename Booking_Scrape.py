import time
import selenium

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pymongo import MongoClient
import certifi

# page is fully loaded when url is entered
def gen_location(city, state, country):
    city = city.replace(" ", "+")
    country = country.replace(" ", "+")

    location = f"{city}%2C+{country}"

    return location


def generate_url(location, Check_in, Check_out, adults, children, rooms):
    "https://www.booking.com/ss=Las+Vegas%2C+United+States+of+America&is_ski_area=&checkin_year=2022&checkin_month=4&checkin_monthday=13&checkout_year=2022&checkout_month=4&checkout_monthday=15&group_adults=1&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&dest_type=city&search_selected=true"
    Check_in = Check_in.split("/")
    Check_out = Check_out.split("/")
    url = f"https://www.booking.com/ss={location}&is_ski_area=&checkin_year={Check_in[0]}&checkin_month={Check_in[1]}&checkin_monthday={Check_in[2]}&checkout_year={Check_out[0]}&checkout_month={Check_out[1]}&checkout_monthday={Check_out[2]}&group_adults={adults}&group_children={children}&no_rooms={rooms}&b_h4u_keep_filters=&from_sf=1&dest_type=city&search_selected=true"

    return url


def scrape_hotels(url):

    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')

    driver = webdriver.Chrome(options=options)
    driver.get(url)



    hotel_names = driver.execute_script(
        "return document.getElementsByClassName(\"fcab3ed991 a23c043802\")")
    
    hotel_rating = driver.execute_script("return document.getElementsByClassName(\"b5cd09854e d10a6220b4\")")

    hotel_price = driver.execute_script("return document.getElementsByClassName(\"fcab3ed991 bd73d13072\")")
    
    #will have to every other values
    hotel_distance = driver.execute_script("return document.getElementsByClassName(\"f4bd0794db b4273d69aa\")")
    
    hotel_location = driver.execute_script("return document.getElementsByClassName(\"fc63351294 a168c6f285 e0e11a8307 a25b1d9e47\")") 

    hotel_image = driver.execute_script("return document.getElementsByClassName(\"b8b0793b0e\")")

    hotel_distance_actual = []
    
    for i in range(0,len(hotel_distance),2):
        # print(i)
        hotel_distance_actual.append(hotel_distance[i].text) 

    rental_actual = []
    for name, rating, price, dist, location, img  in zip(hotel_names, hotel_rating, hotel_price, hotel_distance_actual, hotel_location, hotel_image):
        tmp = []
        # rental_actual.append(name.text, rating.text, price.text, dist, location.get_attribute("href"))
        tmp.append(name.text)
        tmp.append(rating.text)
        tmp.append(price.text)
        tmp.append(dist)
        tmp.append(location.get_attribute("href"))
        tmp.append(img.get_attribute("src"))

        rental_actual.append(tmp)
    
    return rental_actual

def database_insert(rental_actual):
    #https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb
    client = MongoClient("mongodb+srv://skom:access123@cluster0.5vezi.mongodb.net/test", tlsCAFile=certifi.where())
    #make a database of rentals 
    db = client.rentals
    


    #hotel_names, hotel_rating, hotel_price, hotel_distance_actual, hotel_location, hotel_image
    city_state = [
    'New York, New York', 'Honolulu, Hawaii', 'Miami, Florida', 'Hialeah, Florida', 'Miami Gardens, Florida', 'Miramar, Florida', 'Brownsville, Texas', 'Pembroke Pines, Florida', 'Hollywood, Florida', 'Davie, Florida', 'Fort Lauderdale, Florida', 'Pompano Beach, Florida', 'McAllen, Texas', 'Coral Springs, Florida', 'Edinburg, Texas', 'Cape Coral, Florida', 'West Palm Beach, Florida', 'Port St. Lucie, Florida', 'Laredo, Texas', 'Corpus Christi, Texas', 'St. Petersburg, Florida', 'Tampa, Florida', 'Clearwater, Florida', 'Palm Bay, Florida', 'Lakeland, Florida', 'Orlando, Florida', 'San Antonio, Texas', 'League City, Texas', 'Pearland, Texas', 'Sugar Land, Texas', 'Pasadena, Texas', 'Gainesville, Florida', 'Houston, Texas', 'New Orleans, Louisiana', 'Beaumont, Texas', 'Lafayette, Louisiana', 'Austin, Texas', 'Jacksonville, Florida', 'Baton Rouge, Louisiana', 'Tallahassee, Florida', 'Round Rock, Texas', 'College Station, Texas', 'Mobile, Alabama', 'Killeen, Texas', 'Waco, Texas', 'El Paso, Texas', 'Odessa, Texas', 'Savannah, Georgia', 'Midland, Texas', 'Tucson, Arizona', 'Las Cruces, New Mexico', 'Jackson, Mississippi', 'Tyler, Texas', 'Montgomery, Alabama', 'Abilene, Texas', 'Shreveport, Louisiana', 'Columbus, Georgia', 'Chula Vista, California', 'Grand Prairie, Texas', 'Arlington, Texas', 'Mesquite, Texas', 'Dallas, Texas', 'Fort Worth, Texas', 'El Cajon, California', 'Macon, Georgia', 'San Diego, California', 'Charleston, South Carolina', 'Irving, Texas', 'Garland, Texas', 'North Charleston, South Carolina', 'Richardson, Texas', 'Carrollton, Texas', 'Lewisville, Texas', 'Plano, Texas', 'Allen, Texas', 'Carlsbad, California', 'Escondido, California', 'Frisco, Texas', 'McKinney, Texas', 'Oceanside, California', 'Denton, Texas', 'Chandler, Arizona', 'Gilbert, Arizona', 'Augusta, Georgia', 'Tempe, Arizona', 'Mesa, Arizona', 'Temecula, California', 'Birmingham, Alabama', 'Glendale, Arizona', 'Lubbock, Texas', 'Phoenix, Arizona', 'Murrieta, California', 'South Fulton, Georgia', 'Surprise, Arizona', 'Irvine, California', 'Costa Mesa, California', 'Scottsdale, Arizona', 'Menifee, California', 'Huntington Beach, California', 'Santa Ana, California', 'Garden Grove, California', 'Atlanta, Georgia', 'Peoria, Arizona', 'Orange, California', 'Long Beach, California', 'Torrance, California', 'Anaheim, California', 'Corona, California', 'Fullerton, California', 'Norwalk, California', 'Wichita Falls, Texas', 'Moreno Valley, California', 'Riverside, California', 'Downey, California', 'Athens, Georgia', 'Sandy Springs, Georgia', 'Inglewood, California', 'Jurupa Valley, California', 'Los Angeles, California', 'Columbia, South Carolina', 'Ontario, California', 'Pomona, California', 'West Covina, California', 'El Monte, California', 'Fontana, California', 'Rialto, California', 'Rancho Cucamonga, California', 'San Bernardino, California', 'Pasadena, California', 'Glendale, California', 'Burbank, California', 'Thousand Oaks, California', 'Oxnard, California', 'Wilmington, North Carolina', 'Simi Valley, California', 'Ventura, California', 'Santa Clarita, California', 'Victorville, California', 'Palmdale, California', 'Lancaster, California', 'Huntsville, Alabama', 'Little Rock, Arkansas', 'Santa Maria, California', 'Chattanooga, Tennessee', 'Fayetteville, North Carolina', 'Albuquerque, New Mexico', 'Memphis, Tennessee', 'Amarillo, Texas', 'Charlotte, North Carolina', 'Norman, Oklahoma', 'Rio Rancho, New Mexico', 'Bakersfield, California', 'Concord, North Carolina', 'Oklahoma City, Oklahoma', 'Cary, North Carolina', 'Raleigh, North Carolina', 'Murfreesboro, Tennessee', 'Knoxville, Tennessee', 'Durham, North Carolina', 'High Point, North Carolina', 'Henderson, Nevada', 'Broken Arrow, Oklahoma', 'Greensboro, North Carolina', 'Winston�Salem, North Carolina', 'Tulsa, Oklahoma', 'Nashville, Tennessee', 'Las Vegas, Nevada', 'North Las Vegas, Nevada', 'Visalia, California', 'Clarksville, Tennessee', 'Chesapeake, Virginia', 'Salinas, California', 'Fresno, California', 'Virginia Beach, Virginia', 'Clovis, California', 'Norfolk, Virginia', 'Hampton, Virginia', 'Newport News, Virginia', 'Springfield, Missouri', 'Roanoke, Virginia', 'San Jose, California', 'Santa Clara, California', 'Sunnyvale, California', 'Fremont, California', 'Richmond, Virginia', 'San Mateo, California', 'Hayward, California', 'Modesto, California', 'Wichita, Kansas', 'Daly City, California', 'San Francisco, California', 'Oakland, California', 'Berkeley, California', 'Richmond, California', 'Stockton, California', 'Antioch, California', 'Concord, California', 'Evansville, Indiana', 'Lexington, Kentucky', 'Vallejo, California', 'Louisville, Kentucky', 'Fairfield, California', 'Pueblo, Colorado', 'Vacaville, California', 'Elk Grove, California', 'Santa Rosa, California', 'Sacramento, California', 'St. Louis, Missouri', 'Roseville, California', 'Alexandria, Virginia', 'Colorado Springs, Colorado', 'Overland Park, Kansas', 'Olathe, Kansas', 'Washington, District of Columbia', "Lee's Summit, Missouri", 'Columbia, Missouri', 'Topeka, Kansas', 'Independence, Missouri', 'Kansas City, Missouri', 'Kansas City, Kansas', 'Cincinnati, Ohio', 'Baltimore, Maryland', 'Reno, Nevada', 'Sparks, Nevada', 'Centennial, Colorado', 'Aurora, Colorado', 'Lakewood, Colorado', 'Chico, California', 'Denver, Colorado', 'Dayton, Ohio', 'Indianapolis, Indiana', 'Springfield, Illinois', 'Arvada, Colorado', 'Westminster, Colorado', 'Thornton, Colorado', 'Columbus, Ohio', 'Philadelphia, Pennsylvania', 'Boulder, Colorado', 'Lakewood, New Jersey', 'Provo, Utah', 'Greeley, Colorado', 'Pittsburgh, Pennsylvania', 'Edison, New Jersey', 'Fort Collins, Colorado', 'Woodbridge, New Jersey', 'Allentown, Pennsylvania', 'West Jordan, Utah', 'Elizabeth, New Jersey', 'West Valley City, Utah', 'Jersey City, New Jersey', 'Newark, New Jersey', 'Peoria, Illinois', 'Salt Lake City, Utah', 'Lincoln, Nebraska', 'Paterson, New Jersey', 'Yonkers, New York', 'Stamford, Connecticut', 'Akron, Ohio', 'Fort Wayne, Indiana', 'Bridgeport, Connecticut', 'Omaha, Nebraska', 'New Haven, Connecticut', 'Cleveland, Ohio', 'Joliet, Illinois', 'Waterbury, Connecticut', 'Davenport, Iowa', 'Des Moines, Iowa', 'New Bedford, Massachusetts', 'Toledo, Ohio', 'South Bend, Indiana', 'Naperville, Illinois', 'Hartford, Connecticut', 'Aurora, Illinois', 'Providence, Rhode Island', 'Chicago, Illinois', 'Cedar Rapids, Iowa', 'Elgin, Illinois', 'Brockton, Massachusetts', 'Springfield, Massachusetts', 'Quincy, Massachusetts', 'Rockford, Illinois', 'Worcester, Massachusetts', 'Ann Arbor, Michigan', 'Dearborn, Michigan', 'Boston, Massachusetts', 'Cambridge, Massachusetts', 'Detroit, Michigan', 'Lynn, Massachusetts', 'Warren, Michigan', 'Clinton, Michigan', 'Sterling Heights, Michigan', 'Lowell, Massachusetts', 'Lansing, Michigan', 'Buffalo, New York', 'Grand Rapids, Michigan', 'Manchester, New Hampshire', 'Syracuse, New York', 'Milwaukee, Wisconsin', 'Madison, Wisconsin', 'Rochester, New York', 'Sioux Falls, South Dakota', 'Nampa, Idaho', 'Boise, Idaho', 'Meridian, Idaho', 'Rochester, Minnesota', 'Eugene, Oregon', 'Green Bay, Wisconsin', 'Salem, Oregon', 'Saint Paul, Minnesota', 'Minneapolis, Minnesota', 'Gresham, Oregon', 'Hillsboro, Oregon', 'Portland, Oregon', 'Vancouver, Washington', 'Billings, Montana', 'Fargo, North Dakota', 'Tacoma, Washington', 'Federal Way, Washington', 'Kent, Washington', 'Renton, Washington', 'Bellevue, Washington', 'Seattle, Washington', 'Spokane Valley, Washington', 'Spokane, Washington', 'Everett, Washington', 'Anchorage, Alaska']
    
    for key, data in zip(city_state, rental_actual):
        rental_info = {"key":"","hotel_name":"", "hotel_rating":"", "hotel_price":"", "hotel_distance_actual":"", "hotel_location":"", "hotel_image":""}
        rental_info["key"] = "Las Vegas, Nevada"

        rental_info["hotel_name"] = data[0]
        rental_info["hotel_rating"] = data[1]
        rental_info["hotel_price"] = data[2]
        rental_info["hotel_distance_actual"] = data[3]
        rental_info["hotel_location"] = data[4]
        rental_info["hotel_image"] = data[5]

        db.rentals.insert_one(rental_info)    

def main():
    location = gen_location("Las Vegas", "Nevada", "United States of America")
    check_in = "2022/4/13"
    check_out = "2022/4/15"
    adults = 1
    children = 0
    rooms = 1

    url = generate_url(location, check_in, check_out, adults, children, rooms)
    print(url)
    dump = scrape_hotels(url)
    database_insert(dump)



if __name__ == "__main__":
    main()
