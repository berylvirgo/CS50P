import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    if len(sys.argv) == 2:
        try:
            float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")

        try:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            response = response.json()
            amount = float(response["bpi"]["USD"]["rate_float"]) * float(sys.argv[1])
            print(f"${amount:,.4f}")    
        except requests.RequestException:
            pass


if __name__ == "__main__":
    main()