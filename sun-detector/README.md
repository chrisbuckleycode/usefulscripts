# Summary

- Downloads a webcam image
- Analyzes pixel density in a specified hue range looking for evidence of sunrise/sunset
- Runs continuously on an interval until operator interrupt (pressing Ctrl-C)

# Usage Reminder

```shell
$ git clone https://github.com/chrisbuckleycode/usefulscripts.git
$ cd usefulscripts/sun-detect
$ python3 -m venv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
$ python3 main.py
$ deactivate
```

# Notes
- You will need a source url of a static webcam jpg
- (hint, Google search for: "Index of /webcam" 2024 current)
- Increase the value of the threshold variable if you are getting false positive hits for sunrise/sunset
- Modify the hue range to better capture desired color: [chart](https://en.wikipedia.org/wiki/Hue#/media/File:HueScale.svg)
- Do not lower the interval too much or cam server may rate limit you!

# Future Ideas
- Calibrate variables for specific scenes
- Improve http error checking
