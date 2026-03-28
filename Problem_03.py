def calculate_fine(days):
    fine = days * 5
    if fine > 150:
        return 150, True
    return fine, False


def main():
    book = input()
    days = int(input())

    fine, is_max = calculate_fine(days)

    print(f"Book: {book} Days overdue: {days} Fine: Rs. {float(fine)}")

    if is_max:
        print(f"You have accumulated the maximum fine of INR: {float(fine)}")


if __name__ == "__main__":
    main()
    