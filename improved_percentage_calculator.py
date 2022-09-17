name = input("Enter name: ").lower()
previous_year_percentage = {
    'rahul': 56,
    'john':65,
    'singh': 34,
    'ransom':90,
    'gupta':95
    }
if name not in previous_year_percentage:
    print("Name not registered")
else:
    try:
        s1 = float(input("Marks of subject 1: "))
        s2 = float(input("Marks of subject 2: "))
        s3 = float(input("Marks of subject 3: "))
        s4 = float(input("Marks of subject 4: "))
        s5 = float(input("Marks of subject 5: "))
        if s1 <= 100 and s2 <= 100 and s3 <= 100 and s4 <= 100 and s5 <= 100:
            total = s1 + s2 + s3 + s4 + s5
            percentage = total / 500 * 100
        else:
            print("Please enter valid marks")
            quit()
    except ValueError:
        print("Invalid value")
    remark = ''
    if percentage - previous_year_percentage.get(name) >= 30:
        remark = 'Outstanding improvement.Keep it up.'
    elif percentage - previous_year_percentage.get(name) >= 10:
        remark = 'Have shown improvement.Keep it going.'
    elif previous_year_percentage.get(name) - percentage >= 10:
        remark = 'grades have have fallen.Need improvement.'
    elif previous_year_percentage.get(name) == percentage:
        remark = 'No change'
    else:
        remark = 'Grades have fallen drastically.Should be consistent'
    print(f'''
        Name of student : {name.upper()}
        Total marks : {total} out of 500
        total percentage : {percentage}
        {remark}
        ''')
        

    
