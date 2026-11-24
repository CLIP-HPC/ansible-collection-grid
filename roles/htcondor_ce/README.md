# htcondor_ce [![Build Status](https://travis-ci.com/hephyvienna/ansible-role-htcondor-ce.svg?branch=master)](https://travis-ci.com/hephyvienna/ansible-role-htcondor-ce) [![Ansible Role](https://img.shields.io/ansible/role/41511.svg)](https://galaxy.ansible.com/hephyvienna/htcondor-ce)

Configuraion of the HTCondor CE for WLCG/EGI site

Inspired by the [Puppet Module](https://github.com/cernops/puppet-htcondor_ce)
and the [Wiki entry](https://wiki.infn.it/progetti/htcondor-tf/htcondor-ce_setup).
There is also the [OSG documentation](https://bbockelm.github.io/docs/compute-element/htcondor-ce-overview).

## Requirements

*   EL6/7
*   EPEL
*   UMD repos

## Role Variables

    htcondor_ce_repo_install: true

Install HTCondor repository

    htcondor_ce_spool_dir_mode: "0755"

Mode of the spool directory `htcondor_ce_spool_dir` (owned by `condor`). Set it to the mode the storage
sets if the spool is a shared volume, so the role and the storage don't change it back and forth.

    htcondor_ce_apel_acct_group_map:
      - '* /^https\:\/\/cms\-auth\.cern\.ch\// /cms/Role=pilot/Capability=NULL'

Lines of `/etc/condor/apel_acct_group.map`. Jobs submitted with a token have no VOMS FQAN, so
`condor_ce_blah.sh` maps "token issuer,token subject" with this map to the APEL accounting group.
Without a matching line the job has no VO in APEL. See the HTCondor-CE
[APEL scripts](https://github.com/htcondor/htcondor-ce/tree/main/contrib/apelscripts).



## Dependencies

-   grid

## Example Playbook

    - hosts: servers
      vars:
        poolaccounts:
          - name: 'cms%03d'
            uid: 10000
            number: 2
            step: 2
            description: 'Standard User of the CMS VO'
            group: cms
            gid: 10000
          - name: 'cmsprd%02d'
            uid: 11000
            number: 2
            step: 2
            description: 'Production User of the CMS VO'
            group: cmsprd
            gid: 11000
            groups: cms
          - name: 'cmspil%02d'
            uid: 12000
            number: 2
            step: 2
            description: 'Pilot User of the CMS VO'
            group: cmspil
            gid: 12000
            groups: cms
          - name: 'cmssgm'
            uid: 13000
            description: 'SW User of the CMS VO'
            group: cmssgm
            gid: 13000
            groups: cms
        grid_vos:
          - cms
      roles:
        - role: poolaccounts
        - role: grid
        - role: htcondor-ce


## License

MIT

## Author Information

Written by [Dietrich Liko](http://hephy.at/dliko) in June 2019

[Institute for High Energy Physics](http://www.hephy.at) of the
[Austrian Academy of Sciences](http://www.oeaw.ac.at)
