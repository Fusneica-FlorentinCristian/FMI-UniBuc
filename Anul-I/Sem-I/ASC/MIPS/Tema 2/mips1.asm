.data
    n: .word 5
    v: .word 3, 4, 5, 6, 7
    sp: .asciiz " "

.text
main:
    # argumentele v[], n pentru functia modifica
    subu $sp, 8
    # push v
    la $t0, v
    sw $t0, 0($sp)
    # push n
    lw $t0, n
    sw $t0, 4($sp)

    jal modifica

# print array init
    li $t0, 0 # contor=0
    li $t1, 0 # index=0
    lw $t2, n

print_array_loop:
    # while(contor < n)
    beq $t0, $t2, exit

    # put(v[index])
    lw $a0, v($t1)
    li $v0, 1
    syscall

    # put(' ')
    la $a0, sp
    li $v0, 4
    syscall

    addi $t1, 4 # index += 4
    addi $t0, 1 # contor += 1
    j print_array_loop

exit:
    addu $sp, 8
    li $v0, 10
    syscall

modifica:
    #adauga $fp la stiva
    subu $sp,$sp,4
    sw $fp,0($sp)
    addi $fp,$sp,4

    #adauga $ra la stiva
    subu $sp,$sp,4
    sw $ra,0($sp)

    #adauga $s0 la stiva
    subu $sp,$sp,4
    sw $s0,0($sp)

    #adauga $s1 la stiva
    subu $sp,$sp,4
    sw $s1,0($sp)

    #luam argumentele
    lw $s0,0($fp) # v
    lw $s1,4($fp) # n

    # if (n == 0) return;
    beqz $s1, modifica_exit

    # *v = suma_patrate(*v)
    subu $sp, 4
    lw $t0, 0($s0)
    sw $t0, 0($sp)
    jal suma_patrate
    addi $sp, 4
    sw $v0, 0($s0)

    addi $s0, 4  # v += 4
    addi $s1, -1 # n -= 1

    # argumentele pentru apel recursiv
    subu $sp, 8
    sw $s0, 0($sp) # push v
    sw $s1, 4($sp) # push n

    jal modifica
    addu $sp, 8

modifica_exit:
    lw $s1, -16($fp)
    lw $s0, -12($fp)
    lw $ra, -8($fp)
    lw $fp, -4($fp)
    addu $sp, 16
    jr $ra


suma_patrate:
    # push $fp
    subu $sp, 4
    sw $fp, 0($sp)
    addi $fp, $sp, 4

    # push {$ra, $s0}
    subu $sp, 8
    sw $ra, -8($fp)
    sw $s0, -12($fp)
    
    # get arg
    lw $s0, 0($fp) # int num
    subu $s0, 1    # num -= 1; 

    # if(num==1) return 1;
    ble $s0, 1, suma_patrate_ret_1 
    
    # apel recursiv
    # push num
    subu $sp, 4
    sw $s0, 0($sp)
    jal suma_patrate
    addu $sp, 4

    move $t0, $v0 # suma = suma_patrate(num);
    mul $s0, $s0, $s0 # num *= num;
    add $v0, $t0, $s0 # return num + suma;

    j suma_patrate_exit

suma_patrate_ret_1:
    li $v0, 1
suma_patrate_exit:
    lw $s0, -12($fp)
    lw $ra, -8($fp)
    lw $fp, -4($fp)
    addu $sp, 12
    jr $ra
