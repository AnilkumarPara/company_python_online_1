# find the biggest country among 4 countries based on the population
country_1 = int(input("Enter population of country_1"))
country_2 = int(input("Enter population of country_2"))
country_3 = int(input("Enter population of country_3"))
if country_1 > country_2 and country_1 > country_3:
    print("country_1 is greater")
elif country_2 > country_3:
    print("country_2 is greater")
else:
    print("country_3 is greater")
