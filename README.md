# Delete tweets

Delete tweets (or just replies or retweets) from your timeline, including tweets beyond the [3,200 tweet limit](https://dev.twitter.com/discussions/276).

## Dependencies
* python-twitter (`pip install python-twitter`)
* python-dateutil (`pip install python-dateutil`)

## Setup
1. Create a new Twitter app at https://apps.twitter.com/
2. Get the API key and secret of the app, and assign it to `API_KEY` and `API_SECRET` respectively
3. Generate the access token and secret, and assign it to `ACCESS_TOKEN` and `ACCESS_TOKEN_SECRET` respectively
4. Set the permissions of your app to *Read and Write*
5. Request the Twitter archive at https://twitter.com/settings/account
6. Replace *tweets.csv* with the CSV file from the requested Twitter archive

## Usage
* Update `main` method include Twitter app credentials
* Include any additional arguments for `delete` method
    * `date="2019-11-01"`
    * `restrict="retweet"`
* Run `python delete_tweets.py`
