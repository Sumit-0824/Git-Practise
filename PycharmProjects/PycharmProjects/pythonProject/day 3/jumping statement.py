#Continue
for i in range(1,10):
    if i==5:
        continue
    print(i)
print("***********************************")
#Break
for i in range(1,10):
    if i==7:
        break
    print(i)
print("Program exited")
print("***********************************")

#multiple continue
for i in range(1,10):
    if i==5 or i==7:
        continue
    print(i)
print("Program exited")

