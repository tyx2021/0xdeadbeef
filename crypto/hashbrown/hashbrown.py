import time
import hashlib

def slow_hash(s):
    time.sleep(1)  # our state-of-the-art brute-forcing deterrer!!
    return hashlib.sha256(s.encode()).hexdigest()

def check_password(p):
    h = slow_hash(p)
    return slow_hash(p) == "64a1e1972b663b35a8c06b453ce018251efef00925fb414217f6087f179031b8"

def main():
    print("Brute forcing is too slow trust me")
    attempt = input("Enter password: ")
    if check_password(attempt):
        print("Nice job! Flag: CTF{REDACTED}")
    else:
        print("Wrong!")

if __name__ == "__main__":
    main()
