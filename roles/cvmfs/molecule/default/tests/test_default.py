from __future__ import absolute_import, division, print_function
__metaclass__ = type


import os
import pytest

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


@pytest.mark.parametrize("folder", [
    "cms.cern.ch",
    "data.galaxyproject.org",
    "singularity.galaxyproject.org"
])
def test_cvmfs_probe(host, folder):
    f = host.file(f"/cvmfs/{folder}")
    assert f.exists
    assert f.is_directory
    assert len(f.listdir()) > 0
