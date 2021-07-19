from __future__ import absolute_import, division, print_function
__metaclass__ = type


import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name, gid", [
    ("cms", 10000),
    ("cmsprd", 11000),
    ("cmspil", 12000),
    ("cmssgm", 13000),
])
def test_hosts_group(host, name, gid):
    g = host.group(name)

    assert g.exists
    assert g.gid == gid


@pytest.mark.parametrize("name, uid, group, groups", [
    ("cms001", 10000, 'cms', ['cms']),
    ("cms005", 10008, 'cms', ['cms']),
    ("cmsprd01", 11000, 'cmsprd', ['cmsprd', 'cms']),
    ("cmsprd02", 11002, 'cmsprd', ['cmsprd', 'cms']),
    ("cmspil01", 12000, 'cmspil', ['cmspil', 'cms']),
    ("cmspil02", 12002, 'cmspil', ['cmspil', 'cms']),
    ("cmssgm", 13000, 'cmssgm', ['cmssgm', 'cms']),
])
def test_hosts_user(host, name, uid, group, groups):
    u = host.user(name)

    assert u.exists
    assert u.uid == uid
    assert u.group == group
    assert u.groups == groups
