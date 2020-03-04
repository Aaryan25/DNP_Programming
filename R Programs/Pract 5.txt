#Program For Vector Operations On
#5 Day Earning Of People
#Practical No  :-  5

ch='y'
cat("\nEnter Earnings Of 5 Days :-  \n")
earn<-as.numeric(readLines("stdin",5))
names(earn)<-c("Mon","Tue","Wed","Thus","Fri")

ftotal<-function(){
	cat("Total Earn  :-  ",sum(earn))
}
fsort<-function(){
	searn<-sort(earn)
	print(searn)
}
access<-function(){
	cat("\nEnter Index No. To Access Element  :-  ")
	index<-as.numeric(readLines("stdin",1))
	if(index>=1 || index<=5){
		cat("Earning At Index  ",index," is :- ",earn[index])
	}else{
		cat("\nEnter Proper Index")
	}
}
up2date<-function(){
	cat("\nEnter Index No. To Update Element  :-  ")
	index<-as.numeric(readLines("stdin",1))
	cat("\nEnter Earning  :-  ")
	earnup<-as.numeric(readLines("stdin",1))
	if(index>=1 || index<=5){
		earn[index]<-earnup
		cat("\nYour Earning Is Updated\n")
	}else{
		cat("\nEnter Proper Index")
	}
	return(earn)
}
display<-function(){
	print(earn)
}

while(ch=='y' || ch=='Y'){	
	cat("\n1 for sum all Earnings")
	cat("\n2 for Sort Earnings")
	cat("\n3 for Access Particular Earnings")
	cat("\n4 for Update Particular Earnings")
	cat("\n5 for Display Earning")
	cat("\nEnter Your Choice  :-  ")
	choice<-as.numeric(readLines("stdin",1))
	cat("\n")

	switch(
		choice,
		ftotal(),
		fsort(),
		access(),
		earn<-up2date(),
		display()
	)	

	cat("\nDo You Want To Continue  :-  ")
	ch<-readLines("stdin",1)
	cat("\n\n")
}

"""
Output  :-

Enter Earnings Of 5 Days :-  
567
785
543 
655
345

1 for sum all Earnings
2 for Sort Earnings
3 for Access Particular Earnings
4 for Update Particular Earnings
5 for Display Earning

Enter Your Choice  :-  1
Total Earn  :-   2895

Do You Want To Continue  :-  y

1 for sum all Earnings
2 for Sort Earnings
3 for Access Particular Earnings
4 for Update Particular Earnings
5 for Display Earning

Enter Your Choice  :-  2
 Fri  Wed  Mon Thus  Tue 
 345  543  567  655  785 

Do You Want To Continue  :-  y

1 for sum all Earnings
2 for Sort Earnings
3 for Access Particular Earnings
4 for Update Particular Earnings
5 for Display Earning

Enter Your Choice  :-  3
Enter Index No. To Access Element  :-  4
Earning At Index   4  is :-  655

Do You Want To Continue  :-  y

1 for sum all Earnings
2 for Sort Earnings
3 for Access Particular Earnings
4 for Update Particular Earnings
5 for Display Earning

Enter Your Choice  :-  4
Enter Index No. To Update Element  :-  4
Enter Earning  :-  777
Your Earning Is Updated

Do You Want To Continue  :-  y

1 for sum all Earnings
2 for Sort Earnings
3 for Access Particular Earnings
4 for Update Particular Earnings
5 for Display Earning

Enter Your Choice  :-  5
 Mon  Tue  Wed Thus  Fri 
 567  785  543  777  345 

Do You Want To Continue  :-  n

"""
