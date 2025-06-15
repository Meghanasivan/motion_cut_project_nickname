import random

def generate_nicknames(first, last):
    nicknames = []

    # Basic combinations
    nicknames.append(first[:3] + last[-3:])
    nicknames.append(first + "_" + last)
    nicknames.append(last + first)

    # Creative mix
    symbols = ["_", ".", "!", "99", "007"]
    nicknames.append(first.capitalize() + last.lower() + random.choice(symbols))
    nicknames.append(first[0] + last)
    nicknames.append(random.choice(first) + random.choice(last) + str(random.randint(1, 99)))

    return nicknames

# Input from user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

nicknames = generate_nicknames(first_name, last_name)

print("\nGenerated Nicknames:")
for name in nicknames:
    print("➤", name)

# Optional: Save to file
save = input("\nDo you want to save these nicknames? (yes/no): ").lower()
if save == 'yes':
    with open("nicknames.txt", "w") as file:
        for name in nicknames:
            file.write(name + "\n")
    print("Nicknames saved to nicknames.txt")
