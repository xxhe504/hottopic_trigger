#!/usr/bin/env python
# coding: utf-8

# # trigger
# 触发hottopic项目的workflow  
# 260623: 创建  

import requests
import os


def handler(event, context):
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
    USER_NAME = "xxhe504"
    REPO_NAME = "hottopic"
    WORKFLOW_FILE = "run_wb_hottopic.yaml"
    BRANCH = "main"

    print('开始调度GitHub Workflow')
    url = f"https://api.github.com/repos/{USER_NAME}/{REPO_NAME}/actions/workflows/{WORKFLOW_FILE}/dispatches"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }

    # 发送POST请求触发Workflow
    try:
        print(f"请求地址: {url}")
        response = requests.post(url, headers=headers, json={"ref": BRANCH})
        if response.status_code in [204, 200]:
            return {"code": 0, "msg": "触发成功", "status_code": response.status_code}
        else:
            return {"code": -1, "msg": "触发失败", "status_code": response.status_code, "error": response.text}
    except Exception as e:
        return {"code": -2, "msg": "请求异常", "error": str(e)}


if __name__ == '__main__':
    res = handler(None, None)
    print(res)


#!jupyter nbconvert --to python --no-prompt --TemplateExporter.exclude_input_prompt=True --TemplateExporter.exclude_output_prompt=True  trigger.ipynb

