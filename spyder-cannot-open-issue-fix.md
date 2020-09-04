# Usage Tips in Python withiu Ubuntu

My Ubuntu info:

```
$ uname -a
Linux yasen-Latitude-E7240 5.4.0-46-generic #50-Ubuntu SMP Fri Aug 28 15:33:36 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
```

## Spyder error handling

Installed Spyder3 via APT, `sudo apt install spyder3`, when running, get following error:

```
$ spyder3
Attribute Qt::AA_UseSoftwareOpenGL must be set before QCoreApplication is created.
Segmentation fault (core dumped)
```

Cannot fix after uninstall then install

Below method fixed issue:

```
$ pip3 install --upgrade spyder
Collecting spyder
  Downloading spyder-4.1.5-py3-none-any.whl (10.7 MB)
     |████████████████████████████████| 10.7 MB 5.7 MB/s 
Collecting watchdog
  Downloading watchdog-0.10.3.tar.gz (94 kB)
     |████████████████████████████████| 94 kB 2.4 MB/s 
Requirement already satisfied, skipping upgrade: chardet>=2.0.0 in /usr/lib/python3/dist-packages (from spyder) (3.0.4)
Collecting pyqtwebengine<5.13; python_version >= "3"
  Downloading PyQtWebEngine-5.12.1-5.12.9-cp35.cp36.cp37.cp38-abi3-manylinux1_x86_64.whl (60.1 MB)
     |████████████████████████████████| 60.1 MB 16.5 MB/s 
Requirement already satisfied, skipping upgrade: psutil>=5.3 in /usr/lib/python3/dist-packages (from spyder) (5.5.1)
Requirement already satisfied, skipping upgrade: pickleshare>=0.4 in /usr/lib/python3/dist-packages (from spyder) (0.7.5)
Requirement already satisfied, skipping upgrade: numpydoc>=0.6.0 in /usr/lib/python3/dist-packages (from spyder) (0.7.0)
Collecting parso==0.7.0
  Downloading parso-0.7.0-py2.py3-none-any.whl (100 kB)
     |████████████████████████████████| 100 kB 7.6 MB/s 
Requirement already satisfied, skipping upgrade: cloudpickle>=0.5.0 in /usr/lib/python3/dist-packages (from spyder) (1.3.0)
Collecting spyder-kernels<1.10.0,>=1.9.4
  Downloading spyder_kernels-1.9.4-py2.py3-none-any.whl (60 kB)
     |████████████████████████████████| 60 kB 7.3 MB/s 
Requirement already satisfied, skipping upgrade: qtconsole>=4.6.0 in /usr/lib/python3/dist-packages (from spyder) (4.6.0)
Collecting qtawesome>=0.5.7
  Downloading QtAwesome-0.7.2-py2.py3-none-any.whl (832 kB)
     |████████████████████████████████| 832 kB 18.7 MB/s 
Requirement already satisfied, skipping upgrade: qtpy>=1.5.0 in /usr/lib/python3/dist-packages (from spyder) (1.9.0)
Requirement already satisfied, skipping upgrade: pyzmq>=17 in /usr/lib/python3/dist-packages (from spyder) (18.1.1)
Collecting python-language-server[all]<1.0.0,>=0.34.0
  Downloading python_language_server-0.34.1-py3-none-any.whl (49 kB)
     |████████████████████████████████| 49 kB 6.7 MB/s 
Requirement already satisfied, skipping upgrade: pyxdg>=0.26; platform_system == "Linux" in /usr/lib/python3/dist-packages (from spyder) (0.26)
Requirement already satisfied, skipping upgrade: ipython>=4.0 in /usr/lib/python3/dist-packages (from spyder) (7.13.0)
Requirement already satisfied, skipping upgrade: sphinx>=0.6.6 in /usr/lib/python3/dist-packages (from spyder) (1.8.5)
Requirement already satisfied, skipping upgrade: nbconvert>=4.0 in /usr/lib/python3/dist-packages (from spyder) (5.6.1)
Collecting jedi==0.17.1
  Downloading jedi-0.17.1-py2.py3-none-any.whl (1.4 MB)
     |████████████████████████████████| 1.4 MB 16.6 MB/s 
Collecting diff-match-patch>=20181111
  Downloading diff_match_patch-20200713-py3-none-any.whl (61 kB)
     |████████████████████████████████| 61 kB 249 kB/s 
Collecting pyqt5<5.13; python_version >= "3"
  Downloading PyQt5-5.12.3-5.12.9-cp35.cp36.cp37.cp38-abi3-manylinux1_x86_64.whl (62.3 MB)
     |████████████████████████████████| 62.3 MB 7.3 MB/s 
Requirement already satisfied, skipping upgrade: keyring; sys_platform != "linux2" in /usr/lib/python3/dist-packages (from spyder) (18.0.1)
Requirement already satisfied, skipping upgrade: pylint>=1.0 in /usr/lib/python3/dist-packages (from spyder) (2.4.4)
Requirement already satisfied, skipping upgrade: pexpect>=4.4.0 in /usr/lib/python3/dist-packages (from spyder) (4.6.0)
Collecting intervaltree
  Downloading intervaltree-3.1.0.tar.gz (32 kB)
Requirement already satisfied, skipping upgrade: pygments>=2.0 in /usr/lib/python3/dist-packages (from spyder) (2.3.1)
Collecting atomicwrites>=1.2.0
  Downloading atomicwrites-1.4.0-py2.py3-none-any.whl (6.8 kB)
Collecting qdarkstyle>=2.8
  Downloading QDarkStyle-2.8.1-py2.py3-none-any.whl (217 kB)
     |████████████████████████████████| 217 kB 7.7 MB/s 
Collecting pathtools>=0.1.1
  Downloading pathtools-0.1.2.tar.gz (11 kB)
Requirement already satisfied, skipping upgrade: jupyter-client>=5.3.4 in /usr/lib/python3/dist-packages (from spyder-kernels<1.10.0,>=1.9.4->spyder) (6.1.2)
Collecting wurlitzer>=1.0.3; platform_system != "Windows"
  Downloading wurlitzer-2.0.1-py2.py3-none-any.whl (6.1 kB)
Requirement already satisfied, skipping upgrade: ipykernel in /usr/lib/python3/dist-packages (from spyder-kernels<1.10.0,>=1.9.4->spyder) (5.2.0)
Requirement already satisfied, skipping upgrade: six in /usr/lib/python3/dist-packages (from qtawesome>=0.5.7->spyder) (1.14.0)
Collecting pluggy
  Downloading pluggy-0.13.1-py2.py3-none-any.whl (18 kB)
Collecting ujson<=1.35; platform_system != "Windows"
  Downloading ujson-1.35.tar.gz (192 kB)
     |████████████████████████████████| 192 kB 26.7 MB/s 
Collecting python-jsonrpc-server>=0.3.2
  Downloading python_jsonrpc_server-0.3.4-py3-none-any.whl (9.0 kB)
Requirement already satisfied, skipping upgrade: mccabe<0.7.0,>=0.6.0; extra == "all" in /usr/lib/python3/dist-packages (from python-language-server[all]<1.0.0,>=0.34.0->spyder) (0.6.1)
Collecting pyflakes<2.3.0,>=2.2.0; extra == "all"
  Downloading pyflakes-2.2.0-py2.py3-none-any.whl (66 kB)
     |████████████████████████████████| 66 kB 5.1 MB/s 
Collecting pycodestyle<2.7.0,>=2.6.0; extra == "all"
  Downloading pycodestyle-2.6.0-py2.py3-none-any.whl (41 kB)
     |████████████████████████████████| 41 kB 373 kB/s 
Collecting flake8>=3.8.0; extra == "all"
  Downloading flake8-3.8.3-py2.py3-none-any.whl (72 kB)
     |████████████████████████████████| 72 kB 1.7 MB/s 
Collecting yapf; extra == "all"
  Downloading yapf-0.30.0-py2.py3-none-any.whl (190 kB)
     |████████████████████████████████| 190 kB 8.9 MB/s 
Collecting pydocstyle>=2.0.0; extra == "all"
  Downloading pydocstyle-5.1.1-py3-none-any.whl (35 kB)
Requirement already satisfied, skipping upgrade: rope>=0.10.5; extra == "all" in /usr/lib/python3/dist-packages (from python-language-server[all]<1.0.0,>=0.34.0->spyder) (0.10.5)
Collecting autopep8; extra == "all"
  Downloading autopep8-1.5.4.tar.gz (121 kB)
     |████████████████████████████████| 121 kB 17.5 MB/s 
Collecting PyQt5_sip<13,>=4.19.14
  Downloading PyQt5_sip-12.8.1-cp38-cp38-manylinux1_x86_64.whl (293 kB)
     |████████████████████████████████| 293 kB 18.4 MB/s 
Requirement already satisfied, skipping upgrade: secretstorage in /usr/lib/python3/dist-packages (from keyring; sys_platform != "linux2"->spyder) (2.3.1)
Collecting sortedcontainers<3.0,>=2.0
  Downloading sortedcontainers-2.2.2-py2.py3-none-any.whl (29 kB)
Collecting helpdev>=0.6.10
  Downloading helpdev-0.7.1-py3-none-any.whl (14 kB)
Collecting snowballstemmer
  Downloading snowballstemmer-2.0.0-py2.py3-none-any.whl (97 kB)
     |████████████████████████████████| 97 kB 1.9 MB/s 
Collecting toml
  Downloading toml-0.10.1-py2.py3-none-any.whl (19 kB)
Building wheels for collected packages: watchdog, intervaltree, pathtools, ujson, autopep8
  Building wheel for watchdog (setup.py) ... done
  Created wheel for watchdog: filename=watchdog-0.10.3-py3-none-any.whl size=73871 sha256=778fc6974e23c656636a1cef523418eeebbdc3cd49aedf4bb659849969aff77a
  Stored in directory: /home/yasen/.cache/pip/wheels/f8/39/45/b80612a24e42d9de0bd5eaf69eaf953edc25e1a9809d3d989f
  Building wheel for intervaltree (setup.py) ... done
  Created wheel for intervaltree: filename=intervaltree-3.1.0-py2.py3-none-any.whl size=26102 sha256=daedd779485fe2acd9b57c1146d75b98e491603b5caa43406296ef458d3f0bf4
  Stored in directory: /home/yasen/.cache/pip/wheels/45/23/de/5789a92962483fd33cb06674792b9697c1b3766d7c7742830e
  Building wheel for pathtools (setup.py) ... done
  Created wheel for pathtools: filename=pathtools-0.1.2-py3-none-any.whl size=8784 sha256=637859c42a5cc288aad99562e5fb329dd078837e4ac55ee3e17e0a57fbda10c1
  Stored in directory: /home/yasen/.cache/pip/wheels/4c/8e/7e/72fbc243e1aeecae64a96875432e70d4e92f3d2d18123be004
  Building wheel for ujson (setup.py) ... done
  Created wheel for ujson: filename=ujson-1.35-cp38-cp38-linux_x86_64.whl size=81805 sha256=622791ef083e5e5c138fa8953b43582dd0ac5fa70c1f4420640c9decb9faaa34
  Stored in directory: /home/yasen/.cache/pip/wheels/1b/92/b2/df9c56805bf5ebf331fb1ad733d0d4fd32ee3405fd8d88ed09
  Building wheel for autopep8 (setup.py) ... done
  Created wheel for autopep8: filename=autopep8-1.5.4-py2.py3-none-any.whl size=45286 sha256=a3fe29e964fa3076d429849f18f0da79c51c09866c8ea3cbb42ce131df598eb2
  Stored in directory: /home/yasen/.cache/pip/wheels/5f/b4/93/a30fa45720240e1106155083bac98146542dd614e1e6ce12da
Successfully built watchdog intervaltree pathtools ujson autopep8
Installing collected packages: pathtools, watchdog, PyQt5-sip, pyqt5, pyqtwebengine, parso, wurlitzer, spyder-kernels, qtawesome, pluggy, ujson, python-jsonrpc-server, jedi, pyflakes, pycodestyle, flake8, yapf, snowballstemmer, pydocstyle, toml, autopep8, python-language-server, diff-match-patch, sortedcontainers, intervaltree, atomicwrites, helpdev, qdarkstyle, spyder
Successfully installed PyQt5-sip-12.8.1 atomicwrites-1.4.0 autopep8-1.5.4 diff-match-patch-20200713 flake8-3.8.3 helpdev-0.7.1 intervaltree-3.1.0 jedi-0.17.1 parso-0.7.0 pathtools-0.1.2 pluggy-0.13.1 pycodestyle-2.6.0 pydocstyle-5.1.1 pyflakes-2.2.0 pyqt5-5.12.3 pyqtwebengine-5.12.1 python-jsonrpc-server-0.3.4 python-language-server-0.34.1 qdarkstyle-2.8.1 qtawesome-0.7.2 snowballstemmer-2.0.0 sortedcontainers-2.2.2 spyder-4.1.5 spyder-kernels-1.9.4 toml-0.10.1 ujson-1.35 watchdog-0.10.3 wurlitzer-2.0.1 yapf-0.30.0
```
