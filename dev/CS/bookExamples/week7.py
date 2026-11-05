
players_roster = {
    1: {"name": "Alex", "jersey": 23, "rating": 85},
    2: {"name": "Jordan", "jersey": 7, "rating": 92},
    3: {"name": "Sam", "jersey": 41, "rating": 78},
    4: {"name": "Chris", "jersey": 12, "rating": 88},
    5: {"name": "Taylor", "jersey": 3, "rating": 95},
    6: {"name": "Morgan", "jersey": 34, "rating": 81},
    7: {"name": "Casey", "jersey": 19, "rating": 90}
}

def exact_change(value):
    QUARTER = 25
    DIME = 10
    NICKLE = 5

    if value == 0:
        return "no change"

    num_quarters = value//QUARTER
    remainder_from_quarters = value%QUARTER
    num_dimes = remainder_from_quarters//DIME
    remainder_from_dimes = remainder_from_quarters%DIME
    num_nickles = remainder_from_dimes//NICKLE
    num_pennies = remainder_from_dimes%NICKLE
    return (num_pennies, num_nickles, num_dimes, num_quarters)

print((-5)**2)
# # Define your functions here
#
# if __name__ == "__main__":
#     # Type your code here.
#     def is_list_mult10(num_count,num_list):
#         count = 0
#         for i in range(num_count):
#             if(num_list[i]%10==0):
#                 count+=1
#             else:
#                 continue
#         if(len(num_list)==count):
#             return True
#         else:
#             return False
#
#     def is_list_no_mult10(num_count,num_list):
#         count=0
#         for i in range(num_count):
#             if(num_list[i]%10!=0):
#                 count+=1
#             else:
#                 continue
#         if(len(num_list)==count):
#              return True
#         else:
#             return False
#
#     num_count = int(input())
#     num_list =[]
#     for i in range(num_count):
#         num=int(input())
#         num_list.append(num)
#
#     if(is_list_mult10(num_count,num_list)):
#         print("all multiple of 10")
#     elif(is_list_no_mult10(num_count,num_list)):
#         print("no multiple of 10")
#     else:
#         print("mixed values")


# def find_max(num_1, num_2):
#    max_val = 0.0
#
#    if (num_1 > num_2):  # if num1 is greater than num2,
#       max_val = num_1   # then num1 is the maxVal.
#    else:                # Otherwise,
#       max_val = num_2   # num2 is the maxVal
#    return max_val
#
# max_sum = 0.0
#
# num_a = float(input())
# num_b = float(input())
# num_y = float(input())
# num_z = float(input())

# """ Your solution goes here """
# max_sum = find_max(find_max(num_a,num_b),find_max(num_y,num_z))
# print(f"max_sum is: {max_sum}")
