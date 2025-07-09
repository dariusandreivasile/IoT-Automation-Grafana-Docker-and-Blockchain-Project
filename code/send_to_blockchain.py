from web3 import Web3
import json
import time

# === CONFIGURARE ===

ALCHEMY_URL = "https://eth-sepolia.g.alchemy.com/v2/keVks1H5dP8VDLm9W9C_-"
SENDER_ADDRESS = "0xC68B80Fd2021e3dff37b52b88c2ac4cc3159e577"
PRIVATE_KEY = "27a6c8c97599227f9a768fcc9d40a6f7f686ec9835d53af3b2df7304f1b16c72"

# === CONECTARE ===

web3 = Web3(Web3.HTTPProvider(ALCHEMY_URL))
if not web3.is_connected():
    print("❌ Eroare: Nu s-a putut conecta la Sepolia")
    exit()
print("✅ Conectat la Sepolia")

# Verificăm dacă cheia și adresa se potrivesc
derived_address = web3.eth.account.from_key(PRIVATE_KEY).address
if derived_address.lower() != SENDER_ADDRESS.lower():
    print("❌ Cheia privată nu corespunde cu adresa!")
    exit()
else:
    print("🔐 Cheia corespunde adresei:", derived_address)

# === CITIRE JSON ===

try:
    with open("latest_data.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("❌ Fișierul latest_data.json nu a fost găsit")
    exit()

# === CONVERSIE MESAJ ÎN HEX ===

message = json.dumps(data)
hex_data = web3.to_hex(text=message)

# === PREPARARE TRANZACȚIE ===

nonce = web3.eth.get_transaction_count(SENDER_ADDRESS, 'pending')
gas_price = web3.to_wei('20', 'gwei')  # mărim puțin

tx = {
    "nonce": nonce,
    "to": SENDER_ADDRESS,  # ne trimitem nouă înșine
    "value": 0,
    "gas": 100000,
    "gasPrice": gas_price,
    "data": hex_data
}

# === SEMNARE ȘI TRIMITERE ===

signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
print("🚀 Tranzacție trimisă. Așteptăm confirmare...")

# === AȘTEPTARE CONFIRMARE ===

tx_receipt = None
attempts = 0
while tx_receipt is None and attempts < 20:
    try:
        tx_receipt = web3.eth.get_transaction_receipt(tx_hash)
    except:
        time.sleep(5)
        attempts += 1

tx_url = f"https://sepolia.etherscan.io/tx/{web3.to_hex(tx_hash)}"
if tx_receipt:
    print("✅ Confirmată pe blockchain.")
    print("🔗 Verifică aici:", tx_url)
else:
    print("⚠️ Tranzacția încă nu este confirmată.")
    print("🔗 Verifică manual:", tx_url)
