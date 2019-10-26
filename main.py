print("Hello. This program can help you convert a distance from kilometers into miles.")

while True:

    kilometers = float(input("Enter the number of kilometers: "))

    miles = float(kilometers * 0.6214)

    print(str(kilometers) + " kilometers is " + str(miles) + " miles")

    choice = input("Would you like to do another conversion? ")

    if choice == "no":
        print("Thank you for using this converter!")
        break
