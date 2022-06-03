#Introduction to functions (procedures/proceduri) 2

.data

.text
	main:
		addi $a0,$zero,100
		addi $a1,$zero,50
		
		jal addNumbers
		
		#Diplay the sum
		li $v0,1
		add $a0,$zero,$v1 #sau addi $a0,$v1,0
		syscall 
		
	#Tell the system that the program is done.
	li $v0, 10
	syscall
	
	addNumbers:
		add $v1, $a0,$a1
		
		jr $ra #jump register to ra (return adress) // se reintoarce de unde a fost apelat