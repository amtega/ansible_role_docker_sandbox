# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from random import randint

def randomize_names(elements, groups=['docker_sandbox_containers']):
    """Randomize the names of the containers

    Keyword arguments:
    elements -- list of dicts with the containers. See the role
                variables docker_provisioner_containers and for samples of the
                dict structure.

    The return value will be the same list passed as argument, but with the
    containers name randomized.
    """
    result = list()
    for element in elements:
        if "name" in element:
            basename = element["name"]
        else:
            basename = element["image"]

        element["name"] = "{}_{}".format(basename[-22:], randint(0, 99999999))

        result.append(element)

    return result

class FilterModule(object):
    """Ansible docker_provisioner filters"""

    def filters(self):
        return {
            'randomize_names': randomize_names,
        }
