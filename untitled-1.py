def incr(index):
    if(abs(index)>len(temp)):
        temp.insert(0,charset[0])
    else:
        if(temp[index]==charset[-1]):
            temp[index]=charset[0]
            incr(index-1)
        else:
            temp[index]=charset[charset.index(str(unichr(temp[index])))+1]
