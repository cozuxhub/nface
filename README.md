# NFACE

The purpose of this tool is to provide a quick response for multiple nmap questions (how many ports are open?, which versions are running? etc.) that we encounter in some CTFs.

# USAGE

First of all, we need to know the IP address of the target and where the scan output will be. After learning these, use the `python3 nface.py -t <target-ip-address> -o <output-destination>` command to start the tool. 
<br><br>Like `python3 nface.py -t 10.0.2.4 -o /tmp/nface_output.txt`
