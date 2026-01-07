from model import predict

msg = input("Digite a mensagem: ")

result = predict(msg)

if result == 1:
    print("SPAM")
else:
    print("MENSAGEM NORMAL")
