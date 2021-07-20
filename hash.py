import math

def inp(mh,j):
    mh = list(mh)
    c = math.floor(len(mh)/32)-1
    l = len(mh)%32
    for x in range (0,c):
        for i in range(0,32):
            v1 = ord(mh.pop(32))
            v2 = ord(mh[i])
            tmp = math.floor((v1+v2)/2)
            if (sz(tmp)):
                mh[i] = chr(tmp)
            else:
                mh[i] = msz(tmp,i)
    cnt = 0
    for x in range(0,l):
        v1 = ord(mh.pop(32))
        v2 = ord(mh[cnt])
        tmp = math.floor((v1+v2)/2)
        if (sz(tmp)):
            mh[cnt] = chr(tmp)
        else:
            mh[cnt] = msz(tmp,x)
        cnt = cnt + 1
    mh = "".join(mh)
    return mh

def exp(mh,j):
    mh = list(mh)
    c = math.floor(32/len(mh)) - 1
    l = 32%len(mh)
    tmp = len(mh)
    for x in range(0,c):
        for i in range((tmp*x),(tmp*(x+1))):
            v1 = ord(mh[i])
            v2 = len(mh)
            v3 = (v1 * i) % v2
            if (sz(v3)):
                mh.append(chr(v3))
            else:
                tx = msz(v3,i)
                mh.append(tx)
    tmv = len(mh)
    for x in range(0,l):
        v1 = ord(mh[-x])
        v2 = x + tmv
        v3 = (v1*v2)%math.floor(len(mh)/2)
        if (sz(v3)):
            mh.append(char(v3))
        else:
            tx = msz(v3,x)
            mh.append(tx)
    mh = "".join(mh)
    return mh
    
def sz(x):
    if (48<=x<=57 or 65<=x<=90 or 97<=x<=122):
        return True
    else:
        return False

def msz(x,i):
    x = x+1
    if (sz(x + i)):
        return chr(x+i)
    elif (sz(x + len(r))):
        return chr(x+len(r))
    elif(sz( x + math.floor((len(r) + i)/2))):
        return chr( x + math.floor((len(r) + i)/2))
    else:
        flag = True
        c = 0
        while (flag):
            if (c > 15):
                tmp = 120
                break
            tmp = ((x+i)*len(r))* 219
            while (tmp > 122):
                tmp = tmp % 122
            if (sz(tmp)):
                flag = False
            else:
                x = tmp
            c = c + 1
        return(chr(tmp))
    
def mfx():
    global r
    x = ""
    while(x ==""):
        x = input("Enter Your Message: ")
    
    dt = []
    r = []
    for i in range (0,len(x)):
        dt.append(ord(x[i]))
    s = sum(dt)
    for i in range (0,len(dt)):
        r.append(math.floor(s *(dt[i]%((len(dt)+dt[i])/2))))
    salt = math.floor(((sum(dt)/len(dt)) + (sum(r)/len(r)))/2)
    md = []
    for i in range (0,len(r)):
        x = r[i]
        while(x>salt):
            x  = x % salt
        if (x>(salt/2)):
            while (x > 122):
                x = x % 122
        else:
            while (x > 58):
                x = x % 58
        if (x<33):
            x = math.floor((x + 66)/2)
        if (sz(x)):
            md.append(chr(x))
        else:
            md.append(msz(x,i))
    mh = "".join(md)
    if len(mh)<32:
        mh = exp(mh,i)
    elif len(mh) > 32:
        mh = inp(mh,i)
    print(len(mh))
    print(mh)
    mfx()
mfx()
