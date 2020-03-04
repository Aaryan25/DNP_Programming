ch='y'
while(ch=='y' || ch=='Y'){
	cat("\n","*******Program For Student Result*******")
	cat("\n","Enter No. Of Subjects  :-  ")
	sub<-as.numeric(readLines("stdin",1))

	cat("\n","Enter Marks For ",sub," Subjects  :- \n")
	marks<-c(as.numeric(readLines("stdin",sub)))

	print(marks)
	total=sum(marks)
	cat("\nTotal  :-  ",total)
	per<-total/sub
	cat("\nPercentage  :-   ",per,"%")

	if(per>=35){
		if(per>=50){
			if(per>=75){
				cat("\nGrade A")
			}else{
			cat("\nGrade B")
			}
		}else{
			cat("\nGrade C")
		}
	}else{
		cat("\nFail")
	}
	cat("\nDo You Want To Continue  :-  ")
	ch=readLines("stdin",1)
	cat("\n\n")
}

"""
Output  :- 
 *******Program For Student Result*******
 Enter No. Of Subjects  :-  3
 Enter Marks For  3  Subjects  :- 
67
78
76
[1] 67 78 76

Total  :-   221
Percentage  :-    73.66667 %
Grade B
Do You Want To Continue  :-  y


 *******Program For Student Result*******
 Enter No. Of Subjects  :-  4
 Enter Marks For  4  Subjects  :- 
87
76
78
88
[1] 87 76 78 88

Total  :-   329
Percentage  :-    82.25 %
Grade A
Do You Want To Continue  :-  n

"""
