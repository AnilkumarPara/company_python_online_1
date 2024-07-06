# find the biggest country among 3 countries based on the population
country_1 = int(input("Enter population of country_1 "))
country_2 = int(input("Enter population of country_2 "))
country_3 = int(input("Enter population of country_3 "))
if country_1 > country_2:
    if country_1 > country_3:
        print("Country-1 is the biggest country")
    else:
        print("Country-3 is the biggest country")

else:
    if country_2 > country_3:
        print("Country-2 is the biggest country")
    else:
        print("Country-3 is the biggest country")

print("end program")


print("-----------------------------------------------------------")

if country_1 > country_2 and country_1 > country_3:
    print("Country-1 is the biggest country")

else:
    if country_2 > country_3:
        print("Country-2 is the biggest country")
    else:
        print("Country-3 is the biggest country")

print("end program")
