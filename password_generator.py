command=input("\t\tCommand SYNTAX\nminimum_digits\tmaximum_digits\tincludes(numbers/capitals/smalls/symbols)\n")
total={"small":"qwertyuiopasdfghjklzxcvbnm","cap":"QWERTYUIOPASDFGHJKLZXCVBNM","num":"1234567890","sym":"~`!@#$%^&*(),./;'[]\<>?:{}-_=+"}
com,j=tuple(),str()
for i in command:
    if(i==" "):
        com+=(j,)
        j=str()
    else:
        j+=i
min,max,inclusions=com[0],com[1],com[2]











