# crypton_ctf

A beginner-to-intermediate level Capture The Flag (CTF) cryptography challenge set. Each challenge hides a flag using a classic or fundamental cryptographic technique.

## Challenge List

### Easy Challenges

1. **Digital Camouflage** (100 points)
   - File: `challenges/camouflage.txt`
   - Hidden using Base64 encoding.
2. **Mirror Mirror** (100 points)
   - File: `challenges/mirror.txt`
   - The flag is reversed.
3. **Emperor's Message** (150 points)
   - File: `challenges/emperor.txt`
   - Encrypted with ROT13 (Caesar cipher).

### Intermediate Challenges

4. **Binary Warrior** (200 points)
   - File: `challenges/warrior.txt`
   - XORed with a single-byte key (0x13).
5. **Historical Cipher** (250 points)
   - File: `challenges/historical.txt`
   - Encrypted with Vigenère cipher (key: "CIPHER").
6. **Prime Time** (300 points)
   - File: `challenges/prime.txt`
   - RSA-encrypted (small primes, n=3233, e=17).

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd crypton_CFT
   ```
2. **Generate challenge files (if needed):**
   ```bash
   python generate_challenges.py
   # or
   python generate_all_challenges.py
   ```
   This will create files in the `challenges/` directory.

3. **Solve the challenges:**
   - Open each file in `challenges/` and try to recover the flag using the described technique.
   - Hints are available in `hints.txt`.

4. **Verify your solutions:**
   - Use `solve.py` to check your answers or see example solution code for each challenge type.

## Hints

Hints for each challenge are provided in `hints.txt`. Reveal them progressively to participants as needed.

## Challenge Descriptions

See `challenges.md` for full challenge descriptions, point values, and hints.

## Adding New Challenges

- Each challenge has a corresponding Python file (e.g., `challenge1_base64.py`).
- To add a new challenge, follow the structure in these files and update the generator scripts.

## License

MIT License
