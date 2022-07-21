def calc(list_numbers):
    i=0
    for number in list_numbers:
        i += int(number)
    return i


def main():
    numbers = input("enter the numbers via - ',': ")
    list_numbers = numbers.split(",")
    result = calc(list_numbers)
    print(result)



if __name__ == "__main__":
    main()