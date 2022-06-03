.data
	newLine: .asciiz "\n"
.text
	main:
		addi $s0,$zero,10 #s0=10
		
		jal increaseMyRegister
		
		#Print new line
		li $v0, 4
		la $a0, newLine
		syscall
		
		#Print the value
		li $v0, 1
		move $a0,$s0
		syscall
		
	#This lie is going to signal end of program
	li $v0, 10
	syscall
	
	increaseMyRegister:
		addi $sp, $sp, -4
		sw $s0,0($sp)
		
		addi $s0, $s0, 30
		
		#Print new value in function
		li $v0, 1
		move $a0, $s0
		syscall
		
		lw $s0, 0($sp)
		addi $sp, $sp, 4
		
		jr $ra