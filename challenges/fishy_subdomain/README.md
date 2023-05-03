# Fishy Subdomain

<!-- crypto, forensics, osint, reversing, stegano, websec, misc -->
* Category: **{{OSINT}}**

<!-- * "uhctf{...}": must match regex "uhctf{([a-z0-9]+-)*[0-9a-f]{6}}" -->
<!-- * "free-form": anything goes, mention in description what to look for -->
* Flag Format: uhctf{…}

<!-- {{FLAG_TYPE}} can be "static" or "regex" -->
* Flags: <details><summary>CLICK TO SHOW</summary><ul><ul>
<li>static: <code>uhctf{okay-boomer-its-just-a-stupid-button-513a73}</code></li>
</ul></ul></details>

* Connection Info: **ctf.wardsegers.be**

* Credits:
	* ward

* Hints: <ul><ul>
<li><details>
    <summary><strong>15%</strong>: Gives you can idea of the kind of resource(s) to look for</summary>
    Can’t find it? That’s because it is secure! I even got a certificate for that!
</details></li>
<li><details>
    <summary><strong>60%</strong>: Will tell you how you can use the mentioned resource to get to it.</summary>
    Did you know that every certificate that got issued is publicly known?
</details></li>
</ul></ul>

## Description

I made a super secure secret subdomain on my website ctf.wardsegers.be. Can you find it?

**Note**: hosting for this website is on the public Internet. DDoS and attacking the infra is explicitly forbidden and not required to solve the challenge!

## Setup

This was set up using a Cpanel website because I’m lazy and I had it at my disposal already.
1. Have a base domain (e.g. challenge.yourdomain.tld). Host folder src_base here using an Apache server (or setup HTTPS redirects manually)
1. Have a subdomain of that domain (e.g. subdomainthatisdifficulttoguess.challenge.yourdomain.tld). Host folder src_sub here using an Apache server (or setup HTTPS redirects manually)
1. Configure HTTPS for both subdomains with separate certs (to make the challenge not too easy)
1. Check on crt.sh if the setup works and you can find your subdomain.

**Update**: I had to move the subdomain away from the Cpanel, as it made the certificates overlap. Consider separating hosting of the two sites to make sure your hosting doesn't optimize certificates.

# Write-up

By going to ctf.wardsegers.be, you can see that the certificate is from Let’s Encrypt. Hints in the letter indicate (e.g. free since 2014) point to the free certificates of Let's Encrypt. All Let’s Encrypt certificates are public, so a secret subdomain on ctf.wardsegers.be would be publicly listed as well (at least if if has HTTPS using their certificate).
By going to a website (such as https://crt.sh or https://censys.io/certificates), you can explore certificates issued for a given domain. In this particular case, by entering ctf.wardsegers.be, you can see a certificate for the subdomain super-duper-dolka-polka-poly-gizmo-domain.ctf.wardsegers.be.
By visiting the website, you see a page with the flag.

# Source

https://linasvaliukas.medium.com/by-the-way-the-list-of-ssl-tls-certificates-issued-to-you-including-subdomains-is-public-5537ef1f11f5
