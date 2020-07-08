# Bearer Onboarding Python

This sample application allows you to try out [Bearer](https://bearer.sh) before installing it in your application. To get started, you will need:

- An account on Bearer ([Sign up here](http://app.bearer.sh/signup))
- Your Bearer App Key, found [here in the settings](https://app.bearer.sh/settings/general).
- Python 3.7+

## Installation

First, clone this repo.

```shell
# Clone the app
git clone https://github.com/Bearer/onboarding-python.git
```

Next, navigate to the newly created directory.

```shell
# Change directory
cd onboarding-python
```

Finally, run `pip` to install the dependencies.

```bash
pip install -r requirements.txt
```

## Running the application

To start the application, run the following command and replace the `XXXX` with your Bearer App Key.

```bash
BEARER_SECRET_KEY='XXXX' python init.py
```

## Viewing the results

Once the application has finished running, you can view the results by visiting the [dashboard](https://app.bearer.sh).

To get started with Bearer in your own application, check our or [Ruby Agent Documentation](https://ruby.docs.bearer.sh/).

If you need any help along the way, you can get support at our [Help Center](https://support.bearer.sh) or by clicking the Intercom button directly in the dashboard.
