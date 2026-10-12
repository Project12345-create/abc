
import socket
import threading
import time
import sys

HOST = "127.0.0.1"

PORTS = {
    0: 5000,
    1: 5001,
    2: 5002,
    3: 5003
}

N = 4

pid = int(sys.argv[1])
next_process = (pid + 1) % N


def send_token():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORTS[next_process]))
            s.send("TOKEN".encode())
            s.close()

            print(
                f"Process {pid} passed TOKEN "
                f"to Process {next_process}\n"
            )
            break

        except:
            time.sleep(1)


def handle(conn):
    token = conn.recv(1024).decode()

    if token == "TOKEN":
        print(f"Process {pid} received TOKEN")

        choice = input("Enter Critical Section? (y/n): ")

        if choice.lower() == 'y':
            print(f"\nProcess {pid} ENTERED Critical Section")
            time.sleep(5)
            print(f"Process {pid} EXITED Critical Section\n")
        else:
            print(f"Process {pid} skipped Critical Section\n")
            time.sleep(1)

        send_token()

    conn.close()


def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORTS[pid]))
    s.listen()

    print(f"Process {pid} listening on Port {PORTS[pid]}")

    while True:
        conn, addr = s.accept()
        threading.Thread(
            target=handle,
            args=(conn,),
            daemon=True
        ).start()


threading.Thread(target=server, daemon=True).start()

time.sleep(2)

# Process 0 starts with the token
if pid == 0:
    print("\nProcess 0 initially has TOKEN")

    choice = input("Enter Critical Section? (y/n): ")

    if choice.lower() == 'y':
        print("\nProcess 0 ENTERED Critical Section")
        time.sleep(5)
        print("Process 0 EXITED Critical Section\n")

    send_token()

while True:
    time.sleep(1)
