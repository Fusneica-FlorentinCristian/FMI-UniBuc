.data

.text
	addi $t0, $zero, 30
	addi $t1, $zero, 7
	
	div $t0, $t1 #se poate imparti si numai cu doi registrii
	#catul va fi salvat in lo, iar restul in hi, asa ca va trebui sa le accesam:
	
	mflo $s0 #catul
	mfhi $s1 #restul
	
	#Print it!
	li $v0, 1
	add $a0, $zero, $s0 #poti schimba intre s0 si s1 ca sa dai print la cat sau la rest
	syscall