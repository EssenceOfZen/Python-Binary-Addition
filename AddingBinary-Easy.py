# Binary Addition
# Programmed by ZenOokami
# Website: Http://www.EssenceOfZen.org
# E-Mail: ZaneBlalock@EssenceOfZen.org
#
#Easy Way of doing it
#=========================================#
binary_1 = input("Input a binary number: ")
binary_2 = input("Input second binary number: ")

decimal_1 = int(binary_1, 2)
decimal_2 = int(binary_2, 2)

print(decimal_1)
print(decimal_2)
decimal_sum = decimal_1 + decimal_2
print(decimal_sum)
print(bin(decimal_sum))

