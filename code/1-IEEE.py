import struct
value = -14041.1

buff = struct.pack(">f",value)
he = list(buff.hex())
ans = ""

for i in he:
    a = str(bin(int(i,16))[2:])
    if len(a) == 3: a = "0"+a
    ans += a
print(ans)