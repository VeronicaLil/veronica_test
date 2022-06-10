import sys
from datetime import datetime


if __name__ == "__main__":
    day = int(sys.argv[1])
    month = int(sys.argv[2])
    year = int(sys.argv[3])
    birthday = datetime(year, month, day)
    now = datetime.now() 
    difference = now - birthday     
    days = str(difference).split(" ")[0]
    years = round(int(days) / 365)

    #if years >= 18:
    #    print("Maggiorenne")
    #else:
    #    print("Minorenne")

    future_years = years + 20
    print(f"You will have {future_years}")
