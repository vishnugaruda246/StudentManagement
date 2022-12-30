num = input(int("Enter a number"))
rev = 0

while num != 0:
    digit=num % 10
    rev= rev * 10 + digit
    num //=0
print("Reverse of the given number: "rev)