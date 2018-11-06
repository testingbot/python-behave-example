from selenium import webdriver
import os, json

CONFIG_FILE = os.environ['CONFIG_FILE'] if 'CONFIG_FILE' in os.environ else 'config/single.json'
TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0

with open(CONFIG_FILE) as data_file:
    CONFIG = json.load(data_file)

TB_KEY = os.environ['TB_KEY'] if 'TB_KEY' in os.environ else CONFIG['key']
TB_SECRET = os.environ['TB_SECRET'] if 'TB_SECRET' in os.environ else CONFIG['secret']

def before_feature(context, feature):
    desired_capabilities = CONFIG['environments'][TASK_ID]

    for key in CONFIG["capabilities"]:
        if key not in desired_capabilities:
            desired_capabilities[key] = CONFIG["capabilities"][key]

    context.browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="https://%s:%s@hub.testingbot.com/wd/hub" % (TB_KEY, TB_SECRET)
    )

def after_feature(context, feature):
    context.browser.quit()
