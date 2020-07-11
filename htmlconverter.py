import keyword
def converter():
    line=input("Input you'r python code here: ")

    purple=["print","range","len","int","str","list","tuple","dict"]
            
    line=line.split()
    
    HtmlText="<p>"
    for i in range(len(line)):
        if(keyword.iskeyword(line[i])):
            HtmlText+=' <font color="orange">'+str(line[i])+" "+'</font> '  
        elif(line[i][:5] in purple and line[i][6:9] in purple):
            HtmlText+=' <font color="purple">'+str(line[i][:5])+'</font>'+str(line[i][5])+ '<font color="purple">'+str(line[i][6:9])+'</font>'+ str(line[i][9:])

        elif(line[i][:5] in purple):
            HtmlText+=' <font color="purple">'+str(line[i][:5])+" "+'</font> '+str(line[i][5:])
        
        elif(line[i] in purple):
            HtmlText+=' <font color="purple">'+str(line[i])+" "+'</font> '
        elif(line[i][0]=='"'):
            HtmlText+=' <font color="green">'+str(line[i])+" "+'</font> '
        else:
            HtmlText+=str(line[i])

    HtmlText+="</p>"
    return HtmlText
