student_icards = {
    86122600026: {
        "college": "NMIMS Nsomasa",
        "firstname": "Dev",
        "lastname": "Kamdar",
        "course": "AMC",
        "contact": "+91 98203 10513",
        "DOB": "13/05/2007",
        "blood_group": "O-",
        "Year": "1st Year",
        "city": None,
        "state": None
    }
}

defaults = {
    "city": "Mumbai",
    "state": "Maharashtra"
}

for icard_number, details in student_icards.items():
    print(f"ICard Number: {icard_number}")
    for key, value in details.items():
        display_value = value if value is not None else defaults.get(key, "N/A")
        print(f"\t{key}: {display_value}")
    print()