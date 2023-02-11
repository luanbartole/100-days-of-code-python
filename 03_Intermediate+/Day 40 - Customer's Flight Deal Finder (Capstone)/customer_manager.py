from data_manager import DataManager
import os

SHEETY_BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN")
data_manager = DataManager(SHEETY_BEARER_TOKEN)


def sign_up():
    valid_info = False

    while not valid_info:
        print("Welcome to Luan's Flight Club! \nLet us find the best flight deals and email you!")

        user_info = {
            "user": {
                "firstName": input("First Name: ").capitalize(),
                "lastName": input("Last Name: ").capitalize(),
                "email": input("Email: ")
            }
        }
        validate_email = input("Email Confirmation: ")

        if validate_email == user_info["user"]["email"]:
            print("\n" + "=" * 40)
            print(f"Congratulations, {user_info['user']['firstName']}", f"\nYou are in the club!")
            print("=" * 40 + "\n")
            response_status_code = data_manager.add_new_user(user_info)
            print(response_status_code)
            valid_info = True
        else:
            print("\n" + "=" * 40)
            print("Email does not match in both inputs, \nplease try it again")
            print("=" * 40 + "\n")


sign_up()
