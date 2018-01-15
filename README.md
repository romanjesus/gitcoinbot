# gitcoinbot

gitcoinbot for use with gitcoin.co

Make sure GITHUB_API_TOKEN is set as an environment variable

Installation:

virtualenv -p python3 gcoinbotenv

source gcoinbotenv/bin/activate

pip install -r requirements.txt

export GITHUB_API_USER and GITHUB_API_TOKEN for gitcoinbot to use to respond

run migrations

python manage.py migrate



Question?

Should gitcoinbot actions be recorded in the db?