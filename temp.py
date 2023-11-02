import pickle

with open('studdat.bin','wb') as fout:
    dic = {'Admno':1,'Name':'Ajay AB','Class':'XII B','Total Marks':460,'Percentage':92.00,'Grade':'A'}
    pickle.dump(dic,fout)

