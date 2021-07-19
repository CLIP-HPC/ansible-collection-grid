#!/usr/bin/env bash
# Make sure to add SLURM walltime stanza if it is set in the HTCondor job via
# i.e. remote_cerequirements = "Walltime == 172800 && CondorCE == 1"
# see https://www-auth.cs.wisc.edu/lists/htcondor-users/2020-March/msg00011.shtml for more information
# Walltime is in seconds, so it needs to be converted to minutes for SLURM

if [ -n "$Walltime" ]; then
  echo "#SBATCH -t $((Walltime / 60))"
fi