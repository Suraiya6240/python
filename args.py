def full_name(first,last):
    name=f'full name  is : {first} {last}'
    return name
name=full_name('suraiya','bilkis')
print (name)


def famous_name(first,last,title,**addition):
    name=f'{title} {first} {last}'
    # print(addition['title'])
    for key,value in addition.items():
        print(key,value)
    return name
name=famous_name(first='suraiya' ,last='bilkis',title='enginner',addition='miya')
print(name)


# def a_lot(num1,num2):
#     sum =num1+num2
# mult = num1*num2
# remain = num1-num2
# return [sum, mult,remain]
# everything =a_lot(55,21)
# print(everything)