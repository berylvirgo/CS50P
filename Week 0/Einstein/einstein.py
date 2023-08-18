def main():
    mass = int(input("m: "))

    speed_of_light = 300000000  # meters per second
    energy = mass * (speed_of_light ** 2)

    print(f"E: {energy}")


if __name__ == "__main__":
    main()