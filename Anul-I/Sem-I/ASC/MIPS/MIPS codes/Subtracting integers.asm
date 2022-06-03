.data
	number1: .word 20
	number2: .word 17
.text
	lw $s0, number1		#s0=5
	lw $s1, number2($zero)	#s1=10
	sub $t0, $s0, $s1 #t2 = s0 - s1 // t2 = 5 - 10
	
	li $v0, 1
	#move $a0,$t0
	add $a0, $zero, $t0
	syscall