# grid [![Build Status](https://travis-ci.org/hephyvienna/ansible-role-grid.svg?branch=master)](https://travis-ci.org/hephyvienna/ansible-role-grid) [![Ansible Role](https://img.shields.io/ansible/role/40989.svg)](https://galaxy.ansible.com/hephyvienna/grid)

Ansible role for installation of grid repositories, certificates and voms definitions for WLCG/LCG site.

Inspired by the [Ansible Role UMD](https://github.com/EGI-Foundation/ansible-role-umd) by EGI-Foundation.

## Requirements

-   EL9
-   EPEL

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    grid_install_wlcg_repo: true

Install the [WLCG repository](http://linuxsoft.cern.ch/wlcg/) release package and GPG key.
Set to `false` when the repository is provided elsewhere (e.g. Satellite); the `wlcg-repo`
package is then removed (the GPG key is left in place).

    grid_install_umd_repo: true

Install the [UMD 5 repository](https://repository.egi.eu/sw/production/umd/) release package and GPG keys.
Set to `false` when the repository is provided elsewhere (e.g. Satellite); the `umd-release`
package is then removed (the GPG keys are left in place).

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

    grid_use_cvmfs_for_voms_certs: false

Use the VOMS configuration from the CVMFS repository grid.cern.ch instead of installing
the `wlcg-iam-vomses-*` and `wlcg-iam-lsc-*` RPMs. Sets `X509_VOMSES` and `X509_VOMS_DIR`
in `/etc/profile.d/voms.sh` and links `/etc/vomses` to the CVMFS copy, because
`voms-clients-java` ignores `X509_VOMSES`. Requires grid.cern.ch to be mounted.

    grid_host_certificate: {}

Install host certificate. The certificates is provided as hash
-   cert: path to host certificate
-   key: path to private host key. It should be secured with ansible-vault


## Task Entry Points

`main.yml` runs `install.yml` and then `configure.yml`. To install packages in an image
build and configure at first boot, run them separately with `tasks_from`:

-   `install.yml`: IGTF repository and CA packages, WLCG/UMD repositories, VOMS packages
    (`grid_vos`), `fetch-crl` and the `wn`/`ui` metapackage with HEP_OSlibs (`grid_node_type`).
    Starts no services.
-   `configure.yml`: fetch-crl configuration and timer, VOMS profile and `/etc/vomses` link
    (`grid_use_cvmfs_for_voms_certs`), host certificate.

Pass the same `grid_enable_fetch_crl`, `grid_use_cvmfs_for_voms_certs`, `grid_vos`,
`grid_node_type` and repository variables to both.

    - name: Install grid packages
      ansible.builtin.include_role:
        name: clip.grid.grid
        tasks_from: install.yml

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
