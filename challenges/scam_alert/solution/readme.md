# Solution
<!-- optionally include any relevant solution files in this folder -->

- the messages in the chat are hex encoded
- decoding from hex gives garbage -> messages might be ciphertext
- there is a hint "confidently protected, just like WEP" -> WEP uses RC4 for confidentially
- decrypting with RC4 requires a key
- the users need each others' key to communicate -> look for something within the account
- profile pictures have a base64 identifier
- decrypting the ciphertext using the picture identifier as a key gives hex output
- decoding from hex gives the plaintext