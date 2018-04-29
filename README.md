# EPMG

Entropic Password Manager Generator

![](https://pbs.twimg.com/media/DGAT61MXsAAeaDo.jpg)

EPMG is a cross-platform, most secure and storageless password manager that generates passwords

The main code is for the offline version, but you can also use it <a href="https://cryptolok.github.io/EPMG" target="_blank">online</a> safely.

Properties:
* security
* portability
* compatibility
* minimalism
* resilience
* versatility
* deniability

Dependencies:
* **Python** - main offline engine, version 2 and 3 compatible
* **JavaScript** - main online engine, Firefox or Chrome/Edge (limited loader/clipboard) required, IE isn't compatible

Limitations:
* no automatic clipboard copy for Android/iOS
* no proper RAM cleaning
* may take several seconds to compute on some devices
* static password policy
* impossibility to store unpredictable constants
* master-password compromise is fatal

## How it works

The solution allows to generate a service-specific password using only one single master-password.

1. ask for service/website/application/filename
2. ask for login/id/username/email
	* Because, there might be multiple accounts for one service.
3. ask for master-password/key/passphrase
	* This password should always be the same, but strong and unqiue, it allows multiple and deterministic generation.
4. ask how many times the generated password was compromised
	* If the master-password was compromised, every generated password is.
	* However, if one of the generated passwords was compromised, adding the compromission number as a salt will generate a totally different and independent password.
5. calculate PBKDF2-HMAC ( SHA-512, 1 000 000 iterations, service and login, password and compromises number )
	* PBKDF is a strong cryptographic function, combined with a strong and difficult to compute hashing algorithm as SHA-512 for one million times will make it extremely hard to bruteforce for an adversary of any type.
	* PBKDF is more secure than HMAC, which is more secure than a simple hash.
	* As you can see, the password with compromission number is actually used as salt and the actual "password" comes from concatenation of service and login.
6. encode the result in Base64
	* This will output ASCII characters
7. select first 16 characters
	* Because, it's enough
8. add "/0" at the end
	* This is preferable because, the propability of occurence for special characters and numbers is lower than letters, whereas it's necessary for the current password policy (regardless the fact that it has nothing to do with the password security).
9. copy to clipboard or show the generated password

INPUT  : service, login, master-password

OUTPUT : pseudo-randomly generated 18 ASCII characters

### HowTo

First of all, it's available <a href="https://cryptolok.github.io/EPMG" target="_blank">online</a>, but you can also install it locally.

For Unix :
```bash
sudo apt install python || echo 'you know how to install a package, right?'
python EPMG.py || chmod +x EPMG.py && ./EPMG.py
```
If using Python 3 you will also need Tkinter library (which is included in Python 2):
```bash
sudo apt install python3-tk
```

For Windows - [installer2.msi](https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi) or [installer3.msi](https://www.python.org/ftp/python/3.4.2/python-3.4.2.msi)

For Android :
1. Download [QPython2](https://play.google.com/store/apps/details?id=org.qpython.qpy) or [QPython3](https://play.google.com/store/apps/details?id=org.qpython.qpy3)
2. Move EPMG.py to /storage/qpython/scripts/ or ../scripts3/
3. Launch QPython
4. Click on "quick launch" central logo icon
5. Select "Run local script"
6. Select "EPMG.py"
7. Tap press on screen and choose "Select text"
8. Select the password using your finger, this will copy it to the clipboard
9. Press "enter" to exit

For iOS - [iTunes2](https://itunes.apple.com/us/app/python-for-ios/id485729872) or [iTunes3](https://itunes.apple.com/us/app/python-3.2-for-ios/id519319292?mt=8&ign-mpt=uo%3D4), which is paid, but you can find a free version "somewhere in a galaxy"

Examples:
```bash
./EPMG.py
IN : socialNetwork
IN : secured@mail.net
IN (no prompt) : MyStrong&UNIQUEp4$$w0rd
IN : "enter"
OUT (clipboard) : pcRZGsaE26SL6zNT/0

./EPMG.py
IN : mail.net
IN : secured
IN (no prompt) : MyStrong&UNIQUEp4$$w0rd
IN : 1
IN : SHOW
OUT: UngPtVcR9IJ+gxX+/0
```

#### Analysis

At the current date, password is the most common form of authentication, even if some services support multiple authentication types, passwords are still remaining universal.

The code is written in Python (2 and 3 compatible) and even smaller than this README, which makes it executable on almost any device.

The online version is HTML/JavaScript, even if it uses an external library and an image, the execution is stricly limited to the browser and no data will leave it.

[PBKDF](http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-132.pdf) itself is very difficult to bruteforce and practically impossible to make a dictionary/table. I maid it even more secure that your disk encryption and the password managers all together.

Nothing is saved anywhere. The RAM (volatile memory) is exception ofcourse and even if Python has "garbadge collection" it has no C-type control over variables and it makes some copies of them anyway, thus making it almost impossible task to be sure that nothing remains in memory after execution. Nevertheless, compromised passwords can be changed and RAM leaking is pretty irrealistic problem for modern computers. Zero connection prevents network attacks and has less dependencies.

It can also be executed in a different environment (like friend's PC or virtual machine), which should be trusted however.

In case if you're forced to decrypt your drive for instance, all your stored passwords will be compromised and if you've encrypted them, a key might be demanded. A deterministic schema allows deniability in such case by simply denying having a password for a service or by providing a fake-one.

Despite the [criticism](https://tonyarcieri.com/4-fatal-flaws-in-deterministic-password-managers) of deterministic password managers, secuirty policies were somehow stabilized and you can strip/recode the "improper" characters (at the cost of user experience). Anyway, user will end up with some local storage files (certificates, PINs, ...).

Finally, like all my software, it's free and has no "premium" discrimination.

#### Mathematics

Since we add 2 characters in the end, they woun't count for complexity.

We are left with 16 "random" characters selected out of Base64, so 64 possibilities for each-one, which gives us:

64^16 = 10^28 possibilities <=> log(64^16) in base of 2 = 96 random bits of entropy to guess theoretically, which is more than enough.

However, practically the total number of possibilities can be reduced to 10^3 * 26^13 * binom(13,7) = 10^24 <=> 82 bits, because of statistics.

The probability of occurence in Base64 charset for:
* decimals is 10/64 = 15%
* lowercase characters is 26/64 = 41%
* uppercase characters is 26/64 = 41%
* special chars is 2/64 = 3% => neglected

Taking in count that I took only 16 characters, only 3 of them will be decimals and 13 are the alphabet characters, which can be lower or uppercase with no order importance.

This brings us to combinatorics, more specifically binomial coefficients and factorials.

Assuming that there will be half of uppercase and half of lowercase characters, n is total characters number (13) and k in the ratio of inter-charset occurence probability (13/2 = 6), the total number of possibilities for them is:

![factorial notation](https://wikimedia.org/api/rest_v1/media/math/render/svg/3ddcd034186417e2cb2c00fbb8d14a05901de8a9)

which is equivalent to

![multiplicative notation](https://wikimedia.org/api/rest_v1/media/math/render/svg/d4145e0326f57f563b59c943642928342a5a6b18)

which equals 1716

An interesting conclusion is that the more charsets you use in your password, the less secure it is...

##### Notes

Password managers are insecure and hardly usable, just like passwords themself.

This solution isn't a proposition to change something and the idea is pretty old, but it can still be used for "special" purposes or just by paranoids/cypherpunks.

If you ask me what do I use for passwords, I'll say Firefox and manually encrypted files, plus some esoteric solutions that I might publish soon.

We need new meanings of authentication, for more info read my [research paper](http://goo.gl/giXPzC).

> "Cryptography began in mathematics."

James Sanborn
