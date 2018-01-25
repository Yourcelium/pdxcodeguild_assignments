def get_check_diget(num):
    check_diget = num[len(num) - 1]
    return check_diget
#
def double_every_other_number(reversed_num):
    doubled= []
    count = 0
    for i in reversed_num:
        if count == 0:
            doubled.append(i*2)
            count += 1
        else:
            doubled.append(i)
            count -= 1
    return doubled

def nine_subtraction(num):
    new_num = []
    for i in num:
        if i > 9:
            new_num.append(i-9)
        else:
            new_num.append(i)
    return new_num
#
def run_credit_card_check():
    number = input('What number would you like me to check')
    check_diget = get_check_diget(number)
    sliced_num = number[:len(number)-1]
    reversed_num = sliced_num[::-1]
    reversed_num_lst = [int(x) for x in reversed_num]
    doubled_num_list = double_every_other_number(reversed_num_lst)
    subtracted_nine = nine_subtraction(doubled_num_list)
    sum_num = str(sum(subtracted_nine))
    possible_check_diget = sum_num[1]
    print(check_diget)
    print(reversed_num)
    print(reversed_num_lst)
    print(doubled_num_list)
    print(subtracted_nine)
    print(sum_num)
    print(possible_check_diget)
    if check_diget == possible_check_diget:
        print('VALID')
    else:
        print('INVALID')

run_credit_card_check()

# 4556737586899855
