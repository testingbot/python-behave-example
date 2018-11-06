from paver.easy import *
from paver.setuputils import setup
import multiprocessing

setup(
    name = "behave-testingbot",
    version = "0.1.0",
    author = "TestingBot",
    author_email = "info@testingbot.com",
    description = ("Behave Integration with TestingBot"),
    license = "MIT",
    keywords = "example selenium testingbot",
    url = "https://github.com/testingbot/python-behave-example",
    packages=['features']
)

def run_behave_test(config, feature, task_id=0):
    sh('CONFIG_FILE=config/%s.json TASK_ID=%s behave features/%s.feature' % (config, task_id, feature))

@task
@consume_nargs(1)
def run(args):
    if args[0] in ('single', 'local'):
        run_behave_test(args[0], args[0])
    else:
        jobs = []
        for i in range(4):
            p = multiprocessing.Process(target=run_behave_test, args=(args[0], "single", i))
            jobs.append(p)
            p.start()

@task
def test():
    sh("paver run single")
