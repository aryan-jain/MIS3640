msg = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


for i in msg:
    if( (ord(i) in range(65,88)) or (ord(i) in range(97, 120))):
        letter = chr(ord(i)+2)
    #else if( (ord(i) in range(89,90)) or (ord(i) in range(121,122))):
    else:
        letter = chr(ord(i)-24)
    print(letter)


input()