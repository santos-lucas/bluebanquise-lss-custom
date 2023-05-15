#!/bin/sh -e

PAM_UID=$(getent passwd "${PAM_USER}" | cut -d: -f3)

#################################################
## Exclude limits for all administrative users ##
#################################################

if [ "${PAM_UID}" -eq 1023 ] || [ "${PAM_UID}" -eq 1023 ];then

exit 0

fi


#################################################

###################################
## Apply limits for normal users ##
###################################

if [ "${PAM_UID}" -ge 1000 ]; then

/usr/bin/systemctl set-property "user-${PAM_UID}.slice" \
CPUQuota=20% MemoryLimit=1024M BlockIOWeight=10

fi
