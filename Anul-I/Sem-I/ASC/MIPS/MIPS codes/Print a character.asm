.data
	myCharacter: .byte 'm'	#nu merge cu "m"!!
.text
	li $v0, 4
	la $a0, myCharacter
	syscall