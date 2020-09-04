# Installing and Using pygame, pygame zero in Ubuntu

When I try to run `pip3 install pygame` directly, I got error as below first:

```
$ pip3 install pygame
Collecting pygame
  Downloading pygame-1.9.6.tar.gz (3.2 MB)
     |████████████████████████████████| 3.2 MB 1.4 MB/s 
<font color="#CC0000">    ERROR: Command errored out with exit status 1:</font>
<font color="#CC0000">     command: /home/yasen/anaconda3/bin/python -c &apos;import sys, setuptools, tokenize; sys.argv[0] = &apos;&quot;&apos;&quot;&apos;/tmp/pip-install-wsumpanc/pygame/setup.py&apos;&quot;&apos;&quot;&apos;; __file__=&apos;&quot;&apos;&quot;&apos;/tmp/pip-install-wsumpanc/pygame/setup.py&apos;&quot;&apos;&quot;&apos;;f=getattr(tokenize, &apos;&quot;&apos;&quot;&apos;open&apos;&quot;&apos;&quot;&apos;, open)(__file__);code=f.read().replace(&apos;&quot;&apos;&quot;&apos;\r\n&apos;&quot;&apos;&quot;&apos;, &apos;&quot;&apos;&quot;&apos;\n&apos;&quot;&apos;&quot;&apos;);f.close();exec(compile(code, __file__, &apos;&quot;&apos;&quot;&apos;exec&apos;&quot;&apos;&quot;&apos;))&apos; egg_info --egg-base /tmp/pip-pip-egg-info-qx81zo80</font>
<font color="#CC0000">         cwd: /tmp/pip-install-wsumpanc/pygame/</font>
<font color="#CC0000">    Complete output (25 lines):</font>
<font color="#CC0000">    </font>
<font color="#CC0000">    </font>
<font color="#CC0000">    WARNING, No &quot;Setup&quot; File Exists, Running &quot;buildconfig/config.py&quot;</font>
<font color="#CC0000">    Using UNIX configuration...</font>
<font color="#CC0000">    </font>
<font color="#CC0000">    /bin/sh: 1: sdl-config: not found</font>
<font color="#CC0000">    /bin/sh: 1: sdl-config: not found</font>
<font color="#CC0000">    /bin/sh: 1: sdl-config: not found</font>
<font color="#CC0000">    Package freetype2 was not found in the pkg-config search path.</font>
<font color="#CC0000">    Perhaps you should add the directory containing `freetype2.pc&apos;</font>
<font color="#CC0000">    to the PKG_CONFIG_PATH environment variable</font>
<font color="#CC0000">    Package &apos;freetype2&apos;, required by &apos;virtual:world&apos;, not found</font>
<font color="#CC0000">    Package freetype2 was not found in the pkg-config search path.</font>
<font color="#CC0000">    Perhaps you should add the directory containing `freetype2.pc&apos;</font>
<font color="#CC0000">    to the PKG_CONFIG_PATH environment variable</font>
<font color="#CC0000">    Package &apos;freetype2&apos;, required by &apos;virtual:world&apos;, not found</font>
<font color="#CC0000">    Package freetype2 was not found in the pkg-config search path.</font>
<font color="#CC0000">    Perhaps you should add the directory containing `freetype2.pc&apos;</font>
<font color="#CC0000">    to the PKG_CONFIG_PATH environment variable</font>
<font color="#CC0000">    Package &apos;freetype2&apos;, required by &apos;virtual:world&apos;, not found</font>
<font color="#CC0000">    </font>
<font color="#CC0000">    Hunting dependencies...</font>
<font color="#CC0000">    WARNING: &quot;sdl-config&quot; failed!</font>
<font color="#CC0000">    WARNING: &quot;pkg-config freetype2&quot; failed!</font>
<font color="#CC0000">    Unable to run &quot;sdl-config&quot;. Please make sure a development version of SDL is installed.</font>
<font color="#CC0000">    ----------------------------------------</font>
<font color="#CC0000">ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.</font>
</pre>
```



Check from URL: https://stackoverflow.com/questions/19579528/pygame-installation-sdl-config-command-not-found

Got the [EakzIT](https://stackoverflow.com/users/12463811/eakzit)'s great knowledge, running below dependencies installation just in one line:

```
$ sudo apt-get install python-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev python-numpy subversion libportmidi-dev ffmpeg libswscale-dev libavformat-dev libavcodec-dev
```

After that, re-run the command, it's working:

```
$ pip3 install pygame
Collecting pygame
  Using cached pygame-1.9.6.tar.gz (3.2 MB)
Building wheels for collected packages: pygame
  Building wheel for pygame (setup.py) ... done
  Created wheel for pygame: filename=pygame-1.9.6-cp38-cp38-linux_x86_64.whl size=3932848 sha256=dcfcb61cbbd5cb4d156b501e5c46b10540f7d41223cf45d59646de2b05c07bcb
  Stored in directory: /home/yasen/.cache/pip/wheels/5c/3a/34/864e618a7e57b5df7cc5f1d1338aa43e7d566a4749a540c9b7
Successfully built pygame
Installing collected packages: pygame
Successfully installed pygame-1.9.6

```

Thanks a lot EakzIT.

---

Furthermore, install pygame_zero:

```
$ pip3 install pgzero
Collecting pgzero
  Downloading pgzero-1.2-py3-none-any.whl (69 kB)
     |████████████████████████████████| 69 kB 1.4 MB/s 
Requirement already satisfied: pygame<2.0,>=1.9.2 in ./anaconda3/lib/python3.8/site-packages (from pgzero) (1.9.6)
Requirement already satisfied: numpy in ./anaconda3/lib/python3.8/site-packages (from pgzero) (1.18.5)
Installing collected packages: pgzero
Successfully installed pgzero-1.2

```



