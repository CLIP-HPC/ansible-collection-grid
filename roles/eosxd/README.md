role-eosxd
=========

An ansible role to deploy and configure the eosfusex client on a node


Role Variables
--------------

`eosxd_mgmt_alias`: specifies the eos management host (required)

`eosxd_eos_upstream`: to use the upstream EOS repos to install eos-fusex (default: true)

`eosxd_fstab_state`: /etc/fstab entry for eos (default: "absent", possible values: present, mounted)

`eosxd_mount_point`: the mount point for eos when using the systemd (`eosxd_fstab`) service (default: /eos)

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: cluster
      roles:
        - role: clip.role.eosxd
          eosxd_mgmt_alias: eos.example.com

License
-------

BSD

Author Information
------------------

Uemit Seren <uemit.seren@gmi.oeaw.ac.at>
