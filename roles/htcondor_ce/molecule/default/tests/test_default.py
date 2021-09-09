from __future__ import absolute_import, division, print_function
__metaclass__ = type


import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package(host):
    host.package('condor').is_installed
    host.package('htcondor-ce').is_installed


def test_service_running(host):
    ce = host.service('condor-ce')
    assert ce.is_enabled
    assert ce.is_running


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
