.data
	PI: .float 3.14
.text
	li $v0, 2	# 2 provine de la float, asa ca dam load immediately la un float
	# floats are different than integers, floats are going to coprocessor 1(Coproc 1)
	lwc1 $f12, PI	# nu stiu de ce, dar numai cu $f12 merge o.O
	syscall