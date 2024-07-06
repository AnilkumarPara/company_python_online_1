# nested if
"""
WAP to get the Karachi biscuits, when your friend goes to Hyderabad, Ameerpet,
Karachi biscuits shop
"""
city = input("Enter city name: ")
if city == 'Hyderabad':
    area = input("Enter area name: ")
    if area == 'Ameerpet':
        shop = input("Enter shop name: ")
        if shop == 'Karachi biscuits shop':
            print("Buy the Karachi biscuits")
print("End of the program")

