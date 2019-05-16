import sys

def main(args=None):
    import string_problems as sp # pylint: disable=import-error
    import rotate_matrix as rm # pylint: disable=import-error
    if args is None:
        args = sys.argv[1:]
    r = sp.isUnique('This dog runs faster than the other dog dude!')
    print (args, 'isUnique', r)
    rm.rotateMatrix(9)

if __name__ == "__main__":
    main()