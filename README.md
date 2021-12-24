# Log-4-JAM - Log 4 Just Another Mess
Log4j JNDI inj. vuln scanner

## About -
This is a reliable scanner if you are looking to test your applications that could be vulnerable to Log4J JNDI Injection Vulnerability.

## Requirements 
```bash
pip3 install requests_toolbelt
```
## Usage  
```bash
# make sure target list has http/https prepended to it.
# or grab list of endpoints from wayback and pass the list in the argument . 
python3 l4jam.py targetlist.txt collab.net 

```
## Updates  / features
```bash
1. loads the target lists
2. added more RSPs like dns, rmi, etc
3. added more waf bypass payloads.
4. added more headers
5. Prints out request and response of each target.
```

## warning!!

its all on you what you do with this script as this is meant for pentest/Red-Team and bugbounty stuff.
other than that if you use it for malicious purpose like extortion and shit i am not responsible for the mess.


### !!! Feedback's are welcome !!!

## Contact 
If you want to get your product tested if its vuln/exploitable to log4j jndi injection ,
Then write me email - dorkerdevil_log4jmess@protonmail.com
