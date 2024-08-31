'''
https://projecteuler.net/problem=59

key is a triple with values ranging from 97-122
'''
import itertools

transform_text = lambda ciphered_text: "".join(chr(code) for code in ciphered_text)
uncipher_text = lambda key, ciphered_text: list(a^b for a, b in zip(itertools.cycle([ord(k) for k in list(key)]), ciphered_text))

abc = list("abcdefghijklmnopqrstuvwxyz")

with open("./0059_cipher.txt", "r") as file:
    ciphered_text = [int(code) for code in file.read().split(",")]
    for a in abc:
        for b in abc:
            for c in abc:
                key = a+b+c
                unciphered_text = uncipher_text(key, ciphered_text)
                transformed_text = transform_text(unciphered_text)
                if all(word in transformed_text for word in ["the", "and", "I", "or", "to", "have"]):
                    print(f"key: {key}")
                    print(transformed_text)
                    print("Solution: ", sum(unciphered_text))
                    break


