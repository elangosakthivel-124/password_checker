from analyzer import password_strength


def main():
    password = input("Enter password: ")
    result = password_strength(password)

    print("\nPassword Strength Report")
    print("-" * 30)
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
