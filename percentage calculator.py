try:
    s1 = float(input('Subject one: '))
    s2 = float(input('subject two: '))
    s3 = float(input('Subject three: '))
    s4 = float(input('Subject four: '))
    s5 = float(input('Subject five: '))
    if s1 <= 100 and s2 <= 100 and s3 <= 100 and s4 <= 100 and s5 <= 100:
        sum = s1+s2+s3+s4+s5
        percentage = sum/500*100
        print(percentage)
        if percentage > 75:
            print("distinction")
        elif 65 <= percentage <= 75:
            print("First class")
        elif 55 <= percentage < 65:
            print("Second class")
        elif 45 <= percentage < 55:
            print("Average")
        elif 40 <= percentage < 45:
            print("Pass")
        else:
            print("Fail")
    else:
        print("Marks should be between 0 to 100")
except ValueError:
    print("Please use digits only.")


