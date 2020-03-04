tshirt <- c("M", "L", "S", "S", "L", "M", "L", "M")
tshirt_factor <- factor(tshirt, ordered = TRUE,levels = c("S", "M", "L"))

tshirt_factor

Rename<-function(){
	cat("\nEnter New Level Order  :-  ")
	change<-c(readLines("stdin",3))
	levels(tshirt_factor)=change
	return(tshirt_factor)
}
Reorder<-function(){
	cat("\nEnter New Level Order  :-  ")
	change<-c(readLines("stdin",3))
	tshirt_factor<-factor(tshirt_factor,levels=change)
	return(tshirt_factor)
}
compare<-function(){
	cat("\nEnter 1st Index :- ")
	no1<-as.integer(readLines("stdin",1))
	cat("\nEnter 2nd Index :- ")
	no2<-as.integer(readLines("stdin",1))
	print(tshirt_factor[no1]>tshirt_factor[no2])
}

choice='y'
while(choice=='y' || choice=='Y')
{
	cat("\n1 For Reorder level")
	cat("\n2 For Rename level")
	cat("\n3 For Compare Element")
	cat("\n4 For Display")
	cat("\nEnter Your Choice")
	ch<-as.integer(readLines("stdin",1))
	
	switch(
		ch,
		tshirt_factor<-Reorder(),
		tshirt_factor<-Rename(),
		compare(),
		print(tshirt_factor)
		)
	cat("\n Do You Want To Continue :- ")
	choice<-readLines("stdin",1)	
}

"""
Output  :-

[1] M L S S L M L M
Levels: S < M < L

1 For Reorder level
2 For Rename level
3 For Compare Element
4 For Display

Enter Your Choice  :- 1
Enter New Level Order  :-  M
L
S

Do You Want To Continue :- y

1 For Reorder level
2 For Rename level
3 For Compare Element
4 For Display

Enter Your Choice  :- 4
[1] M L S S L M L M
Levels: M < L < S

Do You Want To Continue :- y

1 For Reorder level
2 For Rename level
3 For Compare Element
4 For Display

Enter Your Choice  :- 2
Enter New Level Order  :-  S_s
M_m
L_l    

Do You Want To Continue :- y

1 For Reorder level
2 For Rename level
3 For Compare Element
4 For Display

Enter Your Choice  :- 4
[1] S_s M_m L_l L_l M_m S_s M_m S_s
Levels: S_s < M_m < L_l

Do You Want To Continue :- y

1 For Reorder level
2 For Rename level
3 For Compare Element
4 For Display

Enter Your Choice  :- 3
Enter 1st Index :- 2
Enter 2nd Index :- 5
[1] FALSE

Do You Want To Continue :- n

"""
