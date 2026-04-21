import os
import logging

# Function to generate a private key
import secrets


def generate_private_key():
    return secrets.token_hex(32)  # Generate a random 64 character hex string as a private key

# Setup the winners log
winners_log_path = 'winners.log'
if not os.path.exists(winners_log_path):
    with open(winners_log_path, 'w') as f:
        f.write('Address,PrivateKey,RecoveryPhrase,Balance,Timestamp\n')

# Example winner data
winner_address = 'sample_address'
private_key = generate_private_key()
recovery_phrase = 'sample_recovery_phrase'
balance = 100.0
timestamp = '2026-04-21 04:25:42'

# Log the winner
with open(winners_log_path, 'a') as f:
    f.write(f'{winner_address},{private_key},{recovery_phrase},{balance},{timestamp}\n')
