ascii_num = input()
if type(ascii_num) == str:
    print(ord(ascii_num))
else:
    print(chr(ascii_num))
