from datetime import datetime


def get_days_from_today(date: str) -> int:
    date_today = datetime.today()
    try:
        date_input = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format")
        exit()
    return (date_today - date_input).days


test_data = [
    "2024-07-04",
    "2025-01-01",
    "2024-06-20",
    "2023-12-25",
    "2023-24-12",
]

for data in test_data:
    result = get_days_from_today(data)
    print(f"Days from today: {result}")
