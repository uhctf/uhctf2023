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
    <summary><strong>25%</strong>: Gives you the message from </summary>
    Sent from my Pixel 6
</details></li>
<li><details>
    <summary><strong>50%</strong>: Tells you what is wrong with the image</summary>
    Sent from my Pixel 6
</details></li>
</ul></ul>

## Description
My SO sent me this picture of aCropTop that they liked. I'm not into it, but what do you think of it? To me, it's just a bunch of Pixels.

## Writeup

This is a cropped screenshot from a Pixel 6. There was recently a vulnerability with Pixel devices (dubbed the acropalypse). Instead of removing the old screenshot after a crop, it was instead overwriting the old file. This means that if you crop a image (and thus make it smaller), you would still be able to have some residual data from the older and bigger screenshot.

To decode this image, submit it on a site like https://acropalypse.app
