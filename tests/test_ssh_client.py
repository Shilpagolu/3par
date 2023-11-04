import logging
from my_ssh_client.ssh_client import SSHClient

logging.basicConfig(filename='test_log.txt', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def test_host_is_online(ssh_host, ssh_username, ssh_password):
    logging.info("Test: host is online")
    with SSHClient(ssh_host, ssh_username, ssh_password) as ssh:
        assert ssh.is_host_online()

def test_get_linux_version(ssh_host, ssh_username, ssh_password):
    logging.info("Test: get Linux version")
    with SSHClient(ssh_host, ssh_username, ssh_password) as ssh:
        version = ssh.get_linux_version()
        print(version)
        assert version is not None
