# Ansible Collection: clip.grid

This repo hosts the `clip.grid` Ansible Collection.

The collection includes the roles and playbooks to provision the GRID services for the VBC Cern Tier2 site.

## Installation and Usage

Before using the `clip.grid` collection, you need to install the collection with the `ansible-galaxy` CLI:

`ansible-galaxy collection install vbc.grid`

You can also include it in a `requirements.yml` file and install it through `ansible-galaxy collection install -r requirements.yml` using the format:

```yaml
collections:
- name: clip.grid
```

## Roles

Following roles are supported:

- [cvmfs](roles/cvmfs): Install & configure cvmfs fuse mount
- [eosxd](roles/eosxd): Install & configure eos fusex client
- [grid](roles/grid): Basic role for GRID configuration
- [gridftp](roles/gridftp): Install & configure GridFTP server
- [htcondor_ce](roles/htcondor_ce): Install & configure HTCondor-CE
- [poolaccounts](roles/poolaccounts): Configure poolaccounts
- [vobox](roles/vobox): Install & configure a VOBOX

## Playbooks

Following playbooks will use the above roles to setup the GRID services

- [alien.yml](playbooks/alien.yml): Configure an ALiEN VOBOX
- [apel.yml](plaubooks/apel.yml): Configure APEL accounting
- [ce.yml](playbooks/ce.yml): Configure a Compute Element (CE) using HTCondor-CE
- [gridftp.yml](playbooks/gridftp.yml): Configure a GridFTP server
