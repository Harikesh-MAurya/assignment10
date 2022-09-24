# 1. Write a python script to print the first 10 multiples of 5.
# 2. Write a python script to print first 10 multiples of N
# 3. Write a python script to print first M multiples of N.
# 4. Write a python script to print the first 10 multiples of N in reverse order.
# 5. Write a python script to print table of user’s choice
# 6. Write a python script to print first N even natural numbers.
# 7. Write a python script to print first N odd natural numbers
# 8. Write a python script to print squares of first N natural numbers.
# 9. Write a python script to print cubes of first N natural numbers.
# 10. Write a python script to display all prime numbers within a range.
# # range
# start = 15
# end = 45


# 1) .............................................................
# for i in range(1,11):
    # print(5*i,end=" ")


# 2) ..........................................................
# n=int(input("Enter n : "))
# for i in range(1,10):
#     print(n*i,end=" ")


# 3) ..........................................................
# m=int(input("Enter M : "))
# n=int(input("Enter N : "))
# for i in range(1,m+1):
#     print(n*i,end=" ")


# 4) ...........................................................
# n=int(input("Enter N : "))
# for i in range(10,0,-1):
#     print(n*i,end=" ")


# 5) ..........................................................
# n=int(input("Enter N : "))
# for i in range(1,11):
#     print(n*i,end=" ")


# 6) ..........................................................
# n=int(input("Enter N : "))
# for i in range(1,n+1):
#     print(2*i,end=" ")


# 7) .........................................................
# n=int(input("Enter N : "))
# for i in range(1,n+1,2):
#     print(i,end=" ")


# 8) .........................................................
# n=int(input("Enter N : "))
# for i in range(1,n+1):
#     print(pow(i,2),end=" ")


# 9) ......................................................
# n=int(input("Enter N : "))
# for i in range(1,n+1):
#     print(pow(i,3),end=" ")


# 10) .......................................................
for i in range(15,45):
        for j in range(2,i):
            if(i%j==0):
                break
            else:
                print(i,end=" ")