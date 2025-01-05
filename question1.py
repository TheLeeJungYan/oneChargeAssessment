# TIME TAKEN: 5 MIN
def print_staircase(n):
    for i in range(n):
        hashtag = i+1
        space = n - hashtag
        print(' '*space+'#'*hashtag)
        

if __name__ =="__main__":
    n = int(input('please enter the height of the stair case : '))
    print_staircase(n)
