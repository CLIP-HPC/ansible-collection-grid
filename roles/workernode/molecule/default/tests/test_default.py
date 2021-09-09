from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages_wn(host):

    rel = host.system_info.release
    assert rel[:2] in ['6.', '7.']

    if rel.startswith('7'):
        name = 'wn'
        vers = '4.0.'
    else:
        name = 'emi-wn'
        vers = '3.1.'

    pkg = host.package(name)
    assert pkg.is_installed
    assert pkg.version.startswith(vers)


def test_packages_hepos_lib(host):

    rel = host.system_info.release
    assert rel[:2] in ['6.', '7.']

    if rel.startswith('7'):
        name = 'HEP_OSlibs'
        vers = '7.3.'
    else:
        name = 'HEP_OSlibs_SL6'
        vers = '3.1.'

    pkg = host.package(name)
    assert pkg.is_installed
    assert pkg.version.startswith(vers)


@pytest.mark.parametrize('name', [
    ('/etc/profile.d/gridenv.sh'),
])
def test_files(host, name):
    pkg = host.file(name)
    assert pkg.exists
