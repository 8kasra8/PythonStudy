import sys
import datetime

inp_age = '10'

def fine_year_of_birth(aa = 0):
    thisyear = datetime.datetime.today()
    print("We are in year : " , thisyear.year)
    return int(thisyear.year) - int(aa)


def main():
    inp_age = input("What's your age: ")
    result = fine_year_of_birth(inp_age)
    print("You were born in year : ", result)


if __name__ == "__main__":
    main()
