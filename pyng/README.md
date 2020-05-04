# pyng
a python flask REST endpoint that determines latency between the host it's deployed to, and a list of supplied hosts.

## Example Curl Call
curl -i -H "Content-Type: application/json" -X POST -d '{"google.com":"443","app1.shallowbrookstudio.com":"443","app2.shallowbrookstudio.com":"443"}' http://localhost:5000/latency/v1.0
