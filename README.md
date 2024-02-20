# Installation
1. Do a git clone of the repository in your prefered directory.
2. In linux systems you can run the binary located in .../simple-encrypter/dist/encrypter/
3. In other systems you can just run the Python file "encrypter.py". You may need to install the `cryptocode` python library.

# Usage
When you run the programm it will show you a dialoge. You only have to follow the instructions. /n
NOTE: "password" is not stored anywhere, you must remember it or you won't be able to decrypt your data. 

# Example of use
```
~ ❯ encrypter                                                                                                     
Type 1 for encrypt or 2 for decrypt:1
Write the password:
test_password
Write the data you want to convert:
test_data
Encrypted data::
AZk1on5jsE5o*hKMqZi3WTOY7F+aAWgAO8Q==*tlmKFr/Xe8w9EBNvr3kKkQ==*b/sl6EkVakNUAf3TWcBmew==
~ ❯ encrypter                                                                                                 
Type 1 for encrypt or 2 for decrypt:2
Write the password:
test_password
Write the data you want to convert:
AZk1on5jsE5o*hKMqZi3WTOY7F+aAWgAO8Q==*tlmKFr/Xe8w9EBNvr3kKkQ==*b/sl6EkVakNUAf3TWcBmew==
Decrypted data:
test_data
```
