from pydantic import BaseSettings

class Settings(BaseSettings):
    ALLOWED_HOSTS: list = ["*"]
    DEBUG: bool = False

non_discrete = ["ALLOWED_HOSTS", "DEBUG"]

def check_settings():
    checks_result = 0
    for setting in Settings():
        value_string = "" if not setting[0] in non_discrete else f" = {setting[1]}"
        print(f"INFO:     Running basic checks for {setting[0]}{value_string}")
        if setting[1] in ["", None, " "]:
            print(
                f"ERROR:    Setting '{setting[0]}' has a value of '{setting[1]}'")
            checks_result = 1
    return checks_result
