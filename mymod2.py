# mymod2.py
# module name : mymod2

import mymod

def main():
    print("독립실행시, 출력됩니다.")

def power(x, y):
    r = 1
    for i in range(y):
        r = mymod.multiply(r, x)

if __name__ == "__main__":
    main()
else:
    print("module name : " + __name__)