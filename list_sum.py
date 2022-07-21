def calc(list_numbers):
    i = 0
    step = 0
    try:
        for number in list_numbers:
            i += int(number)
            step += 1
    except ValueError:
        return f" {step} index in the array is not correct"


    return f"Sum of numbers {i}"


def main():
    numbers = input("enter the numbers via - ',': ")
    list_numbers = numbers.split(",")
    result = calc(list_numbers)
    print(result)


if __name__ == "__main__":
    main()
