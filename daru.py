import time
import threading
import sys

GREEN = '\033[1;92m'
RED = '\033[1;91m'
RESET = '\033[0m'

def print_daru_logo():
    logo = """

██████╗░░█████╗░██████╗░██╗░░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░░░██║
██║░░██║███████║██████╔╝██║░░░██║
██║░░██║██╔══██║██╔══██╗██║░░░██║
██████╔╝██║░░██║██║░░██║╚██████╔╝
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░
"""
    print(GREEN + logo + RESET)
    print(GREEN + "         TRICKS BY DARU\n" + RESET)

def execute_server():
    import http.server
    import socketserver

    class MyHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"   TRICKS BY DARU")

    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        httpd.serve_forever()

def send_initial_messages():
    # Dummy offline version: just simulate sending with print statements
    tokens = ["token1", "token2", "token3"]
    target_id = "61568797949037"
    print(GREEN + "[*] Sending initial messages (offline mode)..." + RESET)
    for token in tokens:
        print(f"[+] Would send initial message with token: {token} to ID: {target_id}")
        time.sleep(0.5)

def send_messages_loop():
    messages = ["Hello!", "How are you?", "This is Daru's offline server."]
    tokens = ["token1", "token2", "token3"]
    haters_name = "Daru"
    speed = 1
    print(GREEN + "[*] Starting offline message sending loop..." + RESET)

    while True:
        try:
            for i, message in enumerate(messages):
                token_index = i % len(tokens)
                full_msg = f"{haters_name} {message}"
                print(f"[+] Would send message {i+1} with token {token_index+1}: {full_msg}")
                time.sleep(speed)
            print(GREEN + "[*] Completed one offline cycle. Restarting..." + RESET)
        except KeyboardInterrupt:
            print(RED + "\n[!] Interrupted by user. Exiting..." + RESET)
            sys.exit(0)

def main():
    print_daru_logo()
    server_thread = threading.Thread(target=execute_server, daemon=True)
    server_thread.start()
    send_initial_messages()
    send_messages_loop()

if __name__ == '__main__':
    main()
