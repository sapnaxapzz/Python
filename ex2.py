def isWhiteLine(str1):
    r=str1.strip();
    s=r.replace(" ","");
    print();
    if s==s.isspace():
        print('true');
    else:
        print(s);

def fileExists(file):
    try:
        file=input("pathname");
        with open(file) as f:
            str1 = list(f)
            str2 = ''.join(str(e) for e in str1)
        isWhiteLine(str2);
    except FileNotFoundError:
        return False

fileExists('demo.txt');
