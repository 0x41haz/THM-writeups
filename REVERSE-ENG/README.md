<h3>crackme1</h3>
<h5> In this challenge you are given a simple binary..</h5>

```file crackme1.bin 
crackme1.bin: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=3864320789154e8960133afdf58ddf65f6f8273d, not stripped
```
<h5>after running the it ,you are asked to put password as input</h5>
```
./crackme1.bin 
enter password
qq
password is incorrect
```
<h5>Now lets just see the strings of the binary</h5>
```
strings crackme1.bin                                
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
