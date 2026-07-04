from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/trigger', methods=['GET', 'POST'])
def trigger():
    token = os.environ.get("GITHUB_TOKEN")
    user = "xxhe504"
    repo = "hottopic"
    workflow = "run_wb_hottopic.yaml"

    url = f"https://api.github.com/repos/{user}/{repo}/actions/workflows/{workflow}/dispatches"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    resp = requests.post(url, headers=headers, json={"ref": "main"})

    if resp.status_code == 204:
        # 极简返回，也可以直接 return "ok", 200
        return {"ok": True, "msg": "trigger success"}
    else:
        # 只返回状态码，抛弃长error文本
        return {
            "ok": False,
            "code": resp.status_code,
            "msg": "github dispatch failed"
        }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    