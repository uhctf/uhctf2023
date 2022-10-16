# Imagine
* Category: **Reverse engineering**

* Flag Format: **uhctf{...}**

* Flags: <details><summary>CLICK TO SHOW</summary><ul><ul>
<li>static: <code>uhctf{no-Bert-assembly-is-not-obfuscation-80ff01}</code></li>
</ul></ul></details>

* Connection Info: \#TODO

* Requirements:
    * Ghidra
    * Python & pip
    * ASM knowledge

* Credits:
    * Mihály

* Hints: <ul><ul>
<li><details>
    <summary><strong>15%</strong>: Using keygen binary</summary>
    The keygen binary doesn't seem to work without a password. Can we replicate its workings somehow?
</details></li>
<li><details>
    <summary><strong>10%</strong>: Useful tools</summary>
    Open the keygen binary in Ghidra or IDA. This allows for static analysis of the ASM code.
</details></li>
</ul></ul>

## Description
ObfuDrive is an innovative player on the cloud storage market. Their motto is transparency, so everything is public. But don't worry, your files are encrypted! ObfuDrive devs very confident in their encryption. After all, the key generator's workings are obfuscated using ASM code.