age = 15

if age < 10 or age > 65:
    print("Free")
elif 10 <= age <= 20:
    print(f"Price is {age * 0.1:.2f} Euro")
else:  # covers 21 to 65 inclusive
    print("Price is 2 Euros")
