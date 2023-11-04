import pytest

@pytest.fixture
def ssh_host():
    return "first-cxo-node-4.vlab.nimblestorage.com"

@pytest.fixture
def ssh_username():
    return "firstqa"

@pytest.fixture
def ssh_password():
    return "Peach-05"
