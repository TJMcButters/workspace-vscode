import HideIt
import ShowIt


def main():
    choice = int(input("What would you like to do: \n\t1. Hide a file in an image \n\t2. Extract a file from an image"))
    if choice == 1:
        HideIt.main()
    elif choice == 2:
        ShowIt.main()


if __name__ == '__main__':
    main()
