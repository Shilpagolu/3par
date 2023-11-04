from my_ssh_client.ssh_client import SSHClient

def main():
    host = 'first-cxo-node-4.vlab.nimblestorage.com'
    username = 'firstqa'
    password = 'Peach-05'

    # Create an SSH client and connect
    with SSHClient(host, username, password) as ssh:
        # Example: Run a command on the remote host
        result = ssh.run_command('ls -l')
        if result is not None:
            print("Command output:")
            print(result)
        else:
            print("Command execution failed.")

if __name__ == '__main__':
    main()
