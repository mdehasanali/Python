name=['Ehasan','mahi']
f=open('test.txt','w')
for c in name:
    f.write("%s "%c)
f=open('test.txt','r')
print(f.read())
