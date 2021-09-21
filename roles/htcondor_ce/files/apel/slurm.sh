#!/bin/bash -eu

fail () {
    echo "$@" >&2
    exit 1
}

safe_config_val () {
    var=$1
    attr=$2
    val=$(condor_ce_config_val $attr) ||
    fail "Failed to retrieve CE configuration value '$attr'"
    eval "$var"='$val'
}

# Create a temporary accounting file name
today=$(date -u --date='00:00:00 today' +%FT%T)
yesterday=$(date -u --date='00:00:00 yesterday' +%FT%T)

OUTPUT_DIR="$(condor_ce_config_val APEL_OUTPUT_DIR)"
OUTPUT_FILE="$OUTPUT_DIR/batch-$(date -u --date='yesterday' +%Y%m%d )-$(hostname -s)"

[[ -d $OUTPUT_DIR && -w $OUTPUT_DIR ]] || fail "Cannot write to $OUTPUT_DIR"


safe_config_val BATCH_HOST APEL_BATCH_HOST

TZ=GMT sacct -s CD,F,TO,OOM -P -n --format=JobID,JobName,User,Group,Start,End,Elapsed,TotalCPU,Partition,NCPUS,NNodes,NodeList,MaxRSS,MaxVMSize,State -r grid,cms -S "$yesterday" -E "$today" | grep batch > $OUTPUT_FILE