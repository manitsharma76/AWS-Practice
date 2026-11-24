import os

from flask import Flask, jsonify, render_template_string

application = Flask(__name__)

APP_ENV = os.environ.get("APP_ENV", "development")
APP_MESSAGE = os.environ.get("APP_MESSAGE", "Welcome to Elastic Beanstalk")
APP_VERSION = os.environ.get("APP_VERSION", "1.0")

HOME_PAGE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Elastic Beanstalk Deployment Demo</title>
    <style>
        :root {
            color-scheme: dark;
            font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI",
                sans-serif;
            background: #0b1110;
            color: #eef4f1;
        }

        * { box-sizing: border-box; }

        body {
            margin: 0;
            min-height: 100vh;
            background:
                radial-gradient(ellipse at 50% 0, #18332a 0, transparent 48%),
                #0b1110;
        }

        main {
            width: min(920px, calc(100% - 40px));
            margin: 0 auto;
            padding: 72px 0;
        }

        .eyebrow {
            color: #86d9a1;
            font-size: 0.76rem;
            font-weight: 700;
            letter-spacing: 0.14em;
            text-transform: uppercase;
        }

        h1 {
            margin: 14px 0 12px;
            font-size: clamp(2.2rem, 6vw, 3.6rem);
            letter-spacing: -0.045em;
            line-height: 1.08;
        }

        .intro {
            max-width: 600px;
            color: #a7b6af;
            font-size: 1.08rem;
            line-height: 1.7;
        }

        .status-banner {
            display: flex;
            align-items: center;
            gap: 12px;
            margin: 34px 0 20px;
            padding: 16px 18px;
            border: 1px solid #28583b;
            border-radius: 12px;
            background: #10251a;
            color: #a7efba;
            font-weight: 650;
        }

        .status-dot {
            width: 10px;
            height: 10px;
            flex: 0 0 auto;
            border-radius: 50%;
            background: #52d47c;
            box-shadow: 0 0 14px #52d47c88;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 16px;
        }

        .card {
            min-height: 136px;
            padding: 22px;
            border: 1px solid #25312c;
            border-radius: 14px;
            background: #111a16;
        }

        .card-label {
            color: #93a49b;
            font-size: 0.84rem;
        }

        .card-value {
            display: block;
            margin-top: 16px;
            color: #f0f7f3;
            font-size: 1.35rem;
            font-weight: 650;
            overflow-wrap: anywhere;
        }

        .card-value.healthy { color: #86d9a1; }

        .footer {
            margin-top: 30px;
            color: #718078;
            font-size: 0.85rem;
        }

        @media (max-width: 640px) {
            main { padding: 48px 0; }
            .cards { grid-template-columns: 1fr; }
            .card { min-height: 112px; }
        }
    </style>
</head>
<body>
    <main>
        <div class="eyebrow">AWS Elastic Beanstalk</div>
        <h1>Elastic Beanstalk<br>Deployment Demo</h1>
        <p class="intro">{{ message }}</p>

        <div class="status-banner">
            <span class="status-dot" aria-hidden="true"></span>
            <span>Deployment successful</span>
        </div>

        <section class="cards" aria-label="Deployment details">
            <article class="card">
                <span class="card-label">Environment</span>
                <strong class="card-value">{{ environment }}</strong>
            </article>
            <article class="card">
                <span class="card-label">Application version</span>
                <strong class="card-value">{{ version }}</strong>
            </article>
            <article class="card">
                <span class="card-label">Application status</span>
                <strong class="card-value healthy">Healthy</strong>
            </article>
        </section>

        <p class="footer">A simple Flask app, ready to deploy.</p>
    </main>
</body>
</html>
"""


@application.route("/")
def home():
    return render_template_string(
        HOME_PAGE,
        message=APP_MESSAGE,
        environment=APP_ENV,
        version=APP_VERSION,
    )


@application.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)
