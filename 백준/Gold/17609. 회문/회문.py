import sys

def chk(word,left,right):
    while (left < right):
        if (word[left] == word[right]):
            left += 1
            right -= 1
        else:
            return False
    return True

def isP(word):
    left = 0
    right = len(word) - 1
    while (left < right):
        if (word[left] == word[right]):
            left += 1
            right -= 1
        else:
            chk1 = chk(word,left+1,right)
            chk2 = chk(word,left,right-1)
            if(chk1 or chk2):
                return 1
            else:
                return 2
    return 0

n = int(sys.stdin.readline())
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    print(isP(word))