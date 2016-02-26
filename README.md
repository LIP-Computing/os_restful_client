# OS Restful Client

Python openstack client which interacts with the OS restful api directly.

**Project and user management is supported:** 
 * List elements.
 * Show details of a single element.
 * Create single or bunch of elements, using attributes in command line or a file (json|yaml).
 * Delete single or bunch of elements, using attributes in command line or a file (json|yaml).

**Role management is supported:** 
 * List roles.
 * Show role details.
 * Grant project to a user using a role.
 * Delete grants of a user in a project using a role.
 * List grants of a users in a projects filtering by project.
 * List grants of a users in a projects filtering by user.
 
**Command execution messages can be show in json or table format by using the --output parameter** (see Usage)

## Configuration
The client requires the following environment variables:
    
    $ export OS_AUTH_URL=https://SERVER:5000/v3    
    $ export OS_TOKEN=XXX
    

## Installation
    $ git clone https://github.com/LIP-Computing/os_restful_client.git
    $ cd os_restful_client
    $ pip install .


## Usage


To use it:

    $ os_restfulcli --help


