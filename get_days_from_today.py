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
    "2024-07-04",  # Future date (7 days from today)
    "2025-01-01",  # Far future date (more than a year from today)
    "2024-06-20",  # Past date (10 days before today)
    "2023-12-25",  # Distant past date (more than half a year ago)
    "2023-24-12",  # Invalid date format
]

for data in test_data:
    result = get_days_from_today(data)
    print(f"Days from today: {result}")
