def swap_list(list):
    middleindex = (len(list)-1)//2
    x = list[middleindex]
    list[middleindex]=list[len(list)-1]
    list[len(list)-1] = x
    return list