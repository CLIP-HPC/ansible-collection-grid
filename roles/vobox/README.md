# VOBOX [![Build Status](https://travis-ci.org/CLIP-HPC/ansible-role-vobox.svg?branch=master)](https://travis-ci.org/CLIP-HPC/ansible-role-vobox)

Ansible role for installation of GRID Vobox for WLCG/LCG site.

Inspired by the [Vobox Guide](https://twiki.cern.ch/twiki/bin/view/LCG/WLCGvoboxDeployment).

## Requirements

-   EL7
-   EPEL

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    role_vobox_create_user: false

If the grid users should be created locally or if they already exist on the system (i,.e. LDAP/AD)

    role_vobox_accounts: []

List of accounts to configure on the Vobox for access

    grid_host_certificate: {
      cert: 'files/my.example.com.crt'
      key: 'files/my.example.com.key''
      remote_src: false
    }

Dictionary with location of host certificate and key to be copied into /etc/grid-security.
The flag `remote_src` specifies whether the files are on the remote host or on the ansible host.

## Example Playbook

Configuration for a server without CVMFS

    - hosts: servers
      roles:
        - name: vobox
          vars:
            role_vobox_create_user: true
            grid_host_certificate:
              cert: /srv/certificates/host.crt
              key: /srv/certificates/host.key
              remote_src: true
            role_vobox_storage_element: se.grid.vbc.ac.at
            role_vobox_host: vobox.grid.vbc.ac.at
            role_vobox_sitename: T2_AT_VIENNA
            role_vobox_vos:
              - cms
              - alice
            role_vobox_accounts:
              - name: "cmssgm"
                uid: 44050
                primary_group: cmssgm
                primary_gid: 44050
                secondary_group: cms
                secondary_gid: 49995
                vo: cms
                fqan: /cms/Role=lcgadmin
              - name: "alicesmg01"
                uid: 45450
                primary_group: alicesgm
                primary_gid: 45450
                secondary_group: alice
                secondary_gid: 49996
                vo: alice
                fqan: /alice/Role=lcgadmin

## License

MIT

## Author Information

Written by [Ümit Seren](http://github.com/timeu) in June 2020
