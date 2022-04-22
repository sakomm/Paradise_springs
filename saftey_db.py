from pymongo import MongoClient 
import certifi

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

def read_csv():
    client = MongoClient(
        "mongodb+srv://skom:access123@cluster0.5vezi.mongodb.net/test", tlsCAFile=certifi.where())
    # make a database of rentals
    db = client.rentals_test_drop
    
    with open("JSON_Outputs//cities_us_all.csv", "r") as f:
        i = 1
        for line in f:
            data = line.split(",")
            city = data[0]
            state = data[1]
            #cast saftey to int
            saftey = int(data[2])

            print(f"{i} : {city}, {state} ==> {saftey}")
            i += 1

            saftey_rating = {}
            saftey_rating["key"] = f"{city}, {state}"
            saftey_rating["city"] = city
            saftey_rating["state"] = state
            saftey_rating["safety_rating"] = saftey

            #safety

            db.safety_stat.insert_one(saftey_rating)


            
if __name__ == "__main__":
    read_csv()
