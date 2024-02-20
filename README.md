# Installation
1. Do a git clone of the repository in your prefered directory.
2. In linux systems you can run the binary located in `/simple-encrypter/dist/`
3. In other systems you can just run the Python file "encrypter.py". You may need to install the `cryptocode` python library.

# Modification 
1. If you want to modify whatever you want you should do it in the `encrypter.py` file.
2. If you want to make a binary you can do it with the `pyinstall` python utility. 

# Usage
When you run the programm it will show you a dialoge. You only have to follow the instructions.\
NOTE: "password" is not stored anywhere. You must remember it or you won't be able to decrypt your data. 

# Usage as a system programm
Make a symbolic link of the executable inside `dist/` folder to `/usr/local/bin`. 

# Tested Linux distributions
- Arch Linux.

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
