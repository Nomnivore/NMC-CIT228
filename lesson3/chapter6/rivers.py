rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "lena": "russia"
}

print("------------ Rivers & Countries ------------")
for river, country in rivers.items():
    print(f"The {river.capitalize()} river runs through {country.capitalize()}.")

print("------------------ Rivers ------------------")
for river in rivers.keys():
    print(f"The {river.capitalize()} river")

print("---------------- Countries -----------------")
for country in rivers.values():
    print(country.capitalize())
