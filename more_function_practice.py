def max_num(num1, num2, num3):
    print(max(num1, num2, num3))

def mult_list(*args):
    answer=1
    for i in args:
        answer*= i
    print(answer)

def rev_string(string):
    print(string[::-1])

def num_within(target, range1, range2):
    print (target in range(range1, range2+1))

def pascal(n):
    #uhhh I'm totally lost
    for i in range(n):
        row=[1]
        if i > 0:
            last_row = result[-1]