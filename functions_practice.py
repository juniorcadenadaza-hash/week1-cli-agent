def greet_user(name):
    print("Hello, " + name + "!")

def age_message(age):
    if age < 18:
        return "You're young! Great time to start learning!"
    elif age >= 18 and age <= 20:
        return "Perfect age for learning automation!"
    elif age > 20 and age <= 30:
        return "Awesome! You're at a great age to dive into automation!"
    else:
        return "Never too late to learn. Let's go!"


greet_user("Junior")
age_message(25)
