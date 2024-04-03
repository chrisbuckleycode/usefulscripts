# Summary

- Simple text box and submit button
- Submit single/multiline text
- Will appear on a BBS-style "graffiti wall" in chronological order, including timestamp

# Usage Reminder

```shell
$ git clone https://github.com/chrisbuckleycode/usefulscripts.git
$ cd usefulscripts/graffiti-wall
$ python3 -m venv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
$ python3 app.py
$ deactivate
$ rm -rf .env
```

# Remarks
- Flat file "database" is graffiti_wall.txt
- Tested successfully on pythonanywhere.com hosting
- Auth user/pass stored in plaintext. You should use environment variables/encryption/hashing for production

# Future Ideas
- Change messaging order to reverse chronological?
- Add colors, ANSI art to graffiti wall
- Improve auth
