#! /bin/bash

SCRIPT_PATH=`dirname $0`

# no optimisations to keep most things readable
BINARY=`mktemp`
echo "Compiling"
clang $SCRIPT_PATH/keygen.c -o $BINARY -O0 -g -m32 -fno-stack-protector -lcrypto
chmod +x $BINARY

# replace hash placeholder in binary with actual hash of .text
TEXT_DUMP=`mktemp`
echo "Replacing .text's hash value"
objcopy -O binary --only-section=.text $BINARY $TEXT_DUMP
TEXT_HASH=`sha256sum -b $TEXT_DUMP | cut -d' ' -f1`
/usr/bin/sed -i "s/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/$TEXT_HASH/" $BINARY

# clean up
mv $BINARY $SCRIPT_PATH/keygen
rm $TEXT_DUMP