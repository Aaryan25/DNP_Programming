choice='y'
while(choice=='y' || choice=='Y' ){
	cat("\n*******************Program For Geometrical Objects*******************")
	
	cat("\n\n******Area Of Rectangle******\n")
	cat("\nEnter Length  :-  ")
	l<-as.numeric(readLines("stdin",1))
	cat("\nEnter Breadth  :-  ")
	b<-as.numeric(readLines("stdin",1))
	area<-l*b
	cat("Area  :-  ",area)	
	
	cat("\n\n******Area Of Triangle******\n")
	cat("\nEnter Length  :-  ")
	l<-as.numeric(readLines("stdin",1))
	cat("\nEnter Height  :-  ")
	h<-as.numeric(readLines("stdin",1))
	area<-l*h*0.5
	cat("Area  :-  ",area)
	
	cat("\n\n******Area Of Square******\n")
	cat("\nEnter Base  :-  ")
	b<-as.numeric(readLines("stdin",1))
	area<-b*b
	cat("Area  :-  ",area)
	
	cat("\n\n******Area Of Circle******\n")
	cat("\nEnter radius  :-  ")
	r<-as.numeric(readLines("stdin",1))
	area<-r*r*3.14
	cat("Area  :-  ",area)
	
	cat("\nDo you Want To Continue  :-  ")
	choice<-readLines("stdin",1)
}

if(F){
*******************Program For Geometrical Objects*******************

******Area Of Rectangle******

Enter Length  :-  6
Enter Breadth  :-  7
Area  :-   42

******Area Of Triangle******

Enter Length  :-  8
Enter Height  :-  7
Area  :-   28

******Area Of Square******

Enter Base  :-  5
Area  :-   25

******Area Of Circle******

Enter radius  :-  10
Area  :-   314
Do you Want To Continue  :-  n

}
