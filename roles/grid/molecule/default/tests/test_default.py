from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os

import testinfra.utils.ansible_runner

import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
    '/etc/grid-security/hostcert.pem',
    '/etc/vomses/cms-lcg-voms2.cern.ch',
    '/etc/grid-security/vomsdir/cms/lcg-voms2.cern.ch.lsc',
    '/etc/yum.repos.d/UMD-4-updates.repo'
])
def test_files(host, name):
    f = host.file('/etc/hosts')

    assert f.exists


@pytest.mark.parametrize('name,version', [
    ('ca-policy-lcg', '1.'),
    ('fetch-crl', '3.0.'),
])
def test_packages(host, name, version):
    pkg = host.package(name)

    assert pkg.is_installed
    assert pkg.version.startswith(version)


def test_verify_ca(host):
    cmd = host.run('/usr/bin/openssl verify -CApath /etc/grid-security/certificates /etc/grid-security/hostcert.pem')  # noqa: E501

    assert cmd.rc == 0
