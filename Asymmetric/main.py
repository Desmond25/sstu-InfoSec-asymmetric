import rsa

# Чтение файла (сообщения, которое нужно зашифровать)
with open('message.txt', 'rb') as f:
    message = f.read() 

print("Сообщение: ")
print(message.decode('utf8'))

while True:
    print("\nВыберите действие:\n 1 - создание ключей\n 2 - шифрование сообщения\n 3 - расшифрование сообщения\n")
    action = input()

    if int(action) == 1:
        print("\nСоздание ключей...\n")

        # Генерация ключей
        (publicKey, privateKey) = rsa.newkeys(2048)

        # Сохранение ключей в формате PEM
        publicKey_pem = publicKey.save_pkcs1()
        privateKey_pem = privateKey.save_pkcs1()

        # Сохранение публичного ключа в формате .xml
        with open('publicKey.xml', 'wb') as f:
            f.write(publicKey_pem)

        # Сохранение приватного ключа в формате .xml
        with open('privateKey.xml', 'wb') as f:
            f.write(privateKey_pem)

        print("Ключи успешно созданы")


    elif int(action) == 2:
        print("\nШифрование сообщения:\n")
        print("Укажите путь до публичного ключа:")
        path = input()

        # Поиск публичного кюча
        with open("{}\{}".format(path, 'publicKey.xml'), 'rb') as f:
            publicKey = f.read()

        # Шифрование сообщения
        publicKey = rsa.PublicKey.load_pkcs1(publicKey)
        encryptedMessage = rsa.encrypt(message, publicKey)
        print(encryptedMessage)

        # Сохранение зашифрованного сообщения
        with open('encryptedMessage.txt', 'wb') as f:
            f.write(encryptedMessage)


    elif int(action) == 3:
        print("\nРасшифрование сообщения:\n")
        print("Укажите путь до приватного ключа:")
        path = input()

        # Поиск приватного кюча
        with open("{}\{}".format(path, 'privateKey.xml'), 'rb') as f:
            privateKey = f.read()

        # Поиск зашифрованного сообщения
        with open('encryptedMessage.txt', 'rb') as f:
            encryptedMessage = f.read() 

        # Расшифрование сообщения
        privateKey = rsa.PrivateKey.load_pkcs1(privateKey)
        decryptedMessage = rsa.decrypt(encryptedMessage, privateKey)
        print(decryptedMessage.decode('utf8'))

        # Сохранение зашифрованного сообщения
        with open('decryptedMessage.txt', 'wb') as f:
            f.write(decryptedMessage)

    else:
        print("Операция указана неверно")
        