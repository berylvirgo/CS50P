def main():
    amount = 50
    while True:
        print(f"Amount Due: {amount}")
        coin = int(input("Insert Coin: "))
        if coin not in [5, 10, 25]:
            continue
        else:
            amount -= coin
            if amount <= 0:
                if amount == 0:
                    print(f"Change Owed: {amount}")
                    break
                else:
                    amount = amount * -1
                    print(f"Change Owed: {amount}")
                    break


if __name__ == "__main__":
    main()