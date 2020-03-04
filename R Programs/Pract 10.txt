#Practical No. = 10
#Roll No. = 
#Aim = Program to visualize given data using graphics function

name <- c("Maharashtra","Goa","Utter Pradesh","Himachal Pradesh","Assam","West Bengal","Kerala","Tamil Nadu")
region <- c("West","West","North","North","Eest","West","South","South")
area <- c(307.71,3.70,243.29,55.67,78.43,88.75,38.86,130.06)
population <- c(11.23,0.14,19.98,0.68,3.11,9.13,3.33,7.21)

state_info <- data.frame(name,region,area,population)

cat("\n\tState_info DataFrame =\n")
state_info

temprature <- c(0,20,40,60,80,100,120,140,160,180)
pressure <- c(0.0002,0.0012,0.0600,0.0300,0.0900,0.2700,0.7500,1.8500,4.2000,8.8000)

mercury <- data.frame(temprature,pressure)

cat("\n\tMercury DataFrame =\n")
mercury

sales <- c(231,156,10,519,437,487,299,195,20,342)
ads <- c(8.2,6.9,3.0,12.0,10.6,4.2,5.1,7.3,9.2,11.8)
comp <- c(11,12,15,1,5,4,10,12,15,8)
inv <- c(294,232,149,600,567,571,512,347,212,439)
size_dist <- c(8.2,4.1,4.3,16.1,14.1,3.2,5.9,12.4,15.5,7.1)

shop <- data.frame(sales,ads,comp,inv,size_dist)

cat("\n\tShop DataFrame =\n")
shop

categorical <- function()
{
	png(file = "cat_info.png")
	plot(state_info$region)
}

numeric2 <- function()
{
	png(file = "num2_info.png")
	plot(state_info$area,state_info$population)
}

histogram <- function()
{
	png(file = "hist.png")
	hist(state_info$population, breaks = 10)
}

customize <- function()
{
	png(file = "cust.png")
	par(col.lab = "blue",col.main="darkblue",col.axis="darkgreen")
	plot(mercury$temprature, mercury$pressure,main="Mercury Behaviour")
}

multiple <- function()
{
	png(file = "mult.png")
	grid <- matrix(c(1,1,2,3), nrow = 2, byrow = TRUE)
	layout(grid)
	plot(shop$ads, shop$sales)
	plot(shop$comp, shop$sales)
	plot(shop$inv, shop$sales)
}

c="y"

repeat{

	cat("\nMenu")
	cat("\n\t1).Categorical Data")
	cat("\n\t2).*Numeric Data")
	cat("\n\t3).Histogram")
	cat("\n\t4).Coustomized Plot")
	cat("\n\t5).Muliple Plot\n\n")

	cat("\n\t\tEnter your choice =")
	ch=as.integer(readLines("stdin",1))

switch(ch,
	categorical(),
	numeric2(),
	histogram(),
	customize(),
	multiple()
)

cat("\n\tDo you want to continue y/Y ?=")
c=readLines("stdin",1)

if(c!="y"||c!="Y"){
	break
}
}



