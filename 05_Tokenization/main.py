import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey there! my name is Jitesh Singh"

# Tokens  [25216, 1354, 0, 922, 1308, 382, 643, 3915, 71, 44807]
tokens =  enc.encode(text)

tokenGen = [25216, 1354, 0, 922, 1308, 382, 643, 3915, 71, 44807]

decodedToken = enc.decode(tokenGen)

print("Tokens ", tokens)
print("Decoded tokens ", decodedToken)