# def sum(num1, num2):
#     result=num1+num2
#     return result
# total =sum (99,11)
# print('total: ' ,total)
#args
def all_sum(num1,num2,*numbers):
    print(numbers)
    sum=0
    for num in numbers:
        print(num)
        sum=sum+num 
        return sum
    total=all_sum(45,46,89,11,81,5,2,77)
    print('all_sum: ',total)
    