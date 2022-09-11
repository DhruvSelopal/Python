class Marks:
    def __int__(self,s1,s2,s3,s4,s5):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5

    def total(self):
        return s1 + s2 + s3 + s4 + s5

    def percentage(self):
        return (s1 + s2 + s3 + s4 + s5)/500*100

try:
    s1 = float(input("Marks of subject 1: "))
    s2 = float(input("Marks of subject 2: "))
    s3 = float(input("Marks of subject 3: "))
    s4 = float(input("Marks of subject 4: "))
    s5 = float(input("Marks of subject 5: "))
    if s1 <= 100 and s2 <= 100 and s3 <= 100 and s4 <= 100 and s5 <= 100:
        marks1 = Marks()
        total = marks1.total()
        percentage = marks1.percentage()
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
        print("Marks cannot be greater then 100")
except ValueError:
    print("Invalid value")
