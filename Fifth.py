def removeduplicate(str, n):
    s = set()
    for i in str:
        s.add(i)
    st =""
    for i in s:
        st = st+i
    return st
str = "geeksforgeeks"
n = len(str)
print(removeduplicate(list(str), n))