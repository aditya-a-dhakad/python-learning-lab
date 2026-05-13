import datetime

name = input("enter your name").strip()
age = (input("enter your age")).strip()
city = input("Which city do you live in? ").strip()
profession = input("What is your profession? ").strip()
hobby = input("WHat is your favourite hobby? ").strip()
num_age = int(age)
current_year = datetime.date.today().year
DOB = current_year - num_age
message = (f" Hello everyone my name is {name}"
        f"i am {age} year old (born arround {DOB}) and live in {city}. "
        f"I work as a {profession} and I absolutely enjoy {hobby} in my free time. "
        f"Nice to meet you!\n")

current_date = datetime.date.today().isoformat()

message += f"\n Logged On :{current_date}"

border = "*" * 80
final_output = f"{border}\n{message}\n{border}"

print("\n" + final_output)