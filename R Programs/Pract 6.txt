new_hope <- c(460.998, 314.4)
empire_strikes <- c(290.475, 247.900)
return_jedi <- c(309.306, 165.8)
mat<- rbind(new_hope, empire_strikes, return_jedi)
r=3
c=2
roname<-c("A New Hope","The Empire Strikes Back","Return of the Jedi")
rownames(mat)<-roname
coname<-c("US","non-US")
colnames(mat)<-coname

mat

addrow<-function(){
	cat("\nEnter Star War Movie Name  :-  ")
	mname<-readLines("stdin",1)
	cat("\nEnter Data  :- ")
	mat<-rbind(mat,as.numeric(c(readLines("stdin",c))))
	roname<-c(roname,mname)
	rownames(mat)<-roname
	return(mat)
}
addcol<-function(){
	cat("\nEnter Box Office Name  :-  ")
	bname<-readLines("stdin",1)
	cat("\nEnter Data  :- ")
	mat<-cbind(mat,as.numeric(c(readLines("stdin",r))))
	coname<-c(coname,bname)
	colnames(mat)<-coname
	return(mat)
}
accessrow<-function(){
	cat("\nEnter Row Number  :-  ")
	ro<-as.integer(readLines("stdin",1))
	print(mat[ro,])
}
accesscol<-function(){
	cat("\nEnter Col Number  :-  ")
	co<-as.integer(readLines("stdin",1))
	print(mat[,co])
}
choice<-'Y'
while(choice=='y' || choice=='Y'){
cat("\n1 For Add Row ")
cat("\n2 For Add Col ")
cat("\n3 For Access Row ")
cat("\n4 For Access Col ")
cat("\n5 For ColSums ")
cat("\n6 For RowSums ")
cat("\n7 For Display Mat ")
cat("\nEnter Your Choice :-  ")
ch<-as.numeric(readLines("stdin",1))

cat("\n\n")
switch(
	ch,
	mat<-addrow(),
	mat<-addcol(),
	accessrow(),
	accesscol(),
	print(colSums(mat)),
	print(rowSums(mat)),
	print(mat)
)
if(ch==1){
	r<-r+1
}
if(ch==2){
	c<-c+1
}
cat("\nDo You Want To Continue  :-  ")
choice<-readLines("stdin",1)

}

"""
Output :-
                             US non-US
A New Hope              460.998  314.4
The Empire Strikes Back 290.475  247.9
Return of the Jedi      309.306  165.8

1 For Add Row 
2 For Add Col 
3 For Access Row 
4 For Access Col 
5 For ColSums 
6 For RowSums 
7 For Display Mat 

Enter Your Choice :-  1
Enter Star War Movie Name  :-  Mayur

Enter Data  :- 345.346
456.532

Do You Want To Continue  :-  y

1 For Add Row 
2 For Add Col 
3 For Access Row 
4 For Access Col 
5 For ColSums 
6 For RowSums 
7 For Display Mat 

Enter Your Choice :-  2
Enter Box Office Name  :-  India
Enter Data  :- 234.346
235.346
346.456
342.543 

Do You Want To Continue  :-  y

1 For Add Row 
2 For Add Col 
3 For Access Row 
4 For Access Col 
5 For ColSums 
6 For RowSums 
7 For Display Mat 

Enter Your Choice :-  3
Enter Row Number  :-  2
     US  non-US   India 
290.475 247.900 235.346 

Do You Want To Continue  :-  y

1 For Add Row 
2 For Add Col 
3 For Access Row 
4 For Access Col 
5 For ColSums 
6 For RowSums 
7 For Display Mat 

Enter Your Choice :-  4
Enter Col Number  :-  3
 A New Hope The Empire Strikes Back      Return of the Jedi 
    234.346                 235.346                 346.456 
      Mayur 
    342.543 

Do You Want To Continue  :-  y

1 For Add Row 
2 For Add Col 
3 For Access Row 
4 For Access Col 
5 For ColSums 
6 For RowSums 
7 For Display Mat 

Enter Your Choice :-  5

      US   non-US    India 
1406.125 1184.632 1158.691 

Do You Want To Continue  :-  y

1 For Add Row 
2 For Add Col 
3 For Access Row 
4 For Access Col 
5 For ColSums 
6 For RowSums 
7 For Display Mat 

Enter Your Choice :-  6

 A New Hope The Empire Strikes Back      Return of the Jedi 
   1009.744                 773.721                 821.562 
      Mayur 
   1144.421 

Do You Want To Continue  :-  y

1 For Add Row 
2 For Add Col 
3 For Access Row 
4 For Access Col 
5 For ColSums 
6 For RowSums 
7 For Display Mat 
Enter Your Choice :-  7

                          US  non-US   India
A New Hope              460.998 314.400 234.346
The Empire Strikes Back 290.475 247.900 235.346
Return of the Jedi      309.306 165.800 346.456
Mayur                   345.346 456.532 342.543

Do You Want To Continue  :-  n

"""

