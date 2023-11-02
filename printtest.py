import pickle

Class = input("Enter Class: ")
print('\n\n')
print("Admno",'%17s'%("Name"),'%21s'%("Total Marks"),'%10s'%("Percentage"),'%10s'%("Grade"))


with open('STUDNTDATA.bin','rb') as f:
    try:
        while True:
            dat = pickle.load(f)
            if dat['class'] == Class:
                print(dat['Admno'],'%21s'%(dat["Name"]),'%17s'%(dat["Total marks"]),'%10s'%(dat["Percentage"]),'%10s'%(dat["Grade"]))
    except:
        pass

####This to paste
