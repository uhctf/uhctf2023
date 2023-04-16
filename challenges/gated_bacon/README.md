# Gated Bacon
* Category: **Forensics**

* Flag Format: **uhctf{...}**

* Flags: <details><summary>CLICK TO SHOW</summary><ul><ul>
<li>static: <code>uhctf{r3d1r3c7-7h15-y0u-f1l7hy-c45u41-84234a}</code></li>
</ul></ul></details>

* Connection Info: <ip>:80 (IP to be discovered, **don't share it**)

* Requirements: Wireshark

* Credits:
    * mihály

* Hints: <ul><ul>
<li><details>
    <summary><strong>20%</strong>: Finding the flag on the server</summary>
    Have you found the malicious server but can't access the flag? The C2 is protected using a redirector. It filters traffic that does not adhere to specific requirements. Try determining what this filter is by analysing the C2 beacon traffic.
</details></li>
</ul></ul>

## Description
A manager of DeliBacon Inc. got hacked. Their computer is infected and their passwords were stolen. As professional analysts we got called in to determine how the malware is getting its instructions. If we know the Command and Control server, we can call the police to take it down. This will not only help DeliBacon, but also prevent all other current and future victims from having their stuff stolen.

One of our technicians made a small network dump of the infected machine. Can you analyse it to figure out the server that is sending the malware instructions?

The flag can be found in the `flag.txt` file on the server.