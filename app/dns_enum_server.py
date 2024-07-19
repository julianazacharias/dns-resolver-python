from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import dns.resolver

record_types = {
    'A': 'Host address',
    'AAAA': 'IPv6 host address',
    'NS': 'Name Server',
    'CNAME': 'Canonical name for an alias',
    'MX': 'Mail eXchange',
    'PTR': 'Pointer',
    'SOA': 'Start Of Authority',
    'SRV' : 'Location of service',
    'TXT': 'Descriptive text'
}

class DNSHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/resolve'):
            domain = self.path.split('=')[1].strip()

            results = {}
            for records, name in record_types.items():
                try:
                    answer = dns.resolver.resolve(domain, records)
                    results[name] = [server.to_text() for server in answer]
                except dns.resolver.NoAnswer:
                    results[name] = []
                except dns.resolver.NXDOMAIN:
                    results[name] = []

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET')
            self.send_header('Access-Control-Allow-Headers', 'Content-type')
            self.end_headers()
            self.wfile.write(bytes(json.dumps(results), 'utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes('Endpoint not found', 'utf-8'))

def run():
    print('Starting server...')

    server_address = ('', 8000)
    httpd = HTTPServer(server_address, DNSHandler)
    print('Server running on port 8000')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
