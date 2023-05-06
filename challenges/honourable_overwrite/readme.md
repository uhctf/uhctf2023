# Honourable Overwrite
* Category: **Reversing & BinExp**

* Flag Format: **uhctf{...}**

* Flags: <details><summary>CLICK TO SHOW</summary><ul><ul>
<li>static: <code>uhctf{8uff3r-0v3rf10w-70-7h3-k1n9d0m-26fa2b}</code></li>
</ul></ul></details>

* Connection Info: \#TODO

* Requirements:

* Credits:
    * mihály

* Hints: <ul><ul>
<li><details>
    <summary><strong>5%</strong>: Help using gdb.</summary>
    gdb is a powerful tool to see what a program is doing at runtime. However, it's a cli tool that doesn't show much information, causing newcomers to easily get lost. Try installing <a src="https://github.com/hugsy/gef">gef</a>.
</details></li>
<li><details>
    <summary><strong>15%</strong>: Where is the vulnerability?</summary>
    Open the binary in Ghidra. Look for places where you can interact with the program.

    Don't be afraid to read documentation on C standard library functions! <i>man [function_name]</i> or simply Google will help you out!
</details></li>
</ul></ul>

## Description
Who goes there? - shouted the guard. He was old and seemed to be fixed on certain values. But maybe we should overcome old habits and replace them in order to move forward?

Convince the guard to let you pass.