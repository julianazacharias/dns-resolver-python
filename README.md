# DNS Resolver

This is a Python-based domain resolver tool that helps resolve domain names to their corresponding IP addresses. It can be used to quickly retrieve the IP addresses associated with various domains.

## Features

- Enumerate real world domains.
- Identify real world subdomains.
- Simple and easy-to-use interface.

### Prerequisites

- Python 3.x installed on your system.

## Run in the back-end

`poetry shell`

`poetry install`

This will run the install script to add necessary dependencies to your system.

### Example

```bash

$ python dns_enum_script_only.py < domain >
$ python subdomain_enum_script_only.py < subdomain >

```

## Run in the front-end

start the server:

```bash

$ python dns_enum_server.py

```

Run the index.html file in the browser
