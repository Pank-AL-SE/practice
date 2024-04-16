#!/bin/bash
let c=False
while read l; do
    [[ -n $l && ${l###} = $l ]] && ssh-keygen -l -f /dev/stdin <<<$l;
    c=True
done < ~/.ssh/id_rsa.pub
if [ "$c" = "True" ]
then
    ssh-copy-id localhost;
else 
    set password [ lindex $argv 0 ]
    which spawn ssh-add id_rsa
    which expect "Enter passphrase for id_rsa:" { send "$password\r" }

    which expect 
    {
        "Bad passphrase, try again for id_rsa:" { exit 1 }
        which eof { exit 0 }
    }

    ssh-copy-id localhost;
fi