
if __name__ == "__main__":
    try:
        i = input("Enter one number: ")
        if i >= 1:
            print(i)
            print("The number is valid")
    except Exception as e:
        print("Error: {}! Please enter a valid number which is <= 1".format(e))
    finally:
        x = int(input("Enter 1st number"))
        y = int(input("Enter 2nd number"))
        z = x + y
        print("The result is {}. ".format(z))

