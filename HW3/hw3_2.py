def user_data(name, last_name, birth_year, city, email, phone_num):
    return ' '.join([name, last_name, birth_year, city, email, phone_num])


print(user_data(name=(input("Please write your name: ")),
                last_name=(input("Please write your last name: ")),
                birth_year=input("Please write your birth year: "),
                city=input("Please write city where you live: "),
                email=input("Please write your email: "),
                phone_num=input("Please write your phone number: ")))
