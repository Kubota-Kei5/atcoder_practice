# %%
def check_subsequence(s,t):
    for w in range(1, len(s)):
        for c in range(w):
            now = []
            for i in range(c, len(s), w):
                now.append(s[i])
            if "".join(now) == t:
                return "Yes"
    return "No"

if __name__ == "__main__":
    s,t=map(str,input().split())
    print(check_subsequence(s, t))

 # %%

def check_vertical_reading (s,t):
    for w in range(1,len(s)):
        for c in range(w):
            now=[]
            for i in range(c,len(s),w):
                now.append(s[i])
            if "".join(now)==t:
                return "Yes"
    return "No"

if __name__ =="__main__":
    s,t = map(str,input().split())
    print(check_vertical_reading(s,t))