#!/bin/bash
set -e 

logger -s -t slurm-prolog "START prolog for job=$SLURM_JOB_ID from user $SLURM_JOB_USER"
/usr/bin/run-parts /etc/slurm/prolog.d
logger -s -t slurm-prolog "END prolog for job=$SLURM_JOB_ID from user $SLURM_JOB_USER"