import os
import sys
from flowci import domain, client

def upload(path):
    api = client.Client()
    status = api.sendJobReport(
        path=path,
        name=domain.JobReportCodeCoverage,
        zipped="false",
        contentType=domain.ContentTypeHtml
    )

    print("[plugin-go-test]: upload go coverage report with status {}".format(status))

def stats():
    percent = sys.argv[1]
    percent = percent.rstrip('%')
    percent = (float(percent) / 100)

    body = {
        "type": "go-test",
        "data": {
            "coverage": percent
        }
    }

    api = client.Client()
    api.sendStatistic(body)
    pass


stats()

htmlFile = os.path.join(os.getcwd(), "ci-coverage.html")

if os.path.exists(htmlFile):
    upload(htmlFile)
else:
    print("[plugin-go-test]: cannot find html report file")


