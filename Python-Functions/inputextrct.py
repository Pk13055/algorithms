# compatible with python 2.7.x and up
'''
    use this to extract input into variables
    function returns a list of integer converted inputs
'''


def inputextract(x):
    input_vars = map(int, x.split())
    return input_vars


def main():
    inputextract(input())

if __name__ == '__main__':
    main()
