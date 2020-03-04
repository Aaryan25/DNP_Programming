id <- c(1,2,3)
name <- c("John", "Kirk", "AJ")
age <- c(21,27,18)
employees <- data.frame(ID=id, Name=name, Age=age)
employees

rowno<-3
colno<-3

accesscol<-function(){
	cat("\nEnter Col No. :-  ")
	co<-as.integer(readLines("stdin",1))
	print(employees[,co])
}
accesselement<-function(){
	cat("\nEnter Row No. :-  ")
	ro<-as.integer(readLines("stdin",1))
	cat("\nEnter Col No. :-  ")
	c<-as.integer(readLines("stdin",1))
	print(employees[ro,c])
}

addcol<-function(){
	city<-c("Shahada","Mumbai","Pune")
	employees<-cbind(employees,City=city)
	cat("\nCol Added Successfully")
	return(employees)
}
addrow<-function(){
	lst<-list(4,"Mayur",20,"Shahada")
	employees<-rbind(employees,lst)
	cat("\nRow Added Successfully")
	return(employees)
}
st<-function(){
	cat("\nEnter Col No. For Sorting :-  ")
	sot<-as.integer(readLines("stdin",1))
	print(sort(employees[,sot]))
}
choice='y'

while(choice=='y' || choice=='Y'){
	
	cat("\n1 For Access Column :-  ")
	cat("\n2 For Access Element  :-  ")
	cat("\n3 For Add Column  :-  ")
	cat("\n4 For Add Row  :-  ")
	cat("\n5 For Sort Element  :-  ")
	cat("\n6 For Summary  :-  ")
	cat("\n7 For Display  :-  ")
	cat("\nEnter Your Choice  :-  ")
	ch<-as.integer(readLines("stdin",1))
	
	switch(
		ch,
		accesscol(),
		accesselement(),
		employees<-addcol(),
		employees<-addrow(),
		st(),
		print(summary(employees)),
		print(employees)
		)
	
	cat("\nDo You Want To Continue  :-  ")
	choice<-readLines("stdin",1)
}

"""
Output  :-

  ID Name Age
1  1 John  21
2  2 Kirk  27
3  3   AJ  18

1 For Access Column :-  
2 For Access Element  :-  
3 For Add Column  :-  
4 For Add Row  :-  
5 For Sort Element  :-  
6 For Summary  :-  
7 For Display  :-  

Enter Your Choice  :-  6
       ID        Name        Age      
 Min.   :1.0   AJ  :1   Min.   :18.0  
 1st Qu.:1.5   John:1   1st Qu.:19.5  
 Median :2.0   Kirk:1   Median :21.0  
 Mean   :2.0            Mean   :22.0  
 3rd Qu.:2.5            3rd Qu.:24.0  
 Max.   :3.0            Max.   :27.0  

Do You Want To Continue  :-  y

1 For Access Column :-  
2 For Access Element  :-  
3 For Add Column  :-  
4 For Add Row  :-  
5 For Sort Element  :-  
6 For Summary  :-  
7 For Display  :-  

Enter Your Choice  :-  5
Enter Col No. For Sorting :-  3
[1] 18 21 27

Do You Want To Continue  :-  y

1 For Access Column :-  
2 For Access Element  :-  
3 For Add Column  :-  
4 For Add Row  :-  
5 For Sort Element  :-  
6 For Summary  :-  
7 For Display  :-  

Enter Your Choice  :-  1
Enter Col No. :-  2
[1] John Kirk AJ  
Levels: AJ John Kirk

Do You Want To Continue  :-  y

1 For Access Column :-  
2 For Access Element  :-  
3 For Add Column  :-  
4 For Add Row  :-  
5 For Sort Element  :-  
6 For Summary  :-  
7 For Display  :-  

Enter Your Choice  :-  2
Enter Row No. :-  3
Enter Col No. :-  1
[1] 3

Do You Want To Continue  :-  y

1 For Access Column :-  
2 For Access Element  :-  
3 For Add Column  :-  
4 For Add Row  :-  
5 For Sort Element  :-  
6 For Summary  :-  
7 For Display  :-  

Enter Your Choice  :-  3
Col Added Successfully
Do You Want To Continue  :-  y

1 For Access Column :-  
2 For Access Element  :-  
3 For Add Column  :-  
4 For Add Row  :-  
5 For Sort Element  :-  
6 For Summary  :-  
7 For Display  :-  

Enter Your Choice  :-  4
Row Added Successfully
Do You Want To Continue  :-  y

1 For Access Column :-  
2 For Access Element  :-  
3 For Add Column  :-  
4 For Add Row  :-  
5 For Sort Element  :-  
6 For Summary  :-  
7 For Display  :-  

Enter Your Choice  :-  7
  ID	 Name Age    City
1  1  John  21 Shahada
2  2  Kirk  27  Mumbai
3  3    AJ  18    Pune
4  4 Mayur  20 Shahada

Do You Want To Continue  :-  n

"""
