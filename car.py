def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
class car(object):
    def __init__(self, name, color, company, fuel_type, spoiler, suspension_type):
        self.name = name
        self.color = color
        self.company = company
        self.fuel_type = fuel_type
        self.spoiler = spoiler
        self.suspension_type = suspension_type



    prCyan("\nThese are my favourite cars and their features:\n")
    def printValues(self):
        print(self.name,": \n")
        print(self.color)
        print(self.company)
        print(self.fuel_type)
        print(self.spoiler)
        print(self.suspension_type,"\n")



lamborghini_huracan = car("Lamborghini Huracan","Yellow","Lamborgini","Petrol","GT Spoiler","Competition Suspension")
ford_mustang = car("Ford Mustang","Torino Red","Ford","Petrol","Lip Spoiler","Competition Suspension")

lamborghini_huracan.printValues()
ford_mustang.printValues()