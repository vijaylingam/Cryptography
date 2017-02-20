vector <- []
w1 <- 'a'
w2 <- 'b'
w3 <- 'c'
w4 <- 'd'
p1 <- 0.1
p2 <- 0.2
p3 <- 0.3
p4 <- 0.4 # set to a = pmod5; where is the last significant digit of my roll number. In this case a = 9mod5 = 4.
n<- 10 #set the counter here
w <- 0 #counter variables
x <- 0
y <- 0
z <- 0
for(i in 1:n){
	u<-runif(1,0,1)
	if(u <= p1){
		print(w1)
		#vector <- c(vector, w1)
		#w = w + 1 # w stores the frequncy of occurence of 'a'
	}	
	if(p1 <= u && u <= p1+p2){
		print(w2)
		#vector <- c(vector, w2)
		#x = x + 1 # x stores the frequncy of occurence of 'b'
	}
	if(p1+p2<= u && u <= p1+p2+p3){
		print(w3)
		#vector <- c(vector, w3)
		#y = y + 1 # y stores the frequncy of occurence of 'c'
	}
	if(p1+p2+p3 <= u && u <= 1){ #because p1+p2+p3+p4 = 1
		print(w4)
		#vector <- c(vector, w4)
		#z = z + 1 # z stores the frequncy of occurence of 'd'
	}
	# uncomment the below statement if you want to see the output of the simulation
	#print(vector)
}
cat("frequency of a: ", w)
cat("frequency of b: ", x)
cat("frequency of c: ", y)
cat("frequency of d: ", z)