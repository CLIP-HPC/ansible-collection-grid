role-eosxd
=========

An ansible role to deploy and configure the eosfusex client on a node


Role Variables
--------------

`eosxd_mgmt_alias`: specifies the eos management host (required)

`eosxd_use_upstream_repos`: to use the upstream EOS repos to install eos-fusex; when false, the upstream repo files are removed (default: true)

`eosxd_fstab_state`: /etc/fstab entry for eos (default: "absent", possible values: present, mounted)

`eosxd_mount_point`: the mount point for eos when using the systemd (`eosxd_fstab`) service (default: /eos)

Task Entry Points
-----------------

`main.yml` runs `install.yml` and then `configure.yml`. To install packages in an image
build and configure at first boot, run them separately with `tasks_from`:

- `install.yml`: EOS repositories (`eosxd_use_upstream_repos`) and `eos-fusex`. Doesn't need `eosxd_mgmt_alias` and starts no services.
- `configure.yml`: `/etc/eos/fuse.eos.conf`, keytab and the `/etc/fstab` entry. Requires `eosxd_mgmt_alias`.

      - name: Install eos-fusex
        ansible.builtin.include_role:
          name: clip.grid.eosxd
          tasks_from: install.yml

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
