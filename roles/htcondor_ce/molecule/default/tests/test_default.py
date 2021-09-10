from __future__ import absolute_import, division, print_function
__metaclass__ = type


import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package(host):
    host.package('condor').is_installed
    host.package('htcondor-ce').is_installed


@pytest.mark.parametrize('name', [
    'condor-ce',
    'condor-ce-apel.timer'
])
def test_service_running(host, name):
    ce = host.service(name)
    assert ce.is_enabled
    assert ce.is_running


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
