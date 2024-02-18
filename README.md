# NFACE

The purpose of this tool is to provide a quick response for multiple nmap questions (how many ports are open?, which versions are running? etc.) that we encounter in some CTFs.

# USAGE
First, let's download it to our Linux terminal: `git clone https://github.com/cozuxhub/nface.git` <br>
Go to the directory where you installed the folder and enter the folder. <br> 
Then, need to know the IP address of the target and where the scan output will be. After learning these, use the `python3 nface.py -t <target-ip-address> -o <output-destination>` command to start the tool. 
<br><br>Like this:
```
python3 nface.py -t 10.0.2.4 -o /tmp/nface_output.txt
```
<br><br>
The user inputs which scan wants to perform:

![1](https://github.com/cozuxhub/nface/assets/152704509/9659af0d-5c21-4eda-8533-8809520c0273)<br><br>

And the scan starts:

![2](https://github.com/cozuxhub/nface/assets/152704509/78d99604-4348-4396-ae63-ec63e914c3c1)<br><br>

> Refactoring has been done with artificial intelligence!


