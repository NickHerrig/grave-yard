
from flask import Flask, jsonify, request
from tcp_latency import measure_latency


app = Flask(__name__)

def latency(hosts, runs):
    hosts_list = []
    for host, port in hosts.items():
        keys = ['host','port','latencies']
        values = [host, port, measure_latency(host=host,port=port,runs=runs)]
        host_dict = { key:value for (key,value) in zip(keys,values)}
        hosts_list.append(host_dict)
    return hosts_list 
    
        
@app.route('/latency/v1.0',methods=['POST'])
def get_latency():
    if not request.json:
        return jsonify({'ERROR': 'Please ensure your body is JSON.'})
    hosts_latency =latency(hosts=request.json,runs=3)
    return jsonify(hosts_latency) 

if __name__ == '__main__':
    app.run(debug=True)
