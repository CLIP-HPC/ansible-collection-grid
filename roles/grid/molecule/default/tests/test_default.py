from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os

import testinfra.utils.ansible_runner

import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
    '/etc/grid-security/hostcert.pem',
    '/etc/yum.repos.d/UMD-4-updates.repo'
])
def test_files(host, name):
    f = host.file(name)
    assert f.exists


@pytest.mark.parametrize('vo', [
    'cms',
    'alice',
    'ops',
])
def test_voms_files(host, vo):
    # check LSC files
    lsc = '/etc/grid-security/vomsdir/%s' % vo
    assert host.file('%s/lcg-voms2.cern.ch.lsc' % lsc).exists
    assert host.file('%s/voms2.cern.ch.lsc' % lsc).exists
    if vo in ['cms', 'alice', 'atlas', 'lcb']:
        assert host.file('%s/voms-%s-auth.app.cern.ch.lsc' % (lsc, vo)).exists

    # check vomses files
    voms = '/etc/vomses'
    assert host.file('%s/%s-lcg-voms2.cern.ch' % (voms, vo)).exists
    assert host.file('%s/%s-voms2.cern.ch' % (voms, vo)).exists
    # activate check after 4th of October 2021
    # if vo in ['cms', 'alice', 'atlas', 'lcb']:
    #     f = host.file('%s/voms-%s-auth.app.cern.ch.vomses' % (voms, vo))
    #     assert f.exists


@pytest.mark.parametrize('name,version', [
    ('ca-policy-lcg', '1.'),
    ('fetch-crl', '3.0.'),
    ('wlcg-voms-alice', '1.'),
    ('wlcg-voms-cms', '1.'),
    ('wlcg-voms-ops', '1.'),
])
def test_packages(host, name, version):
    pkg = host.package(name)

    assert pkg.is_installed
    assert pkg.version.startswith(version)


def test_verify_ca(host):
    cmd = host.run('/usr/bin/openssl verify -CApath /etc/grid-security/certificates /etc/grid-security/hostcert.pem')  # noqa: E501

    assert cmd.rc == 0
