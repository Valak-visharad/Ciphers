while(1==1):
    print("\n\n\n\n\t\t:::::::ENCRYPTION SOFTWARE BY VILAKSHAN:::::::")
    original_text=input("YOUR TEXT:\t")
    length=len(original_text)
    squares=[]
    difference=[]
    for i in range(1,100):
        squares.append(i**2)
    if length in squares:
        side=length**(1/2)
    else:
        for q in squares:
            sub=q-length
            if(sub>0):
                difference.append(q-length)
            else:
                continue
        side=(min(difference)+length)**(1/2)
        for s in range(min(difference)):
            original_text+=(" ")
    clear_text=str("")
    last=("")
    for v in range(int(side)):
        clear_text=original_text[v::int(side)]
        last+=clear_text
    print("TEXT BY SOFTWARE:\t",str(last),"\n\t:::::::VILAKSHAN::::::::::")
