# Age checker with if/else statements
name = input("What is your name? ")
age = int(input("How old are you? "))
print("\nHello " + name + "!")
if age <= 18:
    print("You're young! Great time to start learning!")
elif age > 18 and age <= 20:
    print("Perfect age for learning automation!")
elif age > 20 and age <= 30:
    print("Awesome! You're at a great age to dive into automation!")
else:
    print("Never too late to learn. Let's go!")