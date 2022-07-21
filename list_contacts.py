def main():
    contacts = [{"Alex": 80291111111}, {"Eugen": 80297777777}, {"Maks": 80332222222}]

    while True:
        command = input("1-Create\n2-Delete\n3-viewing\nEnter number: ")
        if command == '1':
            name = input("Enter name: ")
            phone_number = int(input("Enter phone number: "))
            contacts.append({name: phone_number})
        elif command == '2':
            id = int(input("Enter id number: "))
            contacts.pop(id)
            print(contacts)
        elif command == '3':
            for id, people in enumerate(contacts):
                for name, number_phone in people.items():
                    print(f"| {id}  |   {name}    | {number_phone} |")
        elif command.lower() == 'exit':
            break


if __name__ == "__main__":
    main()
