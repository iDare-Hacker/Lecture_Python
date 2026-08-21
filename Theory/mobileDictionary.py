mobile = {
    "brand": "OnePlus",
    "os": "OxygenOS 16",
    "ram": "6 GB",
    "cpu": "2.4 GHz",
    "cost": [1234, 12345],
    "storage": ["128 GB", "256 GB"]
}

try:
    i = int(input("Which model (1/2): "))
except ValueError:
    i = 1

if i not in (1, 2):
    i = 1

print(f"brand: {mobile['brand']}")
print(f"os: {mobile['os']}")
print(f"ram: {mobile['ram']}")
print(f"cpu: {mobile['cpu']}")
print(f"cost: {mobile['cost'][i-1]}")
print(f"storage: {mobile['storage'][i-1]}")