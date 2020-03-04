
prime<-function(){
	cat("\n**********************************************\n")
	repeat{
	cat("\nEnter no. To Check Prime Or Not  =  ")
	n=as.numeric(readLines("stdin",1))

	flag=-1
	i=2

	while(i<n){
		if(n%%i==0){
			flag=0		
			break	
		}else{
			flag=1
		}
		i=i+1
	}

	if(flag==1){
		cat(n," Is A Prime No.\n")
	}else{

	cat(n," Is Not A Prime No.\n")
	}
	cat("\nDo You Want to Contionue (y\\n)  =  ")
	ch=readLines("stdin",1)
	if(ch=="n" || ch=="N"){
		break
	}
	cat("\n**********************************************\n")
	}
	cat("\n\n")
}

prime()

"""
Output  :-

**********************************************

Enter no. To Check Prime Or Not  =  6
6  Is Not A Prime No.

Do You Want to Contionue (y\n)  =  y

**********************************************

Enter no. To Check Prime Or Not  =  7
7  Is A Prime No.

Do You Want to Contionue (y\n)  =  n

"""
