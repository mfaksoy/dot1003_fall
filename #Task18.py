#Task18
varsayı = int(input("Sayı"))

if varsayı % 3 ==0 and varsayı % 5 ==0:
    print("FizzBuzz")
elif varsayı % 3 ==0 :
    print ("Fizz")
elif varsayı % 5 ==0:
    print("Buzz")
else:
    print("3 or 5 cant")
