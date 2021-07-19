from __future__ import absolute_import, division, print_function
__metaclass__ = type


import os

import testinfra.utils.ansible_runner

import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
    '/etc/grid-security/hostcert.pem',
    '/etc/grid-security/grid-mapfile',
    '/etc/grid-security/ban-voms-mapfile',
    '/etc/grid-security/ban-mapfile',
    '/etc/grid-security/gsi-authz.conf',
    '/etc/lcmaps/lcmaps.db'
])
def test_files(host, name):
    f = host.file(name)
    assert f.exists


@pytest.mark.parametrize('name,version', [
    ('globus-gridftp-server', '13.'),
    ('globus-gridftp-server-progs', '13.'),
    ('lcmaps', '1.'),
    ('lcmaps-plugins-voms', '1.'),
    ('lcmaps-plugins-verify-proxy', '1.')
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed
    assert pkg.version.startswith(version)


def test_verify_ca(host):
    cmd = host.run('/usr/bin/openssl verify -CApath /etc/grid-security/certificates -trusted /etc/grid-security/certificates/DummyCA.pem /etc/grid-security/hostcert.pem')  # noqa: E501
    assert cmd.rc == 0


@pytest.mark.parametrize('name', [
    'globus-gridftp-server',
])
def test_services(host, name):
    svc = host.service(name)
    assert svc.is_enabled
    assert svc.is_running
