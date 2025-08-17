#  Contact Quick Lookup
names = ("ola", "wale", "ayo")

phone_no = (+2347012345678, +2349012345678, +2348012345678)

contact_dict = {name: phone for name, phone in zip(names, phone_no)}

lookup_name = input("Kindly enter the name you're looking for: ")

if lookup_name in names:
    print(f"The corresponding phone number for {lookup_name} is {contact_dict.get(lookup_name)}")
else:
    print("Contact not Found!")

# print(contact_dict)
