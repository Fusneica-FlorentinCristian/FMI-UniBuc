.data
	v: .word 1, 2, 3, 4
	n: .word 4
	a: .word 2
	c: .word 3
	t: .word 3 
	
.text
	main:
		
		#vreau sa fac un for pentru fiecare element din v
		
		#Inchidere main
		exit
		
	f:
		bge $s0,$s1, exit #vreau ca $s0=v[i], iar $s1=c, si daca s0>=s1, sa iasa din program
		
		
		
		jr $ra
	exit:
		li $v0,10
		syscall
