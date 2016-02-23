# OS Restful Client

Python openstack client which interacts with the OS restful api directly.

**Project and user management is supported:** 
 * List elements.
 * Show details of a single element.
 * Create single or bunch of elements, using attributes in command line or a file (json|yaml).
 * Delete single or bunch of elements, using attributes in command line or a file (json|yaml).
 
**Command execution messages can be show in json or table format by using the --output parameter** (see Usage)

## Configuration
The client requires the following environment variables:
    
    $ export OS_AUTH_URL=127.0.0.23
    $ export OS_PORT=5000
    $ export OS_TOKEN=XXX
    $ export OS_VERSION=v3

## Installation
    $ git clone https://github.com/LIP-Computing/os_restful_client.git
    $ cd os_restful_client
    $ pip install .


## Usage


To use it:

    $ os_restfulcli --help


