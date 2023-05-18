# Fishy Subdomain

- Category: OSINT

I made a super secure secret subdomain on my website ctf.wardsegers.be. Can you find it?

**Note**: hosting for this website is on the public Internet. DDoS and attacking the infra is explicitly forbidden and not required to solve the challenge!

## Setup

This was set up using Cpanel because I’m lazy and I had it at my disposal already.
1. Have a base domain (e.g. challenge.yourdomain.tld). Host folder src_base here using an Apache server (or setup HTTPS redirects manually)
1. Have a subdomain of that domain (e.g.). Host folder src_sub here using an Apache server (or setup HTTPS redirects manually)
1. Configure HTTPS for both subdomains with separate certs (to make the challenge not too easy)
1. Check on crt.sh if the setup works and you can find your subdomain.

## Solution

By going to ctf.wardsegers.be, you can see that the certificate is from Let’s Encrypt. Hints in the letter indicate (e.g. free since 2014) go to Let's Encrypt. All Let’s Encrypt certificates are public, so a secret subdomain on ctf.wardsegers.be would be publicly listed as well.
By going to a website (such as crt.sh), you can explore certificates issued for a given domain. In this particular case, by entering ctf.wardsegers.be, you can see a certificate for the subdomain super-duper-dolka-polka-poly-gizmo-domain.ctf.wardsegers.be.
By visiting the website, you see a page with the flag.

More info at https://en.wikipedia.org/wiki/Certificate_Transparency. It also links to alternatives to crt.sh.