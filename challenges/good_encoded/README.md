# Good enCODEd message

<!-- crypto, forensics, osint, reversing, stegano, websec, misc -->
* Category: **{{Stegano}}**

<!-- * "uhctf{...}": must match regex "uhctf{([a-z0-9]+-)*[0-9a-f]{6}}" -->
<!-- * "free-form": anything goes, mention in description what to look for -->
* Flag Format: uhctf{…}

<!-- {{FLAG_TYPE}} can be "static" or "regex" -->
* Flags: <details><summary>CLICK TO SHOW</summary><ul><ul>
<li>static: <code>uhctf{hello_printing_384493}</code></li>
</ul></ul></details>

* Credits:
	* ward

## Description

A friend sent me this file; told me it was Good enCODEd.

# Write-up

The file is a GCODE file. This type of file is what is used by o.a. 3D printers, CNC routers and laser cutters to get their instructions. If you open this file in Cura, you can explore the different layers of the print. In the middle, you'll find that there's a text encoded in the middle of the object.
