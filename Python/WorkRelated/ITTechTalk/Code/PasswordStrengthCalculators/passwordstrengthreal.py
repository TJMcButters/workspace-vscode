from . import 
import re


def num_format(num):
    return f"{num:,d}"


def check_for_words(pw):
    list_of_words = 
    for word in list_of_words:
        if word in pw:
            print("{}: True".format(word))
        else:
            print("All clear")


def uPass():
    pw = input("\nEnter a FAKE password: ")
    l = len(pw)
    e = 0
    nones = [
        (re.search(r"[a-z]", pw), 26),
        (re.search(r"[A-Z]", pw), 26),
        (re.search(r"[0-9]", pw), 10),
        (re.search(r"[\"\'~!@#$%^&\\*\(\)_=\+\|,./\?:;\[\]\{\}<>] ", pw), 33),
    ]
    for i, k in nones:
        if i != None:
            e += k
    check_for_words(pw)
    """    
    print("\nThe length of the password is {}, and the number of available characters is {}".format(l, e))
    print("To calculate entropy, we take the length of the password and take it to the power of how many available characters exist:")
    print("So, we would take {} to the power of {} to get {}".format(l, e, num_format(pow(l, e))))
    """


def listPass():
    pass


def main():
    for y in range(50):
        print("\n")
    uin = input(
        "Would you like to: \n\t1. Provide a password\n\t2. Test against a list\n"
    )
    if uin == "1":
        uPass()
    elif uin == "2":
        listPass()


if __name__ == "__main__":
    main()
