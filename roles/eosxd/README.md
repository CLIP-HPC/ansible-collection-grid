role-eosxd
=========

An ansible role to deploy and configure the eosfusex client on a node


Role Variables
--------------

`role_eosxd_mgmt_alias`: specifies the eos management host (required)

`role_eosxd_eos_upstream`: to use the upstream EOS repos to install eos-fusex (default: true)

`role_eosxd_epel_upstream`: to use the upstream EPEL repos for dependencies (default: true)

`role_eosxd_fstab_state`: /etc/fstab entry for eos (default: "absent", possible values: present, mounted)

`role_eosxd_mount_point`: the mount point for eos when using the systemd (`role_eosxd_fstab`) service (default: /eos)

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: cluster
      roles:
        - role: role-eosxd
          role_eosxd_mgmt_alias: eos.example.com

License
-------

BSD

Author Information
------------------

Uemit Seren <uemit.seren@gmi.oeaw.ac.at>
