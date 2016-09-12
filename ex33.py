def loop_throug(change_num):
    i = 0
    numbers = []
    while i < change_num:
        print "At the top i is %d" % i
        numbers.append(i)
        i += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

print "The numbers: %r " % loop_throug(1)
