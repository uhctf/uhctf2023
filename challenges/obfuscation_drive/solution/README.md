# Solution
## Recon
### Website
You get access to a weird cloud storage service. Every uploaded file is publicly available. All user's files are encrypted, except the files uploaded by the cloud service provider themselves. We immediately notice the enticing `the_flag.txt.encrypted` file, but it's encrypted.

Unencrypted files can be downloaded as is. Encrypted files require a password to be decrypted. Opening the network tab in your browser's developer panel and (attempting) to download files will reveal the `/uploads/<file_name>?decrypt=<bool>&password=<pass>` endpoint. Browsing to `/uploads/the_flag.txt.encrypted` allows us to download the encrypted version of the flag file.

### app.py
`app.py` is the python source code of the running web server. Reading the source code reveals how files are decrypted.

- The server gets a password and the file name of the file to decrypt.
- A subprocess is started, invoking the keygen binary. The password and file name are passed as parameters. The output is an AES key (based on the function's name).
- The file is loaded and decrypted with the AES key.

If we can somehow manage to get the AES key, this code can easily by adapted to decrypt `the_flag.txt.encrypted` that we downloaded earlier.

### keygen
`keygen` is, as the name implies, a key generator. As we learned above, it generates an AES key to decrypt files. However, it requires a password to run.

We cannot tamper with the binary as it includes anti-debugging and anti-tampering features. (They can by bypassed but this is likely harder than the intended route 😁)

Opening the binary in e.g. Ghidra will allow us to reverse engineer the key generation process. More specifically, we can adapt the `keygen` function to python (see the `solution.py` file). This requires reading some assembly and/or Ghidra's decompiler output.