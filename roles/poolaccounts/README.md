# poolaccounts [![Build Status](https://travis-ci.org/hephyvienna/ansible-role-poolaccounts.svg?branch=master)](https://travis-ci.org/hephyvienna/ansible-role-poolaccounts) ![Ansible Role](https://img.shields.io/ansible/role/40961.svg)

Create Pool Accounts for WLCG/EGI Grid Site

*   See old [YAIM Guide](https://twiki.cern.ch/twiki/bin/view/LCG/YaimGuide400#users_conf)

## Role Variables

Accounts are defined as a list of dictionaries describing the user group.

For each group first the correspondig unix grouo mis created and then the user accounts.

*   _name_ - python format string
*   _uid_ - uid of the first account
*   _number_ - number accounts to be created
*   _step_ - uid of an account is _uid + i * step_
*   _description_ - command for _/etc/passwd_
*   _group_ - name of the group
*   _gid_ - gid of the groups
*   _groups_ - additional groups of which the accounts are member
*   _fqan_ - Fully qualified attribute name describing the relevant VOMS role

The example demonstrates the usage. If _number_ is not defined, only
one account _name_ is created.

      poolaccounts:
        - name: 'cms%03d'
          uid: 10000
          number: 100
          step: 2
          description: 'Standard User of the CMS VO'
          group: cms
          gid: 10000
          fqan: /cms
        - name: 'cmsprd%02d'
          uid: 11000
          number: 10
          step: 2
          description: 'Production User of the CMS VO'
          group: cmsprd
          gid: 11000
          groups: cms
          fqan: /cms/Role=production
        - name: 'cmspil%02d'
          uid: 12000
          number: 10
          step: 2
          description: 'Pilot User of the CMS VO'
          group: cmspil
          gid: 12000
          groups: cms
          fqan: /cms/Role=pilot
        - name: 'cmssgm'
          uid: 13000
          description: 'SW User of the CMS VO'
          group: cmssgm
          gid: 13000
          groups: cms
          fqan: /cms/Role=lcgadmin

Additional settings

    poolaccounts_homedir: /home

Prefix for the home directory

    poolaccounts_enable_cleanup: false

Install and config grid cleanup routines for home directories

    poolaccounts_enable_gridmapdir: false

Create _gridmapdir_ for administration of grid accounts

    poolaccounts_enable_grid-mapfile: false

Configure _grid-mapfile_  for mapping of the accounts to VOMS attributes.

    poolaccounts_enable_groupmapfile: false

Configure _groupmapfile_ for mapping the groups to VOMS attributes.


## Example Playbook

    - hosts: servers
      roles:
         - role: hephyvienna.poolaccounts
           vars:
             poolaccounts:
               - name: 'cms%03d'
                 uid: 10000
                 number: 100
                 step: 2
                 description: 'Standard User of the CMS VO'
                 group: cms
                 gid: 10000
               - name: 'cmsprd%02d'
                 uid: 11000
                 number: 10
                 step: 2
                 description: 'Production User of the CMS VO'
                 group: cmsprd
                 gid: 11000
                 groups: cms
               - name: 'cmspil%02d'
                 uid: 12000
                 number: 10
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

## License

MIT

## Author Information

Written by [Dietrich Liko](http://hephy.at/dliko) in April 2019

[Institute for High Energy Physics](http://www.hephy.at) of the
[Austrian Academy of Sciences](http://www.oeaw.ac.at)
