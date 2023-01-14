val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
roman_ = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

num = int(input("Enter a number: "))
roman = ""

for i  in range(len(val)):
    while (val[i] <= num):
        roman += roman_[i]
        num -= val[i]
    if  num == 0:
        break

print(roman)
