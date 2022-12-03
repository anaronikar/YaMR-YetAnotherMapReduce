import requests
import json
import numpy as np

def read_file(filename):
    metadata = json.loads(requests.post(f"http://127.0.0.1:8000/metadata").text)
    return "".join([read_file_from_worker(filename, port_) for port_ in metadata["ports"]])
    
def write_file(filename):
    metadata = json.loads(requests.post(f"http://127.0.0.1:8000/metadata").text)
    filecontents = open(filename, "r").readlines()
    parts = ["".join(list(d)) for d in np.array_split(filecontents, len(metadata["ports"]))]
    for i in range(len(parts)):
        write_file_to_worker(parts[i], filename, metadata["ports"][i])

def mapper_run(filename, mapperfile):
    metadata = json.loads(requests.post(f"http://127.0.0.1:8000/metadata").text)
    mapper_data = open(mapperfile, "r").read()
    for i in range(len(metadata["ports"])):
        run_mapper_in_worker(mapper_data, filename, metadata["ports"][i])

def reducer_run(filename, reducerfile):
    metadata = json.loads(requests.post(f"http://127.0.0.1:8000/metadata").text)
    reducer_data = open(reducerfile, "r").read()
    for i in range(len(metadata["ports"])):
        run_reducer_in_worker(reducer_data, filename, metadata["ports"][i])

def write_file_to_worker(filedata, filename, port):
    requests.post(f"http://127.0.0.1:{port}/write/{filename}", data = filedata)

def read_file_from_worker(filename, port):
    data = requests.post(f"http://127.0.0.1:{port}/read/{filename}")
    return data.text

def run_mapper_in_worker(data, filename, port):
    res = requests.post(f"http://127.0.0.1:{port}/map/{filename}", data = data)
    print(res.status_code)

def run_reducer_in_worker(data, filename, port):
    res = requests.post(f"http://127.0.0.1:{port}/reduce/{filename}", data = data)
    print(res.status_code)

input = "sample_input.txt"
mapper = "mapper.py"
reducer = "reducer.py"

write_file(input)
read_file(input)
mapper_run(input, mapper)
reducer_run(input, reducer)
