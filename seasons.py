from datetime import datetime
import re
import sys

class DOB:
    def __init__(self, year, month, day):
        self.dob = datetime(year, month, day)

    def calculate_age_in_minutes(self):
        now = datetime.now() 
        age = now - self.dob
        age_in_minutes = age.total_seconds() / 60
        return int(age_in_minutes)

def main():
    try:
        input_dob = input("DOB: ")
        if re.fullmatch("^[0-9]{4}-[0-1][0-9]-[0-3][0-9]$",input_dob):
            pass
        else:
            print("invalid Format")
        year, month, day = map(int, input_dob.split('-'))
        dob_object = DOB(year, month, day)
        age_in_minutes = dob_object.calculate_age_in_minutes()
        print(f"The age in minutes is: {age_in_minutes} minutes")
    except ValueError as e:
        print(f"Invalid Format")
        

if __name__ == "__main__":
    main()
