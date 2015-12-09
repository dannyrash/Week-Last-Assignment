#Daniel Rash
#CIS-125
#Collaborated with Devin

def gCd(a, b):
    if b==0:
        return a
    else:
        return gCd(a, a%b)
    
def main():
    a=eval(input("Pick a number: "))
    b=eval(input("Pick another number: "))
    print("GCD of",a,",",b,"=",gCd(a,b))

if __name__ == "__main__":
    main()