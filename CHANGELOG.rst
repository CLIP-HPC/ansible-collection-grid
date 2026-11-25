========================
clip.grid Release Notes
========================

.. contents:: Topics

v2.3.1
======
Release Summary
---------------
- EOSxd (bugfix): Add eosxd_mount_opts for the /etc/fstab entry, default "fsname=eos,_netdev,nofail". Without _netdev and nofail a failed or hanging /eos mount fails local-fs.target and puts the host into emergency mode
- EOSxd: With eosxd_fstab_state: mounted, the changed options remount /eos on the next run, which can hang or interrupt running jobs. Apply the upgrade with eosxd_fstab_state: present to defer the change to the next reboot or manual remount

v2.3.0
======
Release Summary
---------------
- Grid, CVMFS, EOSxd: Split the roles into install.yml (repositories and packages, no services) and configure.yml, so image builds can install with tasks_from: install.yml and configure at first boot. main.yml runs both, so existing callers don't change
- Grid: Install all packages, including fetch-crl and the VOMS RPMs, before writing configuration
- EOSxd: Check eosxd_mgmt_alias after installing eos-fusex instead of before

v2.2.5
======
Release Summary
---------------
- HTCondor-CE (bugfix): Report the VO of token-submitted jobs to APEL. condor_ce_blah.sh falls back to the token subject and maps "issuer,subject" to the accounting group with htcondor_ce_apel_acct_group_map
- HTCondor-CE: Add htcondor_ce_spool_dir_mode to set the mode of the spool directory (default 0755)
- HTCondor-CE: Add the collector host (condor://) to the SciTokens server audience
- Grid, HTCondor-CE (bugfix): Import the WLCG and HTCondor GPG keys with rpmkeys on EL10. rpm_key fails on EL10.3+ because gpg cannot parse the OpenPGP v6 release key that Rocky Linux 10.3 adds to the rpm database
- Grid (bugfix): Link /etc/vomses to CVMFS when grid_use_cvmfs_for_voms_certs is enabled
- CVMFS (bugfix): Quote the CVMFS_SERVER_URL server list in the domain configuration
- Grid: Remove the wlcg-repo/umd-release packages when grid_install_wlcg_repo/grid_install_umd_repo is false (e.g. repositories provided by Satellite)
- HTCondor-CE (bugfix): Don't download the HTCondor GPG key when htcondor_ce_repo_install is false
- Docs: Fix the repository variable names in the grid and eosxd READMEs

v2.2.4
======
Release Summary
---------------
- CVMFS: Add cvmfs_skip_chksetup and cvmfs_skip_probe variables to skip the cvmfs_config chksetup/probe checks

v2.2.2
======
Release Summary
---------------
- Add support for configuring fetch-crl options via ansible variables

v2.2.1
======
Release Summary
---------------
- Grid (bugfix): Use RPM for Belle VOMS configuration

v2.2.0
======
Release Summary
---------------
- CVMFS (bugfix): Don't install cvmfs-auto-setup package. Configure autofs manually

v2.1.1
======
Release Summary
---------------
- Add support for CVMFS-based VOMS configuration
- Bugfix: Fix RHEL10 issue in the grid role

v2.1.0
======
Release Summary
---------------
- Add support for RHEL10 (except htcondor_ce)
- Switch molecule tests to ansible-native method
- Support testing on MacOS ARM platform
- Use uv for local development and testing


v2.0.1
======
Release Summary
---------------
- FIx IGTF GPG Key

v2.0.0
======
Release Summary
---------------

- Refactor grid collection and add support for RHEL9

v1.6.0
======

Release Summary
---------------

- Add support for newer ansible versions
- Update VOMS info for belle
