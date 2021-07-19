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

    htcondor_ce_repo_development_enable: false

Enable development repo for latest version

    htcondor_ce_batch_system: slurm

Select batch system (only slurm tested)

    htcondor_ce_enable_static_shadow: false

Did not test this feature.

    htcondor_ce_enable_bdii: true

Enable BDII publictaion of the service

    htcondor_ce_uid_domain: "{{ ansible_domain }}"

Recognise local condor daemons as friendly (not useful for batch system deployment)

    htcondor_ce_condor_view_hosts: []

Condor View Hosts routes your collector information to global or site collectors

    htcondor_ce_pool_collector_str: ''

Set appropriate place to route.

    htcondor_ce_gsi_regexp: '^\/DC\=ch\/DC\=cern\/OU\=computers\/CN\=(host\/)?([A-Za-z0-9.\-]*)$'


    htcondor_ce_benchmark_result: 10.00-HEP-SPEC06
    htcondor_ce_execution_env_cores: 16
    htcondor_ce_election_hosts:
      - "{{ ansible_fqdn }}"

For publication in the BDII

    htcondor_ce_argus_server: argus.hephy.oeaw.ac.at

Argus server

    htcondor_ce_argus_port: 8154

Argus server port

    htcondor_ce_argus_resourceid: http://authz-interop.org/xacml/resource/resource-type/ce

Argus resource id

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
