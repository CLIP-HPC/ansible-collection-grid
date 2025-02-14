#!/bin/bash -eu

# "timestamp=2019-05-01 23:56:01" "userDN=/C=UK/O=eScience/OU=Liverpool/L=CSD/CN=stephen jones" "userFQAN=/dteam/Role=NULL/Capability=NULL" "ceID=hepgrid6.ph.liv.ac.uk:9619/hepgrid6.ph.liv.ac.uk-condor" "jobID=1.0_hepgrid6.ph.liv.ac.uk" "lrmsID=1_hepgrid6.ph.liv.ac.uk" "localUser=dteam001"

fail () {
    echo "$@" >&2
    exit 1
}

safe_config_val () {
    var=$1
    attr=$2
    val=$(condor_ce_config_val "$attr") ||
    fail "Failed to retrieve CE configuration value '$attr'"
    eval "$var"="$val"
}

DATE='today'
if [ $# -ge 1 ] && [ -n "$1" ]; then
    DATE=$1
fi

today=$(date -u --date="00:00:00 $DATE" +%s)
yesterday=$(date -u --date="00:00:00 $DATE - 1 day" +%s)

safe_config_val OUTPUT_DIR APEL_OUTPUT_DIR
OUTPUT_FILE="$OUTPUT_DIR/blahp-$(date -u --date="$DATE - 1 day" +%Y%m%d )-$(hostname -s)"

if [ ! -d "$OUTPUT_DIR" ] || [ ! -w "$OUTPUT_DIR" ]; then
    echo "Cannot write to $OUTPUT_DIR"
    exit 1
fi

# Build the filter for the history command
CONSTR="EnteredCurrentStatus >= $yesterday && EnteredCurrentStatus < $today && RemoteWallClockTime != 0 && GridJobId =!= UNDEFINED "

safe_config_val CE_HOST APEL_CE_HOST
safe_config_val BATCH_HOST APEL_BATCH_HOST
safe_config_val CE_ID APEL_CE_ID

# Need to replace the GridJobId which is in format "batch slurm ce-1.grid.vbc.ac.at_9619_ce-1.grid.vbc.ac.at_780192.0_1631527967 slurm/20210913/26830538" to match the output from the batch logs using sacct
SED_FILTER="s/batch slurm .+slurm\/[[:digit:]]+\/([[:digit:]]+)/\1.batch/"

TZ=GMT condor_ce_history -const "$CONSTR" \
 -format "\"timestamp=%s\" " 'formatTime(EnteredCurrentStatus, "%Y-%m-%d %H:%M:%S")' \
 -format "\"userDN=%s\" " x509userproxysubject \
 -format "\"userFQAN=%s\" " x509UserProxyFirstFQAN \
 -format "\"ceID=${CE_ID}\" " EMPTY \
 -format "\"jobID=%v_${CE_HOST}\" " RoutedFromJobId \
 -format "\"lrmsID=%v\" " GridJobId \
 -format "\"localUser=%s\"\n" Owner | sed -r "$SED_FILTER"  > "$OUTPUT_FILE"
