# grid [![Build Status](https://travis-ci.org/hephyvienna/ansible-role-grid.svg?branch=master)](https://travis-ci.org/hephyvienna/ansible-role-grid) [![Ansible Role](https://img.shields.io/ansible/role/40989.svg)](https://galaxy.ansible.com/hephyvienna/grid)

Ansible role for installation of grid repositories, certificates and voms definitions for WLCG/LCG site.

Inspired by the [Ansible Role UMD](https://github.com/EGI-Foundation/ansible-role-umd) by EGI-Foundation.

## Requirements

-   EL9
-   EPEL

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    grid_enable_repo: true

Set up the [grid repository](http://repository.egi.eu/category/umd_releases/distribution/umd-4/)
including [yum priorties](https://wiki.centos.org/PackageManagement/Yum/Priorities).

    grid_umd_version: 4

UMD version of the repository. Its most likely 4.

    grid_umd_exclude: []

List of packages to exclude from updates or installs.

    grid_umd_includepkgs: []

List of packages you want to only use from the UMD repository.

    grid_enable_certificates: true | false | 'cvmfs'

Enable grid certificates. 'cvmfs' implies the usage of certificates
from the CVMFS repositoru grid.cern.ch

    grid_ca_polices_pkgs:
      - ca-policy-egi-core
      - ca-policy-lcg

RPMs of CA polices to be installed

    grid_fetchcrl_options: []

Options for fetchcrl are passed as a hash. Following keys are possible.
-   agingtolerance: 24
-   nosymlinks: true
-   nowarnings: true
-   noerrors: false
-   http_proxy: <undef>
-   httptimeout: 30
-   parallelism: 4
-   logmode: syslog

Details for the parameters see [Nikhef Wiki](https://wiki.nikhef.nl/grid/FetchCRL3)

    grid_vos: []

A list of Virtual Organisations (VOs) to be configured. The detail of the configuration is
taken from the [EGI Operation Portal](https://operations-portal.egi.eu/)

    grid_host_certificate: {}

Install host certificate. The certificates is provided as hash
-   cert: path to host certificate
-   key: path to private host key. It should be secured with ansible-vault


## Example Playbook

Configuration for a server without CVMFS

    - hosts: servers
      roles:
        - name: grid
          vars:
            grid_vos:
              - cms
              - alice
              - belle
            grid_host_certificate:
              cert: server.crt
              key: server.key

Configuration for a worker node with CVMFS

    - hosts: workers
      roles:
        - name: grid
          vars:
            grid_vos:
              - cms
              - alice
              - belle
            grid_enable_certificates: cvmfs
        - role: cvmfs
        - role: grid_worker
          vars:
            grid_worker_role: wn

## License

MIT

## Author Information

Written by [Dietrich Liko](http://hephy.at/dliko) in May 2019

[Institute for High Energy Physics](http://www.hephy.at) of the
[Austrian Academy of Sciences](http://www.oeaw.ac.at)
