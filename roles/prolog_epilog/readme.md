# prolog_epilog

### Description

Just a simple prolog_epilog role made to keep prolog and epilog files synced through cluster nodes

This role will configure the following:

- A simple prolog.sh script in /etc/slurm/prolog.sh 

This script will only execute any other script under /etc/slurm/prolog.d/ using the "run-parts" utility, if the directory is empty, it will execute nothing and return 0 .

- A simple epilog.sh script in /etc/slurm/epilog.sh

This script will only execute any other script under /etc/slurm/epilog.d/ using the "run-parts" utility, if the directory is empty, it will execute nothing and return 0 .

This role will also create both directories `/etc/slurm/prolog.d/` and  `/etc/slurm/epilog.d/` to make sure that prolog and epilog executes sucessifully out of the box.