# Write a File
f=open("demo.txt","w")
f.write("Hello Harsh Here")
f.close()

#Append and add content in File

f=open("demo.txt","w")
msg=["raj","is","here"]
for i in msg:
    f.write(i)
f.close()

#Reading File
f=open("demo.txt","r+")
print(f.read())
#print(f.readline()) #read only First Line by using readline()
#print(f.readline()) #reading 2nd line of file
f.close()

f=open("demo.txt","r+")
f.write("Something will add soon ..")
f.close()

f=open("demo.txt","r+")
print(f.read())