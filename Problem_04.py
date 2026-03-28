def calculate_fine(days, rate):
    return days * rate


def main():
    book = input()
    days = int(input())
    rate = float(input())

    fine = calculate_fine(days, rate)

    print(f"Book: {book} Days overdue: {days} Fine: Rs. {float(fine)}")


if __name__ == "__main__":
    main()
    

