# Binary Addition
# Programmed by ZenOokami
# Website: Http://www.EssenceOfZen.org
# E-Mail: ZaneBlalock@EssenceOfZen.org
#
# This program was rather rushed for a particular viewer. I will update this to be more presentable later.
#-----------
# The program was built to add simple bytes. Going over will result in an error.
# Will add a cap to limit the final product.
#-----------

# Import modules/libraries
import eoz_module

#Full Way of doing it - Check the easy file for shorter faster method
#=========================================#
# Functions

def add_indexes(index_1, index_2):
    return (int(index_1)+int(index_2))

def version():
    current_version = '1.2.0'

    if(current_version == '1.0.0'):
        print("Version: " + current_version)
        print("* Created the program.")

    elif(current_version == '1.2.0'):
        print("Version: " + current_version)
        print("* Updated functions")
        print("* Cleaned up the program")

    else:
        print(" Error with Function: \"version()\"")
    

def footer():
    print("Thank you for using Essence of Zen's program!")
    print("I created this program in hopes to help other new programmers learn more about algorithms and binary")
    print("There are a lot of improvements that this program can be given, I might take the time to do so later on.")
    print("-ZenOokami")
    print("\nwww.EssenceOfZen.org")

def add_arrays(array_1, array_2):
    #print("TEST Start function")
    carry = 0
    #Convert elements into ints
    int_array_1 = [int(index) for index in array_1]
    int_array_2 = [int(index) for index in array_2]
    time = 7
    final_array = [0, 0, 0, 0, 0, 0, 0, 0]
    #print("TEST Made it to step 1")


    #We create our meat of the program now
    while( time > -1):
        final_array[time] = int_array_1[time] + int_array_2[time]
        time -= 1
        #TEST print(time)

    #print("TEST completed first loop") 
    #now that we have our final array, we need to convert them to binary again
    #We start at the end of the array and think that 3 = 1 with a carry, 2 = 0 with a carry
    #and 1 = 1 without a carry, finally 0 = 0 without a carry
    check = 7
    while(check > -1):
        final_array[check] = final_array[check] + carry
        if(final_array[check] == 3):
            final_array[check] = 1
            carry = 1
            check -= 1
        elif(final_array[check] == 2):
            final_array[check] = 0
            carry = 1
            check -= 1
        elif(final_array[check] == 1):
            final_array[check] = 1
            carry = 0
            check -= 1
        elif(final_array[check] == 0):
            final_array[check] = 0
            carry = 0
            check -= 1
        else:
            print("something went wrong")
    
    #print("TEST " +final_array)
    return final_array

def set_binary_length(binary):
    while(len(binary) < 8):
        binary.insert(0, '0')
    return binary

#-----------------------------
# The main function which runs the core of the code
def main():
    version()
    print()
    eoz_module.print_information()

    #Get input from user
    user_binary_1 = input("Input binary number: ")
    user_binary_2 = input("Input binary number: ")
    print()

    #Let's make them into an array now 
    user_binary_1 = list(user_binary_1)
    user_binary_2 = list(user_binary_2)

    #print them to check
    print("User Binary input 1: " + ''.join(user_binary_1))
    print("User Binary input 2: " + ''.join(user_binary_2))

    #Now, we need to make sure both binary numbers have the same length of numbers
    user_binary_1 = set_binary_length(user_binary_1) #Now using the new function
    user_binary_2 = set_binary_length(user_binary_2)


    #We can then print to check the arrays
    print("\nPrinting New Arrays")
    print(user_binary_1)
    print(user_binary_2)
    print()

    #Print out the compressed text
    print("Printing New Arrays as compressed Binary")
    print("Binary 1: " + ''.join(user_binary_1))
    print("Binary 2: " + ''.join(user_binary_2))

    #Testing function
    #my_sum = add_indexes(user_binary_1[7], user_binary_2[7])
    #print(my_sum)


    print()
    final_array_sum = add_arrays(user_binary_1, user_binary_2)
    print("Final Array")
    print(final_array_sum)
    string_final_array_sum = [str(index) for index in final_array_sum]
    print("Final Binary: " + ''.join(string_final_array_sum))

    print()
    footer()
#---------------------------------

main()
