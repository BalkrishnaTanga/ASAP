## Setting up

Install all the python dependencies

```
pip3 install -r requirements.txt
```

Install chrome driver (MacOS)

```
brew install cask chromedriver
```

Make sure that the chromedriver version installed is compatible with chrome version in your browser. Refer to the
chromedriver downloads page if the version installed by brew is incompatible. Download and unzip the version
into `/usr/local/bin/` or add symlink to the binary there

```
https://chromedriver.chromium.org/downloads
```

You might have to run the below command to prevent Mac from blocking chromedriver

```
cd /usr/local/Caskroom/chromedriver/103.0.5060.53
xattr -d com.apple.quarantine chromedriver
```

## Running the tests

```
behave tests/preview/preview.feature
```

## Setting up allure for reporting

1) Open powershell
2) run "Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')"
3) run "scoop install allure"