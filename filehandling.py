

# How to get user input in python ?

msg = input('Please write down something ');
print(msg)

# Always open the file
fp = open('input.txt',"a")  #a = append mode

fp.write(msg)

# Always close the file
fp.close()

fp = open('input.txt',"r")

print(fp.read())

fp.close()
