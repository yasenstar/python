If there's no tkinter module, you will have following error:

```python
[Running] /usr/bin/env python3 "..."
Traceback (most recent call last):
  File "...", line 5, in <module>
    from tkinter import Label, mainloop
ModuleNotFoundError: No module named 'tkinter'
```

# Install tkinter in python3

It was told that tkinter is now built in Python3, but seems not true, below still need to install that first.


```
$ sudo apt install python3-tk
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  blt libtk8.6 tk8.6-blt2.5
Suggested packages:
  blt-demo tk8.6 tix python3-tk-dbg
The following NEW packages will be installed:
  blt libtk8.6 python3-tk tk8.6-blt2.5
0 upgraded, 4 newly installed, 0 to remove and 0 not upgraded.
Need to get 1,396 kB of archives.
After this operation, 5,181 kB of additional disk space will be used.
Do you want to continue? [Y/n] 
Get:1 http://ca.archive.ubuntu.com/ubuntu groovy/main amd64 libtk8.6 amd64 8.6.10-1 [714 kB]
Get:2 http://ca.archive.ubuntu.com/ubuntu groovy/main amd64 tk8.6-blt2.5 amd64 2.5.3+dfsg-4 [572 kB]
Get:3 http://ca.archive.ubuntu.com/ubuntu groovy/main amd64 blt amd64 2.5.3+dfsg-4 [4,944 B]
Get:4 http://ca.archive.ubuntu.com/ubuntu groovy/main amd64 python3-tk amd64 3.8.6-1 [106 kB]
Fetched 1,396 kB in 1s (1,257 kB/s)  
Selecting previously unselected package libtk8.6:amd64.
(Reading database ... 290937 files and directories currently insta
lled.)
Preparing to unpack .../libtk8.6_8.6.10-1_amd64.deb ...
Unpacking libtk8.6:amd64 (8.6.10-1) ...
Selecting previously unselected package tk8.6-blt2.5.
Preparing to unpack .../tk8.6-blt2.5_2.5.3+dfsg-4_amd64.deb ...
Unpacking tk8.6-blt2.5 (2.5.3+dfsg-4) ...
Selecting previously unselected package blt.
Preparing to unpack .../blt_2.5.3+dfsg-4_amd64.deb ...
Unpacking blt (2.5.3+dfsg-4) ...
Selecting previously unselected package python3-tk:amd64.
Preparing to unpack .../python3-tk_3.8.6-1_amd64.deb ...
Unpacking python3-tk:amd64 (3.8.6-1) ...
Setting up libtk8.6:amd64 (8.6.10-1) ...
Setting up tk8.6-blt2.5 (2.5.3+dfsg-4) ...
Setting up blt (2.5.3+dfsg-4) ...
Setting up python3-tk:amd64 (3.8.6-1) ...
Processing triggers for libc-bin (2.32-0ubuntu3) ...
```

After that, using below command to verify `tkinter`:

```
$ python -m tkinter
```

You will be able to see one sample window
