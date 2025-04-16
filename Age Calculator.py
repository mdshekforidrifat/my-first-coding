from datetime import date

# User input
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

# Date objects
birth_date = date(birth_year, birth_month, birth_day)
current_date = date.today()

# Total days lived
age_days = (current_date - birth_date).days

# Convert days to years, months, days (approximate)
age_years = age_days // 365
age_months = (age_days % 365) // 30
age_remaining_days = (age_days % 365) % 30

# Output
print(f"Tomar boyosh: {age_years} bochhor, {age_months} mash, {age_remaining_days} din.")