from flask import *
import sys
import subprocess
import os
app = Flask(__name__)
if len(sys.argv) > 1:
    port = int(sys.argv[1])
    workerpath = str(port % 100)
else:
    port = 8001
    workerpath = "0"
print("in worker")
print(port)
if not os.path.exists(workerpath):
    os.mkdir(workerpath)
os.chdir(workerpath)
@app.route("/write/<filename>", methods = ["GET", "POST"])
def write(filename):
    global workerpath
    open(os.path.join(filename), "wb").write(request.data)
    return "Done"

@app.route("/read/<filename>", methods = ["GET", "POST"])
def read(filename):
    global workerpath
    return open(os.path.join(filename), "r").read()

@app.route("/map/<filename>", methods = ["GET", "POST"])
def map(filename):
    global workerpath
    open("temp_mapper.py", "wb").write(request.data)
    subprocess.run(["python", "temp_mapper.py"], stdin = open(filename, "r"), stdout = open(filename + "_mapout", "w"))
    return "done"

@app.route("/reduce/<filename>", methods = ["GET", "POST"])
def reduce(filename):
    global workerpath
    open("temp_reducer.py", "wb").write(request.data)
    subprocess.run(["python", "temp_reducer.py"], stdin = open(filename + "_mapout", "r"), stdout = open(filename + "_redout", "w"))
    return "done"

app.run("0.0.0.0", port = port)
