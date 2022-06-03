.data
	myMessage: .asciiz "Hello World \n"

.text
	li $v0, 4		#load immediately (li) a print command ($v0, 4)
	la $a0, myMessage	#load adress of myMessage (into $a0)
	syscall			#do it! do it, system!
	