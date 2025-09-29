# TASK SEVEN: List Manipulation
cities = ["Abuja", "Lagos", "Ibadan", "Kano", "Jos"]
user_city = input("Enter any city different from (Abuja, Lagos, Ibadan, Kano, Jos): ")
cities[2] = user_city
cities.pop()
cities.insert(0, "Akure")
print(cities)