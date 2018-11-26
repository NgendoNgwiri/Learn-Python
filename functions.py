#functions are routines
import car
def print_name(my_name):
    print("my name is" , my_name)
    
def print_age(my_age):
        my_age =int(my_age)
        print("my age is",my_age)
#calling the function
print_name("Christine")
print_age(24)



def add_num(num_1,num_2):
    s_num = num_1 + num_2
    return s_num
    


print(add_num(23,45))

car.print_weight(78)
