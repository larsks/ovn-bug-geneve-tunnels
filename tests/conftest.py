import pytest

@pytest.fixture
def hostname(host):
    return host.backend.hostname
