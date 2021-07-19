# cvmfs [![Build Status](https://travis-ci.com/hephyvienna/ansible-role-cvmfs.svg?branch=master)](https://travis-ci.com/hephyvienna/ansible-role-cvmfs) [![Ansible Role](https://img.shields.io/ansible/role/40972.svg)](https://galaxy.ansible.com/hephyvienna/cvmfs)

Install and configure [CVMFS](https://cernvm.cern.ch/portal/filesystem) client

Inspired by the [Puppet Module](https://github.com/cvmfs/puppet-cvmfs)

## Requirements

*   EL6/7

## Role Variables

The configuration of a CVMFS client is described in more details in the [documentation](https://cvmfs.readthedocs.io/en/stable/)

    cvmfs_manage_yumrepo: false
    cvmfs_yumrepo_enabled: true
    cvmfs_yumrepo_testing_enabled: false
    cvmfs_yumrepo_config_enabled: false
    cvmfs_yumrepo_priority: 10

Manage CVMFS Yum repository and configure it.

    cvmfs_manage_cvmfs_user: true

Manage the creation of a cvmfs user and group

    cvmfs_mount_repositories: [ autofs | mount ]

Mount repositories using autofs or by explicit mount

    cvmfs_http_proxy:
      - http://squid01.example.org:3128|http://squid02.example.org:3128
      - DIRECT

Define the http proxy

    cvmfs_cache_base: /var/cache/cvmfs

The location of the cache

    cvmfs_cache_quota: 4000

The size of the cache

    cvmfs_quota_fraction: 0.85

In case the cache is on a separate partition, its size can be given
as a fraction of the partition size

    cvmfs_config:
      CVMFS_USE_GEOAPI: yes

Other global settings can be passed by a hash


    cvmfs_repositories:
      - name: cms.cern.ch
        config:
          CMS_CACHE_BASE: /var/lib/test
        env_vars:
          CMS_LOCAL_SITE: /cvmfs/cms.cern.ch/SITECONF/T2_AT_Vienna

Repositories and their settings are provided as a hash

## Example Playbook

    - hosts: servers
      roles:
         - role: hephyvienna.cvmfs
           vars:
             cvmfs_quota_limit: 4000
             cvmfs_repositories:
               - name: cms.cern.ch
                 env_vars:
                   CMS_LOCAL_SITE: /cvmfs/cms.cern.ch/SITECONF/T2_AT_Vienna
               - name: belle.cern.ch

## License

MIT

## Author Information

Written by [Dietrich Liko](http://hephy.at/dliko) in April 2019

[Institute for High Energy Physics](http://www.hephy.at) of the
[Austrian Academy of Sciences](http://www.oeaw.ac.at)
