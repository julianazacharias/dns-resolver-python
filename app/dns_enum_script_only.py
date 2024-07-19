import dns.resolver
import sys

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

try:    
    domain = input('Type the domain: ')
    #domain = sys.argv[1]
except IndexError:
    print('Syntax error - python3 dns_enum.py domainname')

for records, name in record_types.items():
    try:
        answer = dns.resolver.resolve(domain, records)
        print(f'\n Record type = {records} : {name}')
        print('-' * 70)
        for server in answer:
            print(server.to_text())
    except dns.resolver.NoAnswer:
        pass
    except dns.resolver.NXDOMAIN:
        print(f'{domain} does not exist.')
        quit()
    except KeyboardInterrupt:
        print('Quitting.')
        quit()