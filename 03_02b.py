from collections import namedtuple
from csv import reader

def main():
    #add code here
    #read data/Customer.csv
    with open("data/Customer.csv", "r") as open_csv:
        read = reader(open_csv)
        Person = namedtuple("Person", next(read))
        for line in read:
            person = Person(*line)
            print(person)
    #Create workable objects with each line
    return

if __name__ == "__main__":
    main()