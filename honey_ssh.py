import socket
import threading
import logging
import argparse
from datetime import datetime

# --- SAFETY WARNING ---
# This script is a basic SSH honeypot for educational and research purposes ONLY.
# Running honeypots can have significant legal implications depending on your jurisdiction
# and how they are deployed. Always consult legal counsel before deploying any honeypot
# in a production environment or public-facing network.
# ENSURE THIS IS RUN IN A COMPLETELY ISOLATED ENVIRONMENT (e.g., dedicated VM, strict firewall).
# NEVER deploy this on systems with sensitive data or within your main network.
# --- SAFETY WARNING ---

# Configure logging
logging.basicConfig(filename='ssh_honeypot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def handle_client(client_socket, addr):
    """
    Handles an incoming client connection, simulates SSH interaction, and logs data.
    """
    client_ip, client_port = addr
    logging.info(f"Connection established from: {client_ip}:{client_port}")

    try:
        # Simulate SSH banner exchange
        ssh_banner = b"SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3
"
        client_socket.send(ssh_banner)

        # Log connection attempt
        logging.info(f"[{client_ip}] SSH banner sent.")

        # Simulate authentication
        client_socket.send(b"Username: ")
        username = client_socket.recv(1024).strip().decode('utf-8', errors='ignore')
        logging.info(f"[{client_ip}] Attempted Username: {username}")

        client_socket.send(b"Password: ")
        password = client_socket.recv(1024).strip().decode('utf-8', errors='ignore')
        logging.info(f"[{client_ip}] Attempted Password: {password}")

        # Simulate successful login (but no actual shell access)
        client_socket.send(b"Welcome to Ubuntu 18.04 LTS (GNU/Linux 4.15.0-72-generic x86_64)
")
        client_socket.send(b"Last login: " + str(datetime.now()).encode() + b" from " + client_ip.encode() + b"
")
        client_socket.send(b"This system is under restricted access.
")
        client_socket.send(b"You have no shell access.
")

        # Simulate a command prompt and log commands
        while True:
            client_socket.send(b"user@honeypot:~# ")
            command = client_socket.recv(1024).strip().decode('utf-8', errors='ignore')
            if not command:
                break
            logging.info(f"[{client_ip}] Command attempted: {command}")
            
            # Respond to common commands without executing them
            if command.lower() == 'exit' or command.lower() == 'quit':
                client_socket.send(b"Connection closed.
")
                break
            elif command.lower() == 'help':
                client_socket.send(b"Available commands: exit, quit, help (no actual execution).
")
            else:
                client_socket.send(b"Command not found or disallowed.
")

    except ConnectionResetError:
        logging.warning(f"[{client_ip}] Connection reset by peer.")
    except BrokenPipeError:
        logging.warning(f"[{client_ip}] Broken pipe error, client disconnected.")
    except Exception as e:
        logging.error(f"[{client_ip}] Error handling client: {e}")
    finally:
        client_socket.close()
        logging.info(f"Connection closed for {client_ip}:{client_port}")

def main():
    parser = argparse.ArgumentParser(description="Simple Python SSH Honeypot Logger.")
    parser.add_argument("--port", type=int, default=2222,
                        help="Port to listen on (default: 2222).")
    args = parser.parse_args()

    host = '0.0.0.0'  # Listen on all available interfaces
    port = args.port

    # Print prominent safety warning to console
    print("
" + "="*80)
    print("                 !!! HONEYPOT SAFETY WARNING !!!")
    print("================================================================================")
    print("This script is a basic SSH honeypot. It should ONLY be run in a COMPLETELY")
    print("ISOLATED ENVIRONMENT (e.g., dedicated VM, strict firewall rules) to prevent")
    print("any potential risks to your main network or sensitive systems.")
    print("DO NOT DEPLOY THIS ON PRODUCTION SYSTEMS OR NETWORKS WITH SENSITIVE DATA.")
    print("ALWAYS consult legal counsel regarding honeypot deployment in your jurisdiction.")
    print("================================================================================")
    print(f"Starting SSH honeypot on {host}:{port}. Logging to ssh_honeypot.log...")
    logging.info(f"Honeypot starting on {host}:{port}")

    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen(5)
        logging.info(f"Listening on {host}:{port}")

        while True:
            client_socket, addr = server_socket.accept()
            client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
            client_handler.start()

    except OSError as e:
        if e.errno == 98: # Address already in use
            logging.error(f"Port {port} is already in use. Please choose another port or stop the existing service.")
            print(f"Error: Port {port} is already in use. Please choose another port or stop the existing service.")
        elif e.errno == 13: # Permission denied
            logging.error(f"Permission denied to bind to port {port}. Try running with sudo if port is < 1024 (e.g., sudo python honey_ssh.py).")
            print(f"Error: Permission denied to bind to port {port}. Try running with sudo if port is < 1024.")
        else:
            logging.error(f"Socket error: {e}")
            print(f"Socket error: {e}")
    except KeyboardInterrupt:
        logging.info("Honeypot stopped by user (KeyboardInterrupt).")
        print("
Honeypot stopped.")
    except Exception as e:
        logging.critical(f"An unhandled error occurred in the main honeypot loop: {e}")
        print(f"An unhandled error occurred: {e}")
    finally:
        if 'server_socket' in locals() and server_socket:
            server_socket.close()
            logging.info("Server socket closed.")

if __name__ == "__main__":
    main()
