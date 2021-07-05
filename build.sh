python3 -m venv venv
source venv/bin/activate

pip3 install pytest
pip3 install -U setuptools pip
pip3 install --user numpy
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
tar -xvzf geckodriver
chmod +x geckodriver
sudo mv geckodriver /usr/local/bin/
# chmod -R 777 ./ - provide permissions to directory

