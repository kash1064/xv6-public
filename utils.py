def rev_PGROUNDUP(sz):
    print("***************rev_PGROUNDUP***************")
    pgsize = 4096
    num1 = (sz)+(pgsize-1)
    num2 = ~(pgsize-1)
    result = num1 & num2
    print("pgsize               : {}".format(pgsize))
    print("pgsize[bin]          : {}".format(bin(pgsize)))
    print("(sz)+(pgsize-1)      : {}".format(num1))
    print("(sz)+(pgsize-1)[bin] : {}".format(bin(num1)))
    print("~(pgsize-1)          : {}".format(num2))
    print("~(pgsize-1)[bin]     : {}".format(bin(num2)))
    print("result               : {}".format(result))
    print("result[bin]          : {}".format(bin(result)))
    return result


def main():
    return


if __name__ == '__main__':
    main()