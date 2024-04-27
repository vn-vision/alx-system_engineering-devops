# Attack is the Best Defense

Security is a vast topic, and network security is an important part of it. A lot of very sensitive information goes over networks that are used by many people, and some people might have bad intentions. Traffic going through a network can be intercepted by a malicious machine pretending to be another network device. Once the traffic is redirected to the malicious machine, the hacker can keep a copy of it and analyze it for potential interesting information. It is important to note that the traffic must then be forwarded to the actual device it was supposed to go (so that users and the system keep going as if nothing happened).

Any information that is not encrypted and sniffed by an attacker can be seen by the attacker - that could be your email password or credit card information. While today’s network security is much stronger than it used to be, there are still some legacy systems that are using unencrypted communication means. A popular one is telnet.

In this project, we will not go over ARP spoofing, but we’ll start by sniffing unencrypted traffic and getting information out of it.

Your mission is to execute user_authenticating_into_server locally on your machine and, using tcpdump, sniff the network to find my password. Once you find it, paste the password in your answer file. This script will not work on a Docker container or Mac OS, use your Ubuntu vagrant machine or any other Linux machine.

You can download the script `user_authenticating_into_server`.
change the execution permissions if you have not: `chmod 755 user_authenticating_into_server`

# DISCLAIMER:
you will probably see Authentication failed: Bad username / password in the tcpdump trace. It’s normal, we deleted the user to our Sendgrid account. You can’t verify the password found via Sendgrid, only the correction system can!

1. Run tcpdump indicating the interface, host, port and include the necessary flags
    - 'tcpdump -i wlan0 host <your_host_ip> and port 587 -w <file_name_to_save_output>`
2. While tcpdump is running execute the file `./user_authenticating_into_server`
3. Once you capture the packets, run `tcpdump -r <name_of_your_output_file> -A` to be able to read the ASCII format
4. Go through the captured packets and decrypt the Authentication packets: Username and Password
