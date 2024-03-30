#!/usr/bin/env python3
class WorkingCarException(Exception):
    typ : int
    def __init__(self,typ):
        self.typ =typ
    def eval(self) :
        if self.typ==1:
            return "Vin is not 4 digits"
        elif self.typ == 2:
            return "Brand must be Ford,Honda,Toyota,Chrysler or other"
        elif self.typ==3:
            return "The year must be between 1997 and 2007"
        elif self.typ == 4 :
            return "The mileage/price cannot be NEGATIVE"
        else:
            return "null"
    def __str__(self):
        return self.eval()
class workingcar:
    VIN : str
    brand : str
    year : int
    price : float
    mileage : float
    def __init__(self,VIN,brand,year,price,mileage):
        try:
            if len(VIN)!=4:
                raise WorkingCarException(1)
            else:
                self.VIN = VIN
        except WorkingCarException as we:
            print(we)
        try:
            if brand.casefold() not in ['Ford','Toyota','Chrysler','Other']:
                raise WorkingCarException(2)
            else:
                self.brand=brand
        except WorkingCarException as we:
            print(we)
        try:
            if year < 1997 or year > 2017 :
                raise WorkingCarException(3)
            else:
                self.year = year
        except WorkingCarException as we:
            print(we)
        try:
           if price < 0.0 or mileage <0.0 :
               raise WorkingCarException(4)
           else:
               self.price = price
               self.mileage = mileage
        except WorkingCarException as we:
            print(we)
class TestWorkingCarException:
    def main(self):
        vin = ""
        brand = ""
        year = 0
        price = 0.0
        mileage = 0.0
        wc = [None] * 7

        for i in range(7):
            vin = input("Enter the vin of the car: ")
            brand = input("Enter the brand of the car: ")
            year = int(input("Enter the year of the car: "))
            price = float(input("Enter the price of the car: "))
            mileage = float(input("Enter the mileage of the car: "))
            wc[i] = workingcar(vin, brand, year, price, mileage)
        print(wc)
if __name__ == "__main__":
    tester = TestWorkingCarException()
    tester.main()
