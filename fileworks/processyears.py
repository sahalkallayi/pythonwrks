
f_read=open("C:\\Users\\User\\OneDrive\\Desktop\\PythonWorks\\fileworks\\years.txt","r")
f_centuary=open("C:\\Users\\User\\OneDrive\\Desktop\\PythonWorks\\fileworks\\centuary.txt","w")
f_noncentuary=open("C:\\Users\\User\\OneDrive\\Desktop\\PythonWorks\\fileworks\\noncentuary.txt","w")

for year in f_read:

    y=int(year.rstrip("\n"))

    if y%100==0:

        f_centuary.write(str(y)+"\n")

    else:

        f_noncentuary.write(str(y)+"\n")



