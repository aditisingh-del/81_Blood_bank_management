import os

DONORS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "donors.txt")
VALID_GROUPS = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]


def initial_stock():
    
    stock = {group: 0 for group in VALID_GROUPS}
    stock.update({"A+": 10, "B+": 5, "O+": 8, "AB+": 2})
    return stock


def load_donors(path=DONORS_FILE):
    
    donors = []
    if not os.path.exists(path):
        return donors
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = [p.strip() for p in line.split(",")]
            if len(parts) != 3 or not parts[2].isdigit():
                continue  # skip badly formatted lines
            donors.append(
                {"name": parts[0], "group": parts[1].upper(), "units": int(parts[2])}
            )
    return donors


def save_donors(donors, path=DONORS_FILE):
    
    with open(path, "w", encoding="utf-8") as f:
        for d in donors:
            f.write(f"{d['name']}, {d['group']}, {d['units']}\n")


def check_group(text):
    
    group = text.strip().upper()
    if group not in VALID_GROUPS:
        print(f"Invalid blood group. Valid groups: {', '.join(VALID_GROUPS)}.")
        return None
    return group


def check_units(text):
    text = text.strip()
    if not text.isdigit() or int(text) <= 0:
        print("Invalid units. Please enter a positive whole number.")
        return None
    return int(text)


def add_donor(stock, donors):
    name = input("Name: ").strip()
    group_text = input("Blood group: ")
    units_text = input("Units: ")

    if not name:
        print("Name cannot be empty.")
        return
    group = check_group(group_text)
    if group is None:
        return
    units = check_units(units_text)
    if units is None:
        return

    donors.append({"name": name, "group": group, "units": units})
    stock[group] += units
    save_donors(donors)
    print(f"Donor saved to donors.txt. Stock of {group} is now {stock[group]} units.")


def issue_blood(stock):
    group_text = input("Blood group: ")
    units_text = input("Units: ")

    group = check_group(group_text)
    if group is None:
        return
    units = check_units(units_text)
    if units is None:
        return

    if stock[group] < units:
        print(f"Insufficient stock: only {stock[group]} unit(s) of {group} available.")
        return

    stock[group] -= units
    print(f"{units} unit(s) of {group} issued. Stock of {group} is now {stock[group]} units.")


def view_stock(stock):
    print("\nCurrent Blood Stock:")
    for group in VALID_GROUPS:
        print(f"  {group}: {stock[group]} unit(s)")


def search_donors(donors):
    group = check_group(input("Blood group: "))
    if group is None:
        return
    found = [d for d in donors if d["group"] == group]
    print(f"Donors with blood group {group}:")
    for i, d in enumerate(found, start=1):
        print(f"{i}. {d['name']} - {d['units']} unit(s)")
    print(f"Total donors found: {len(found)}")


def main():
    stock = initial_stock()
    donors = load_donors()

    while True:
        print("\n===== Blood Bank Management System =====")
        print("1. Add donor")
        print("2. Issue blood")
        print("3. View stock")
        print("4. Search donors")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_donor(stock, donors)
        elif choice == "2":
            issue_blood(stock)
        elif choice == "3":
            view_stock(stock)
        elif choice == "4":
            search_donors(donors)
        elif choice == "5":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Please enter 1 to 5.")


if __name__ == "__main__":
    main()