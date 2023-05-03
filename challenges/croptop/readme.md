# Croptop

* Category: **forensics**
* Flag Format: **uhctf{...}**
* Flags: <details><summary>CLICK TO SHOW</summary><ul><ul>
<li>static: <code>uhctf{iftheywerecheatingthiswouldbeamessagefromasidepartner-d4bedc}</code></li>
</ul></ul></details>

<!-- Only enter people's first name in lowercase, it will be changed later -->
* Credits:
    * ward

* Hints: <ul><ul>
<li><details>
    <summary><strong>for 75%</strong>: Hint of something particular about the picture</summary>
    Sent from my Google Pixel phone
</details></li>
<li><details>
    <summary><strong>for 50%</strong>: Tells you what you can do with the information of the previous hint</summary>
    Google for recent vulnerabilities of this device.
</details></li>
<li><details>
    <summary><strong>for 25%</strong>: Name of the exact problem</summary>
    You don't like it? That would be an acropalypse!
</details></li>
</ul></ul>

## Description

My SO sent me this picture of aCropTop that they liked. I'm not into it, but what do you think of it? To me, it's just a bunch of Pixels.

## Writeup

This is a cropped screenshot from a Pixel 7. There was recently a vulnerability with Pixel devices (dubbed the acropalypse). Instead of removing the old screenshot after a crop, it was instead overwriting the old file. This means that if you crop a image (and thus make it smaller), you would still be able to have some residual data from the older and bigger screenshot.

To decode this image, submit it on a site like https://acropalypse.app
