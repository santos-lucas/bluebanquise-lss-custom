This role is an simple role to control sudoers configuration for a group of managed nodes.

By default, it will remove all the files on /etc/sudoers.d/* to ensure that only the configured permissions are there. For now the /etc/sudoers default file is not managed.




```yaml
---
sudoers: groups:
group1:
policy: "ALL=(root) NOPASSWD:" allow:
-	/usr/sbin/iotop
-	/usr/bin/perf
-	/usr/bin/nvidia-smi
-	/usr/bin/strace bullatos:
users:
bulladm:
policy: "ALL=(root) NOPASSWD:" allow:
-	/opt/PMSM/bin/pmsmMC.py
-	/bin/sinfo
-	/usr/sbin/ibstat default:
policy: "ALL=(root) NOPASSWD:" deny:
-	"/bin/su"
-	"/usr/bin/*sh"
```
