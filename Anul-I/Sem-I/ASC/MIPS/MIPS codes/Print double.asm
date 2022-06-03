.data
	myDouble: .double 7.202
	zeroDouble: .double 0.0	# cica zeroDouble se face ca sa ne putem folosi de $f12
.text
	#always use even registers for doubles ($f0,2,4,6,...), it's a special case
	ldc1 $f2, myDouble	#nu stiu de ce s-a ales %f2
	ldc1 $f0, zeroDouble	#sau aici %f0
	
	li $v0, 3		#3 e specific pt double, deci pregatim sistemul sa dea print la un double
	add.d $f12, $f2, $f0	#se adauga in %f12 $f2 si %f0 (f12=f0+f2)
	syscall
	
	#idk how doubles work :P