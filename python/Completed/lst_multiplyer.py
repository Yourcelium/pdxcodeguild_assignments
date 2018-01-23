

def lst_muliplyer(list, n):
    multuplied_lst = []
    for i in list:
        if i == 0:
            continue
        else:
            multuplied_lst.append(i*n)
    print(multuplied_lst)
    return multuplied_lst
