.data

.text
	addi $t0,$zero,20000
	addi $t1,$zero,300
	
	mult $t0,$t1
	
	mflo $s0	#move from lo (unde lo este un registru) // s0=lo
	
	# Display the product
	li $v0, 1
	add $a0,$zero,$s0
	syscall