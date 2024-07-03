import json
import re

with open("default_countries_1.json", "r") as f:
    VALID_COUNTRY_CODES = json.load(f)


def normalize_phone(phone_number: str) -> str:
    normalized_number = re.sub(r"[^\d+]", "", phone_number)

    if normalized_number.startswith("+"):
        for _, country_code in VALID_COUNTRY_CODES.items():
            if normalized_number.startswith("+" + country_code):

                return normalized_number

    else:
        if not normalized_number.startswith("+38"):
            if normalized_number.startswith("380"):
                normalized_number = "+" + normalized_number
                return normalized_number
            else:
                normalized_number = "+38" + normalized_number
                return normalized_number
        else:
            normalized_number = "+38" + normalized_number
            return normalized_number

    return normalized_number


raw_numbers = [
    "+1 514-966-0249 ",
    "+263 09 235828",
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
