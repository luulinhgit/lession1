import string
import random
Letters=string.ascii_letters
Numbers=string.digits
Punctuation=string.punctuation
print(Punctuation)
print(Numbers)
print(Letters)
print("Toeic990")
def password_generator(length):
    printable=f'{Letters}{Numbers}{Punctuation}'
    printable=list(printable)
    random.shuffle(printable)
    random_password=random.choices(printable,k=length)
    random_password=''.join(random_password)
    return  random_password
def   get_password_length():
    password_length=input("How long do you want your password:")
    return int(password_length)
def main():
    password_length = get_password_length()
    password=password_generator(password_length)
    print(password)
if __name__ == '__main__':
    main()