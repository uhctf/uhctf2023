#! /bin/bash

PASSWORD='ZNsHtmyn'
FLAG='uhctf{no-Bert-assembly-is-not-obfuscation-80ff01}'

# compile keygen
./keygen/compile.sh

# write password file
echo -n $PASSWORD > ./website/password

# write flag
echo -n $FLAG > ./website/uploads/the_flag.txt

# "upload" encrypted files
cd ./website/
if [[ -f ./.venv ]]; then source "$HOME/.virtualenvs/`cat ./.venv`/bin/activate"; else pip3 install -r ./requirements.txt; fi
for file in `ls ./uploads/`; do
    python3 ./encrypt_file.py $PASSWORD $file
done
if [[ -f ./.venv ]]; then deactivate; fi
cd -

# upload plain text files
cp ./keygen/keygen ./website/uploads/
cp ./website/app.py ./website/uploads/
