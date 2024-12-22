import os
import pyotp
import argparse
import robin_stocks.robinhood as r


def generate_token():
    totp = pyotp.TOTP("My2factorAppHere").now()
    print(f"TOTP: {totp}")

def login(mfa_code):
    username = os.getenv("RH_USERNAME")
    password = os.getenv("RH_PASSWORD")
    if not username or not password:
        print("Error: RH_USERNAME or RH_PASSWORD environment variables are not set.")
        exit(1)
    if mfa_code == "totp":
        mfa_code = pyotp.TOTP("My2factorAppHere").now()
        print(f"TOTP: {mfa_code}")
    else:
        # Add your login logic here
        print(f"User parameter: {mfa_code}")
        
    login = r.login(username, password, mfa_code=mfa_code)
    print(f"Login: {login}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process command line arguments.")
    parser.add_argument("action", choices=["token", "login"], help="Action to perform: 'token' or 'login'")
    parser.add_argument("mfa_code", nargs='?', help="User parameter for login action")
    args = parser.parse_args()

    if args.action == "token":
        generate_token()
    elif args.action == "login":
        if args.mfa_code:
            login(args.mfa_code)
        else:
            print("Error: user_param is required for login action.")
            exit(1)

# Note: after successful login, you can fin the pickle file in the current directory
# open ~/.tokens/robinhood.pickle to see the token
