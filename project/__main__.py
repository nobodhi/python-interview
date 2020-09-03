import sys


def main(args=None):
     # pylint: disable=import-error
    # import string_problems as sp
    import rotate_matrix as rm
    import chunk_file as cf
    if args is None:
        args = sys.argv[1:]
    # r = sp.is_unique('This dog runs faster than the other dog dude!')
    # print(args, 'is_unique', r)
    rm.rotateMatrix(9)
    # cf.read_json_file()


if __name__ == "__main__":
    main()
