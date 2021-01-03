# Install pygame in Python3 / Ubuntu

When I run `pip3 install pygame` directly, I got following error:



```
pip3 install pygame
Collecting pygame
  Downloading pygame-1.9.6.tar.gz (3.2 MB)
     |████████████████████████████████| 3.2 MB 1.4 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /home/yasen/anaconda3/bin/python -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-wsumpanc/pygame/setup.py'"'"'; __file__='"'"'/tmp/pip-install-wsumpanc/pygame/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /tmp/pip-pip-egg-info-qx81zo80
         cwd: /tmp/pip-install-wsumpanc/pygame/
    Complete output (25 lines):
    
    
    WARNING, No "Setup" File Exists, Running "buildconfig/config.py"
    Using UNIX configuration...
    
    /bin/sh: 1: sdl-config: not found
    /bin/sh: 1: sdl-config: not found
    /bin/sh: 1: sdl-config: not found
    Package freetype2 was not found in the pkg-config search path.
    Perhaps you should add the directory containing `freetype2.pc'
    to the PKG_CONFIG_PATH environment variable
    Package 'freetype2', required by 'virtual:world', not found
    Package freetype2 was not found in the pkg-config search path.
    Perhaps you should add the directory containing `freetype2.pc'
    to the PKG_CONFIG_PATH environment variable
    Package 'freetype2', required by 'virtual:world', not found
    Package freetype2 was not found in the pkg-config search path.
    Perhaps you should add the directory containing `freetype2.pc'
    to the PKG_CONFIG_PATH environment variable
    Package 'freetype2', required by 'virtual:world', not found
    
    Hunting dependencies...
    WARNING: "sdl-config" failed!
    WARNING: "pkg-config freetype2" failed!
    Unable to run "sdl-config". Please make sure a development version of SDL is installed.
    ----------------------------------------
ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.

```



