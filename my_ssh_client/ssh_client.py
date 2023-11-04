import paramiko
import logging

# Configure logging settings
logging.basicConfig(filename='ssh_client.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SSHClient:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.client = None

    def __enter__(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.host, username=self.username, password=self.password)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.client:
            self.client.close()

    def execute_command(self, command):
        if self.client:
            try:
                stdin, stdout, stderr = self.client.exec_command(command)
                result = stdout.read().decode('utf-8')
                logger.debug(f"Command executed: {command}")
                logger.debug(f"Command output: {result}")
                return result
            except Exception as e:
                logger.error(f"Error executing command: {command}")
                logger.error(str(e))

    def is_host_online(self):
        # Ping the host to check if it's online
        response = self.execute_command("ping -c 1 " + self.host)
        return "1 packets transmitted, 1 received" in response

    def get_linux_version(self):
        # Get the Linux version
        return self.execute_command("show version")
