#!/bin/bash
let c=False
while read l; do
    [[ -n $l && ${l###} = $l ]] && ssh-keygen -l -f /dev/stdin <<<$l;
    c=True
done < ~/.ssh/authorized_keys
if [ "$c" = "True" ]
 then
  echo '1'
fi