# bankjs

- Category: **Web Security**
- Flag Format: uhctf{…}

# Description

Someone attempted to write a bank application in everyone's favorite programming language. They gave me a live version, a demo account on there and a copy of the source code. Can you show them how the app is flawed?

# Attachments

- A copy of this source code (except for the README and git history off course)
- Link to a running version of the docker container

# Hints:

- 25%: general tips on how to get to the solution. <details><summary>CLICK TO SHOW</summary><ul><ul>
<li>  If only that dev wouldn't be the TYPE to use JavaScript. Try to look at function signatures and look for stupid JavaScript convertions. Check if everything does what you'd expect it to do.
</li>
</ul></ul></details>

- 50%: gives you the exact line where you can find the solution. <details><summary>CLICK TO SHOW</summary><ul><ul>
<li> tip.js:29 </li>
</ul></ul></details>

# Deployment

To deploy the challenge, build and run the docker, with your flag of choice as a environment variable:

```bash
docker build -t bankjs .
docker run -p 80:80 -e FLAG="uhctf{js_more_like_jf*ck_abcdef}" bankjs
```

# Writeup

By browsing through the source, you can see that you can get the flag from sending a tip to the admin.

The catch is that parseInt takes a string as input, but we gave it a number, which will trigger automatic type conversion.
Now, if you try 0.00000005, you'll see that the string conversion for that yields "5e-8". Now, that same string is fed as input to parseInt, which will take the first integer part, being 5.
