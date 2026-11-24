# Elastic Beanstalk Zero-Downtime Deployment Demo

A small Flask application for practicing application deployments on AWS Elastic
Beanstalk. The homepage displays the configured environment and version, and a
health endpoint is available for load balancer checks.

## Technology stack

- Python 3
- Flask
- Gunicorn
- HTML templates and CSS (no frontend framework)

## Project structure

```text
.
├── application.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Run locally on macOS

From the project directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python application.py
```

Open [http://localhost:5000](http://localhost:5000). To run with the same
production WSGI server used for deployment, run:

```bash
gunicorn --bind 0.0.0.0:5000 application:application
```

## Endpoints

| Path | Description |
| --- | --- |
| `/` | Deployment dashboard |
| `/health` | Health check returning `{"status": "healthy"}` with HTTP 200 |

## Configuration

The application reads these environment variables when it starts:

| Variable | Default | Description |
| --- | --- | --- |
| `APP_ENV` | `development` | Name of the current deployment environment |
| `APP_MESSAGE` | `Welcome to Elastic Beanstalk` | Homepage welcome message |
| `APP_VERSION` | `1.0` | Application version shown on the homepage |

For local development in macOS Terminal, set variables before starting the
application:

```bash
export APP_ENV=local
export APP_MESSAGE="Hello from my local environment"
export APP_VERSION=1.1
python application.py
```

To keep local values in a `.env` file, load them into the shell yourself before
launching the app (for example, with `set -a; source .env; set +a`). The app
does not require or load a `.env` file automatically.

On Elastic Beanstalk, set the same names under **Configuration → Updates,
monitoring, and logging → Runtime environment variables** in the AWS console,
or use the EB CLI:

```bash
eb setenv APP_ENV=production APP_MESSAGE="Welcome to Elastic Beanstalk" APP_VERSION=1.0
```

## Deploy to AWS Elastic Beanstalk

1. Install and configure the AWS CLI and EB CLI, then configure AWS credentials
   with permission to create Elastic Beanstalk resources. On macOS, one option
   for installing the EB CLI is `brew install awsebcli`.
2. From this project directory, initialize an Elastic Beanstalk Python
   application. Choose a currently supported Python platform version and your
   AWS region:

   ```bash
   eb init -p python-3.12 eb-zero-downtime --region us-east-1
   ```

3. Create a load-balanced environment (do not use the single-instance option):

   ```bash
   eb create eb-zero-downtime-env
   ```

4. Configure the environment variables using the console or `eb setenv`
   command above, then deploy:

   ```bash
   eb deploy
   eb open
   ```

5. In the Elastic Beanstalk environment's health-check settings, set the
   application health-check path to `/health`. For zero-downtime updates, use
   a load-balanced environment and select a rolling deployment policy (or
   rolling with an additional batch) in the environment's deployment settings.
   Verify the environment health before and after deployment.

Elastic Beanstalk uses `application.py` and its WSGI object named `application`
as the entry point. The `requirements.txt` file supplies Flask and Gunicorn;
no Docker configuration or database is required.
