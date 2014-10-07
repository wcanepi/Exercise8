
f = open("short.txt")
input_text = f.read()
input_text = input_text.strip().split()
print input_text

for i in range(len(input_text), -2):
    print i
    tup1 = input_text[i]
    tup2 = input_text[i+1]
    out_tuple = (tup1, tup2)
    i += 1
    #return out_tuple     
    print tup1