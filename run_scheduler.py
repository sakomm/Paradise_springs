import csv
from struct import calcsize
import timeit
import multiprocessing as mp
import time
import os


#look at the cities_us_all csv file the first two from the csv
def read_csv():
    with open("/home/saikommuri/Documents/CoDiNG_GeNiuS/Paradise_springs/JSON_Outputs/cities_us_all.csv", "r") as f:
        contet = csv.reader(f, delimiter=",")
        for row in contet:
            print(f"{row[0]} {row[1]}")
            call_code(row[0],row[1])
            time.sleep(7)

def call_code(city,state):                   

    #run Vrbo_scrape.py with the city and state as location argument, 2 adults, 1 child, and 0 infants
    os.system(f"python3 /home/saikommuri/Documents/CoDiNG_GeNiuS/Paradise_springs/AirBnb_Scrape.py {city}--{state}--united-states 2 1 0")
    # print("test")
def main():
    read_csv() 

if __name__ == "__main__":
    main()