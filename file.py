

#1.  Always Open the resource
fp = open("D:/Python Projects/File Handling/mydocuments/demofile.txt","a")

#print(fp.readline());
#print(fp.readline());
fp.write("OKLABS")

print(fp.read());
  
#2.  Always Close the resource
fp.close();
