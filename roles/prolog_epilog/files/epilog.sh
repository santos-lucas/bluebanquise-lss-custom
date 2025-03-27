#!/bin/bash
set -e 

logger -s -t slurm-epilog "START epilog for job=$SLURM_JOB_ID from user $SLURM_JOB_USER "
/usr/bin/run-parts /etc/slurm/epilog.d
logger -s -t slurm-epilog "END epilog for job $SLURM_JOB_ID form user $SLURM_JOB_USER"