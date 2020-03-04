roll<-c(1:3)
name<-c("Mayur","Sid","Vishu")
class<-c("SYCOMP","SYCOMP","SYCOMP")
student_lst <- list(RollNo = roll, Name = name, Class = class)

student_lst

access<-function(){
	cat("\nEnter Index No. :-  ")
	index<-as.integer(readLines("stdin",1))
	print(student_lst[index])
}
sublist<-function(){
	marks_lst <- list(Sub1 = 45, Sub2 = 54, Sub3 = 60)
	student_lst["Mark"]=marks_lst
	cat("\nSublist Added Successfully")
	return(student_lst)
}
add<-function(){
	cat("\nEnter City To Add  :-  ")
	city<-readLines("stdin",1)
	student_lst["City"]=city
	return(student_lst)
}
del<-function(){
	cat("\nEnter Index To Delete Data  :-  ")
	i<-as.integer(readLines("stdin",1))
	student_lst[i]=NULL
	return(student_lst)
}
updat<-function(){
	cat("\nEnter Name Of Index :-  ")
	name<-readLines("stdin",1)
	cat("\nEnter Data To Update :- ")
	data<-readLines("stdin",1)
	student_lst$name=data
	return(student_lst)
}
choice='y'
while(choice=='y' || choice=='Y'){

	cat("\n1 For Access Element")
	cat("\n2 For Create Sublist")
	cat("\n3 For Add Element")
	cat("\n4 For Remove Element")
	cat("\n5 For Update Element")
	cat("\n6 For Display")
	cat("\nEnter Your Choice :- ")
	ch<-as.integer(readLines("stdin",1))
	switch(
		ch,
		access(),
		student_lst<-sublist(),
		student_lst<-add(),
		student_lst<-del(),
		student_lst<-updat(),
		print(student_lst)
	
	)
	cat("\nDo You Want To Continue :- ")
	choice<-readLines("stdin",1)
	
}

"""
Output  :- 

$RollNo
[1] 1 2 3

$Name
[1] "Mayur" "Sid"   "Vishu"

$Class
[1] "SYCOMP" "SYCOMP" "SYCOMP"

1 For Access Element
2 For Create Sublist
3 For Add Element
4 For Remove Element
5 For Update Element
6 For Display

Enter Your Choice :- 1
Enter Index No. :-  2
$Name
[1] "Mayur" "Sid"   "Vishu"

Do You Want To Continue :- y

1 For Access Element
2 For Create Sublist
3 For Add Element
4 For Remove Element
5 For Update Element
6 For Display

Enter Your Choice :- 2
Sublist Added Successfully

Do You Want To Continue :- y

1 For Access Element
2 For Create Sublist
3 For Add Element
4 For Remove Element
5 For Update Element
6 For Display

Enter Your Choice :- 3
Enter City To Add  :-  Shahada

Do You Want To Continue :- y

1 For Access Element
2 For Create Sublist
3 For Add Element
4 For Remove Element
5 For Update Element
6 For Display

Enter Your Choice :- 6
$RollNo
[1] 1 2 3

$Name
[1] "Mayur" "Sid"   "Vishu"

$Class
[1] "SYCOMP" "SYCOMP" "SYCOMP"

$Mark
[1] 45

$City
[1] "Shahada"

Do You Want To Continue :- y

1 For Access Element
2 For Create Sublist
3 For Add Element
4 For Remove Element
5 For Update Element
6 For Display

Enter Your Choice :- 4
Enter Index To Delete Data  :-  4

Do You Want To Continue :- y

1 For Access Element
2 For Create Sublist
3 For Add Element
4 For Remove Element
5 For Update Element
6 For Display

Enter Your Choice :- 6
$RollNo
[1] 1 2 3

$Name
[1] "Mayur" "Sid"   "Vishu"

$Class
[1] "SYCOMP" "SYCOMP" "SYCOMP"

$City
[1] "Shahada"

Do You Want To Continue :- y

1 For Access Element
2 For Create Sublist
3 For Add Element
4 For Remove Element
5 For Update Element
6 For Display

Enter Your Choice :- 5
Enter Name Of Index :-  Name
Enter Data To Update :- SYCOMP

Do You Want To Continue :- y

1 For Access Element
2 For Create Sublist
3 For Add Element
4 For Remove Element
5 For Update Element
6 For Display

Enter Your Choice :- 6
$RollNo
[1] 1 2 3

$Name
[1] "Mayur" "Sid"   "Vishu"

$Class
[1] "SYCOMP"

$City
[1] "Shahada"

Do You Want To Continue :- n
"""
