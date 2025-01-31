# GridFTP [![Build Status](https://travis-ci.org/CLIP-HPC/ansible-role-gridftp.svg?branch=master)](https://travis-ci.org/CLIP-HPC/ansible-role-gridftp)

Ansible role for installation of GridFTP Server with lcmaps authorization

## Requirements

- EL7
- EPEL

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    role_gridftp_port_start: 5000
    role_gridftp_port_end: 5100

The port range for the GridFTP's data transfer streams

    role_gridftp_datainterface:

If the GridFTP server is behind NAT specify the datainterface hostname or IP addresse that is publicly reachable.

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
        - name: gridftp
          vars:
            grid_host_certificate:
              cert: /srv/certificates/host.crt
              key: /srv/certificates/host.key
              remote_src: true
            role_gridftp_datainterface: se.grid.vbc.ac.at

## License

MIT

## Author Information

Written by [Ümit Seren](http://github.com/timeu) in June 2020
