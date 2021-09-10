#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    size = (len(sys.argv) - 1)
    if size == 0:
        print('0 arguments.')
    elif size == 1:
        print('{:d} argument:'.format(size))
        print('{:d}: {:s}'.format(size, sys.argv[size]))
    else:
        index = 1
        print('{:d} arguments:'.format(size))
        while index < (len(sys.argv)):
            print('{:d}: {:s}'.format(index, sys.argv[index]))
            index += 1
