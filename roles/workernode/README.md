# workernode [![Build Status](https://travis-ci.com/hephyvienna/ansible-role-workernode.svg?branch=master)](https://travis-ci.com/hephyvienna/ansible-role-workernode) [![Ansible Role](https://img.shields.io/ansible/role/41059.svg)](https://galaxy.ansible.com/hephyvienna/workernode)


Ansible role for installation of WLCG/EGI worker node or user interface


# Requirements

-   EL6/7
-   EPEL

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    workernode_ui: false

Request installation of user interface

    workernode_install_htc_ce_client: false

Install HTCondor CE client

## Dependencies

*   hephyvienna.grid

## Example Playbook

    - hosts: all
      roles:
        - role: geerlingguy.repo-epel
        - role: hephyvienna.grid
          vars:
            grid_vos:
              - cms
              - alice
              - belle
            grid_umd_repo_exclude:
              - dpm-*
              - lfc-*
              - lcgdm-*
        - role: hephyvienna.workernode


## License

MIT

## Author Information

Written by [Dietrich Liko](http://hephy.at/dliko) in May 2019

[Institute for High Energy Physics](http://www.hephy.at) of the
[Austrian Academy of Sciences](http://www.oeaw.ac.at)
