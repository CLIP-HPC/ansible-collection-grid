from __future__ import absolute_import, division, print_function
__metaclass__ = type


import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package(host):
    pkg = host.package('cvmfs')

    assert pkg.is_installed


def test_file_on_cvmfs(host):
    path = '/cvmfs/cms.cern.ch/SITECONF/local/JobConfig/site-local-config.xml'
    f = host.file(path)

    assert f.exists
    assert f.user == 'cvmfs'
    assert f.group == 'cvmfs'
    assert f.contains('<site name="T2_AT_Vienna">')
