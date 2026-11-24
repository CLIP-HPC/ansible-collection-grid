========================
clip.grid Release Notes
========================

.. contents:: Topics

v2.2.5
======
Release Summary
---------------
- HTCondor-CE (bugfix): Report the VO of token-submitted jobs to APEL. condor_ce_blah.sh falls back to the token subject and maps "issuer,subject" to the accounting group with htcondor_ce_apel_acct_group_map
- HTCondor-CE: Add htcondor_ce_spool_dir_mode to set the mode of the spool directory (default 0755)

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
