# ───────────────────────────────────────────────────────────────
# Caesar Cipher Tool | Prodigy Internship Task - 1
# Purpose : Encrypt/Decrypt text using Caesar Cipher Algorithm
# GitHub  : https://github.com/prajwal-sharmaa/Prodigy-task1-caesar-cipher
# # ───────────────────────────────────────────────────────────────

def caesar_cipher(text: str, shift: int, mode: str) -> str:
   
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = shift if mode == "encrypt" else -shift
            shifted = (ord(char) - base + offset) % 26
            result += chr(base + shifted)
        else:
            result += char

    return result


def banner():
    print("\n" + "=" * 50)
    print(" Caesar Cipher Encryption / Decryption Tool")
    print("=" * 50 + "\n")


def main():
    banner()
    try:
        message = input(" Enter your message       : ")
        shift = int(input(" Enter shift (1-25)       : "))
        mode = input("  Mode? [encrypt/decrypt] : ").strip().lower()

        if mode not in ["encrypt", "decrypt"]:
            print(" Invalid mode selected. Use 'encrypt' or 'decrypt'.")
            return

        result = caesar_cipher(message, shift, mode)
        print(f"\n Result ({mode.title()}ed): {result}")

    except ValueError:
        print("  Shift must be a number between 1 and 25.")
    except Exception as e:
        print(f" Unexpected Error: {e}")


if __name__ == "__main__":
    main()
