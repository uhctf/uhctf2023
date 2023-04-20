# DNS server
To make the pcap look ever so slightly more realistic, we decided to do the `reddid.com` resolution on DNS level instead of placing it in the hosts file.

## Install
### Server
On a PC/VM in the victim network do the following:
- download project: https://github.com/yizheh/dns_server
- pip install requirements
- tweak script to run on the proper port, interface, etc.
- configure a config file to specify resolution for `reddid.com`

### Victim
- flush DNS cache: `ipconfig /flushdns`
- configure windows (set static DNS IP in network settings)