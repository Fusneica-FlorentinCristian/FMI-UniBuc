.data
	age: .word 19
.text
	li $v0, 1	#nu e text (string), asa ca prin 1 dam load immediately la un integer
	#programul se asteapta sa primeasca un word (in cazul asta un integer/valori intregi)
	lw $a0, age	#load word din argumentul ($a0) age
	syscall
