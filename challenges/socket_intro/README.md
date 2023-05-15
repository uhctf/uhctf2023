# Warmup #3
* Category: **pwn**

* Flag Format: **uhctf{...}**

* Flags: <details><summary>CLICK TO SHOW</summary><ul><ul>
<li>static: <code>uhctf{4-50ck3t-15-4-d00r-ad3a21}</code></li>
</ul></ul></details>

* Connection Info: <ip>:8000

* Requirements: netcat

* Credits:
    * mihály

* Hints: <ul><ul>
</ul></ul>

## Description
Some computer programs must be available over a network. The address where we can find the program consists of 2 parts:
- an IP address: the address of the computer
- a port number: the address of the application

To send raw data to a program over a network, connect to it as follows: `nc <ip> <port>` (read `nc` as `netcat`).

Tell the program on `<TODO_IP>:<TODO_PORT>` to "open sesame".