# Deployment
This challenge consists of several parts:
- C2 + redirector: used during setup & during challenge
- Windows victim PC: used during setup
- C2 beacon: used during setup
- DNS server: used during setup
- PCAP file: created during setup & shared with players

## C2 + redirector
This is all contained in the `src/Dockerfile`. Simply build & deploy. Be sure this host is accessible from the Windows victim PC. Additionally, ensure the IP used during setup (PCAP file generation) and during the challenge are identical.

## Windows victim PC
Is exactly what it sounds like. This can be any Windows host. Recommended is to run a VM with a clean install. Install Wireshark on it to create the PCAP dump later. Also copy the C2 beacon over to it.

## C2 beacon
The "malware" that runs on the victim. Located at `src/assets/sliver/GRUBBY_BOY.exe`. Simply copy it over to the victim and double click to start. It will report back to the C2 server hosted by Docker.

## DNS server
In order to make stuff more realistic, we also hosted a DNS server that resolves the attacker-controlled host `reddid.com`. The beacon connects to the attacker-controlled host.
The DNS server should be accessible by the Windows victim PC and obviously configured to be used by it. Setup for the DNS server is located in `src/dnsserver`.

## PCAP file
Requirements that must be met at this point:
- Windows victim is running
- C2 & DNS server are accessible by Windows victim host
- Windows victim has Wireshark installed
- Windows victim has C2 beacon on disk

To create the PCAP file:
1. start capturing network traffic with Wireshark
2. start the beacon
3. create some network traffic
    - browse the web
    - log in to the C2 server and interact with the beacon