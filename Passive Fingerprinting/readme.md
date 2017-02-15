#Perform Passive OS Fingerprinting

----------------
| REQUIREMENTS |
----------------

1. Python 3.X
2. Scapy-python-3 module

--------------
| MOTIVATION |
--------------

1. Understand how scapy can be used to interpret pcap files.
2. Explore and experiment different functions in Scapy.
3. Find out the OS from pcap packet content using different approach as given below.

-----------------------
| HIGH LEVEL APPROACH |
-----------------------

There are some signs to find the OS, but none of them are 100% reliable.
  1. Look for typical values for MSS and Windows size in TCP connections
  2. Look for typical RTT values:	http://www.netresec.com/?page=Blog&month=2011-11&post=Passive-OS-Fingerprinting
  3. Look for typical protocols of a certain OS (netbios, etc.)
  4. Look for sign of certain client software (Browser: User-Agent, Banner, etc.)
  5. Look for the TCP source ports used. There are difference of those ranges between different OSes
  6. Look for the IP ID and how it changes. There are difference of ID between different OSes
	
---------------------------------
| OUR APPROACH FOR OS DETECTION |
---------------------------------

1. Extract GET/POST Request.
2. Look for User-Agent string in HTTP Headers
3. In User-Agent - find OS
4. For malicious packets monitor HTTP Status Code - 302 - Redirection
5. Analyze hexdump to find signatures related to metasploit etc. For example metasploit = 6D 65 74 61 73 70 6C 6F 69 74
6. Analyze unique strings in hexdump to find OS, services etc.
7. Identify other network devices like firewalls, switches, router etc.
