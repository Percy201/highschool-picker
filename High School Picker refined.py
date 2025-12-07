print("Which city are you based at?")
area = input().strip().lower()

# dictionary of cities and their schools
schools_by_city = {
    "alberton": [
        "Alberton High",
        "Hoerskool Alberton",
        "Hoerskool Dinamika",
        "Parklands High",
        "Marais Viljoen"
    ],
    "germiston": [
        "Germiston High",
        "Dinwiddie High",
        "Vryburgher High",
        "Primrose High",
        "Bedfordview High"
    ],
    "pretoria": [
        "Hoerskool Waterkloof",
        "St. Albans College",
        "Pretoria High School for Girls",
        "Pretoria Boys High School",
        "Afrikaans Seuns Hoer",
        "Afrikaans Meisies Hoer"
    ],
}

from random import choice

if area in schools_by_city:
    print("Here’s a school you might know:")
    print(choice(schools_by_city[area]))
else:
    print("Sorry, no high schools found in that area.")
    print("Try one of these cities:", ", ".join(schools_by_city.keys()))
