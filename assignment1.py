class Car:
    def __init__(self, brand, model):

        self.brand = brand
        self.model = model

    def showme(self):
        print("Car brand is " + self.brand)
        print("Car model is " + self.model)

if __name__ == "__main__":
    civic = Car("Honda", "Civic")
    lambo = Car("Lamborghini", "Diablo")

    civic.showme()
    lambo.showme()
