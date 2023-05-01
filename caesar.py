def encipher(p, k):
    c = ''
    for i in range(len(p)):
        a = ord(p[i])
        if a == 32: a = 64
        t = a + k
        if t > 90: t -= 27
        if t == 64: t = 32
        c += chr(t)
    return c

text = input("Enter the sentence to encrypt(uppercase only): ")
shift = int(input("Enter the location you want to move in the Caesar encrypt: "))

encrypt_text = encipher(text, shift)

print(encrypt_text)
