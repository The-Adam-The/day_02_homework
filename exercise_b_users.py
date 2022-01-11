users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
twitter_handle = users["Jonathan"]["twitter"]
print(f"Jonathan's Twitter Handle: {twitter_handle}")

# 2. Get Erik's hometown
hometown = users["Erik"]["home_town"]
print(f"Erik's hometown: {hometown}")

# 3. Get the list of Erik's lottery numbers
lottery_n = users["Erik"]["lottery_numbers"]
print(f"Erik's lottery numbers: {lottery_n}")

# 4. Get the species of Avril's pet Monty
pet_species = users["Avril"]["pets"][0]["species"]
print(f"Avril has a pet {pet_species}.")

# 5. Get the smallest of Erik's lottery numbers
lowest_lottery_n = min(lottery_n)
print(f"Erik's lowest lottery number: {lowest_lottery_n}")


# 6. Return an list of Avril's lottery numbers that are even
avril_lottery_n = users["Avril"]["lottery_numbers"]

avril_even_lottery_numbers = []

for n in avril_lottery_n:
  if n % 2 == 0:
    avril_even_lottery_numbers.append(n)
print(f"Avril's even lottery numbers: {avril_even_lottery_numbers}")


# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users["Erik"]["lottery_numbers"].append(7)
erik_appended_lotter_numbers = users["Erik"]["lottery_numbers"]
print(f"Erik's appended lottery numbers: {erik_appended_lotter_numbers}")

# 8. Change Erik's hometown to Edinburgh
users["Erik"]["hometown"] = "Edinburgh"

erik_hometown = users["Erik"]["hometown"]

print(f"Erik's updated hometown: {erik_hometown}")

# 9. Add a pet dog to Erik called "fluffy"
users["Erik"]["pets"] = [
  {"name": "fluffy",
   "species": "dog"
   }
]

erik_pet = users["Erik"]["pets"]

print(f"Erik's pet: {erik_pet}")

# 10. Add another person to the users dictionary

users["Simon"] = {
    "twitter": "simon_says",
    "hometown": "Huddersfield",
    "lottery_numbers": [4, 8, 29, 30, 21, 35],
    "pets": [
      
      {
        "name": "Spike",
        "species": "unicorn"
      },
      {
        "name": "Fido",
        "species": "cat"
      }
    ]
}

simon_element = users["Simon"]
print(f"Simon's dictionary element: {simon_element}")


