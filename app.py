from flask import Flask, render_template
import datetime, random

app = Flask(__name__)

@app.route('/')
def dashboard():
    build_status = random.choice(["✅ Success", "❌ Failed"])
    uptime = f"{random.randint(99, 100)}.{random.randint(0,9)}%"
    version = "v1.0.3"
    commit_id = "abc1234"
    last_deploy = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", build_status=build_status,
                           uptime=uptime, version=version,
                           commit_id=commit_id, last_deploy=last_deploy)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
