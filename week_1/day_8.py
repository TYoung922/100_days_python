alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def start():
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message = input("Type your message:\n").lower()
    offset_let = input("Type the shift number:\n")
    if choice == "encode":
        encode(message, offset_let)
    elif choice == "decode":
        decode(message, offset_let)
    else:
        print(f"Whoops your input {choice} didn't make sense")


def encode(mes, num):
    set_message = list(mes)
    set_index = []
    encoded_message = []
    for let in set_message:
        if let in alphabet:
            set_index.append(alphabet.index(let))
    for ind in set_index:
        new_ind = ind + int(num)
        if new_ind < len(alphabet):
            encoded_message.append(alphabet[new_ind])
        else:
            adjust = (new_ind - len(alphabet))
            # print(len(alphabet))
            # print(set_index)
            # print(new_ind)
            # print(adjust)
            encoded_message.append(alphabet[adjust])
    print("Here's the encoded result:", ''.join(encoded_message))
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if again == 'yes':
        start()
    else:
        print("Goodbye")

def decode(mes, num):
    set_message = list(mes)
    set_index = []
    encoded_message = []
    for let in set_message:
        if let in alphabet:
            set_index.append(alphabet.index(let))
    for ind in set_index:
        new_ind = ind - int(num)
        if new_ind >= 0:
            encoded_message.append(alphabet[new_ind])
        else:
            adjust = (new_ind + len(alphabet))
            # print(len(alphabet))
            # print(set_index)
            # print(new_ind)
            # print(adjust)
            encoded_message.append(alphabet[adjust])
    print("Here's the encoded result:", ''.join(encoded_message))
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if again == 'yes':
        start()
    else:
        print("Goodbye")

start()
