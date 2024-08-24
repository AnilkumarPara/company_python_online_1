# Searching for an Element in a List

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = 0
search_element = int(input("Enter a element to search from a list "))
for number in numbers:
    if number == search_element:
        c = c + 1
        break
if c == 1:
    print(f"{search_element}  Element is found")
else:
    print(f"{search_element}  Element is not found")

print("End of the Program")
