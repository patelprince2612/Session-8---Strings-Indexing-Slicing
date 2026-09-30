# 3.
# Build a function reverse_message(message) that reverses any string passed to it,
# similar to how WhatsApp displays reversed text stickers.<br><br><em><strong>Constraint:</strong> 
# Do not use Python's built-in reversed() or [::-1] slicing shortcut.</em>

message = "Hello how Are YOu??"

for rev in range(len(message)-1,-1,-1):
    reve = message[rev]
    print(reve,end="")