import itertools
import pytest

testinfra_hosts = ['ansible://ovn']

hosts = ['ovn0', 'ovn1', 'ovn2']
targets = itertools.permutations(['ovn0', 'ovn1', 'ovn2'], 2)


@pytest.mark.parametrize('target', targets)
def test_services(host, hostname, target):
    if target[0] != hostname:
        pytest.skip('Port not realized on this host')
    else:
        with host.sudo():
            port = 'ovn-{}-0'.format(target[1])
            res = host.run(f'ovs-vsctl list port {port}')
            assert res.exit_status == 0
