#Introduction to functions (procedures/proceduri)

.data
	message: .asciiz "Hi, everybody.\nMy name is Florin.\n"
.text
	main:
		jal displayMessage #jump and link the procedure
		
		#Codul nu se sfarseste la apelarea procedurii, se poate continua:
		
		addi $s0,$zero,5
		
		#Print 5
		li $v0, 1
		add $a0,$zero,$s0
		syscall
		
	#Tell the system that the program is done.
	li $v0, 10
	syscall
	
	displayMessage:
		li $v0, 4
		la $a0, message
		syscall
		
		jr $ra #jump register to ra (return adress) // se reintoarce de unde a fost apelat