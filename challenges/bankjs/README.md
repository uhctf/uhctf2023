# bankjs

- Category: **Web Security**
- Flag Format: uhctf{…}

# Description

Someone attempted to write a bank application in everyone's favorite programming language. And of course, it uses its own cryptocurrency, bankjs dollars (BJ$). They gave me a live version, a demo account on there and a copy of the source code. Can you show them how the app is flawed?

# Attachments

- A copy of this source code (everything in the src and static folder)
- Link to a running version of the docker container

# Flag

<details>
<summary>CLICK TO SHOW</summary>
<pre>uhctf{js_more_like_jf*ck_7b453d6}</pre>
</details>

# Hints:

- 25%: general tips on how to get to the solution. <details><summary>CLICK TO SHOW</summary><ul><ul>
<li>  If only that dev wouldn't be the TYPE to use JavaScript. Try to look at function signatures and look for stupid JavaScript conversions. Check if everything does what you'd expect it to do.
</li>
</ul></ul></details>

- 50%: gives you the exact line where you can find the solution. <details><summary>CLICK TO SHOW</summary><ul><ul>
<li> tip.js:29 </li>
</ul></ul></details>

# Deployment

To deploy the challenge, build and run the docker, with your flag of choice as a environment variable:

```bash
docker build -t bankjs .
docker run -p 80:80 bankjs
```