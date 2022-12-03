from flask import *
import sys
import os
app = Flask(__name__)
worker_count = 2
worker_ports = [8001 + i for i in range(worker_count)]
metadata = {"ports": worker_ports}
print(metadata)
if len(sys.argv) > 1:
    port = int(sys.argv[1])
    workerpath = str(port % 100)
else:
    port = 8000
    workerpath = "0"
print("in worker")
print(port)
if not os.path.exists(workerpath):
    os.mkdir(workerpath)
@app.route("/metadata", methods = ["GET", "POST"])
def writefile():
    global worker_ports
    return json.dumps(metadata)
app.run("0.0.0.0", port = port)
