class Car:
    def __init__(self, brand, model):

        self.brand = brand
        self.model = model

    def showme(self):
        print("Car brand is " + self.brand)
        print(f"Car model is {self.model}")


def main():
    civic = Car("Honda", "Civic")
    lambo = Car("Lamborghini", "Diablo")

    civic.showme()
    print("--------------")
    lambo.showme()


if __name__ == "__main__":
    main()
