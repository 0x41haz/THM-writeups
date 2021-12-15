<h2>crackme1</h2>
<h5> In this challenge you are given a simple binary..</h5>

```file crackme1.bin 
crackme1.bin: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=3864320789154e8960133afdf58ddf65f6f8273d, not stripped
```
<h5>after running  it ,you are asked to put password as input</h5>

```./crackme1.bin 
enter password
qq
password is incorrect
```
<h5>Now lets just see the strings of the binary</h5>

```strings crackme1.bin                                
/lib64/ld-linux-x86-64.so.2
libc.so.6
__isoc99_scanf
puts
__stack_chk_fail
__cxa_finalize
strcmp
__libc_start_main
GLIBC_2.7
GLIBC_2.4
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
=y	 
=9	 
52	 
AWAVI
AUATL
[]A\A]A^A_
enter password
password is correct
password is incorrect
hax0r
;*3$"
GCC: (Ubuntu 7.3.0-27ubuntu1~18.04) 7.3.0
crtstuff.c
deregister_tm_clones

__do_global_dtors_aux
```

<h5>Here you can see a word hax0r.lets try it as password</h5>

```./crackme1.bin      
enter password
hax0r
password is correct

```
<h5>BOOM !! its correct</h5>

--------------------------------------------------------------------------------------
<h2>crackme2</h2>
<h5> Now you are given a binary to do more analysis than the crackme1 . First run the binary </h5>
```
./crackme2.bin 
enter your password
llllll
password is incorrect
```
<h5> As the previous one you are asked to input password . after looking at the strings we have not anything yet</h5>
<h5>Lets open it on gdb and disassemble the main function first</h5>
```Dump of assembler code for function main:
   0x000000000000071a <+0>:	push   rbp
   0x000000000000071b <+1>:	mov    rbp,rsp
   0x000000000000071e <+4>:	sub    rsp,0x10
   0x0000000000000722 <+8>:	mov    rax,QWORD PTR fs:0x28
   0x000000000000072b <+17>:	mov    QWORD PTR [rbp-0x8],rax
   0x000000000000072f <+21>:	xor    eax,eax
   0x0000000000000731 <+23>:	lea    rdi,[rip+0xec]        # 0x824
   0x0000000000000738 <+30>:	call   0x5d0 <puts@plt>
   0x000000000000073d <+35>:	lea    rax,[rbp-0xc]
   0x0000000000000741 <+39>:	mov    rsi,rax
   0x0000000000000744 <+42>:	lea    rdi,[rip+0xed]        # 0x838
   0x000000000000074b <+49>:	mov    eax,0x0
   0x0000000000000750 <+54>:	call   0x5f0 <__isoc99_scanf@plt>
   0x0000000000000755 <+59>:	mov    eax,DWORD PTR [rbp-0xc]
   0x0000000000000758 <+62>:	cmp    eax,0x137c
   0x000000000000075d <+67>:	jne    0x76d <main+83>
   0x000000000000075f <+69>:	lea    rdi,[rip+0xd5]        # 0x83b
   0x0000000000000766 <+76>:	call   0x5d0 <puts@plt>
   0x000000000000076b <+81>:	jmp    0x779 <main+95>
   0x000000000000076d <+83>:	lea    rdi,[rip+0xd9]        # 0x84d
   0x0000000000000774 <+90>:	call   0x5d0 <puts@plt>
   0x0000000000000779 <+95>:	mov    eax,0x0
   0x000000000000077e <+100>:	mov    rdx,QWORD PTR [rbp-0x8]
   0x0000000000000782 <+104>:	xor    rdx,QWORD PTR fs:0x28
   0x000000000000078b <+113>:	je     0x792 <main+120>
   0x000000000000078d <+115>:	call   0x5e0 <__stack_chk_fail@plt>
   0x0000000000000792 <+120>:	leave  
   0x0000000000000793 <+121>:	ret    
End of assembler dump.
```
<h5> at the line number 15th we can see that 0x137c is compared to our input . lets input it on password field</h5>
```
./crackme2.bin
enter your password
0x137c
password is incorrect
```
<h5>oops! its incorrect .lets convert it ot decimal </h5>
```
>>> hex ='0x137c'
>>> deci=int(hex, 16)
>>> print(deci)
4988
```
<h5> it's 4988 . try it and we get as valid password </h5>
```
./crackme2.bin 
enter your password
4988
password is valid
```









