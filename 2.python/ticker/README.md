# Summary

Crypto ticker (Bitcoin).

# Usage Reminder

```shell
$ git clone https://github.com/chrisbuckleycode/usefulscripts.git
$ cd usefulscripts/2.python/ticker
$ python3 -m venv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
$ python3 ticker.py
$ deactivate
```

To run in the background ("`&`") after exiting the terminal ("hanging up" i.e. "`nohup`"), activate venv as above then:
```shell
$ nohup python3 ticker.py &
```

# Notes
- Prices obtained from Coingecko API free tier.
- Price updates once every 30s to avoid rate limiting.

# Future Ideas
- Display 24hr % change.
- Self-contained binary

