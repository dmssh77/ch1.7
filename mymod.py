# module name: mymod

def main():
    print("최상의 모듈( 실행모듈 )")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("mymod.py ??? " + __name__)

if __name__ == "__main__":
    main()
else:
    print("module name : " + __name__)