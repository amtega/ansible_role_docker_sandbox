# Ansible docker_sandbox role

This is an [Ansible](http://www.ansible.com) role that wraps docker_provisioner and idempotence_tester roles to make easy to run unit tests.

The role will provisione a docker based sandbox and run idempotence tests on the deployed containers.

## Requirements

- Ansible >= 2.3

## Role Variables

A list of all the default variables for this role is available in `defaults/main.yml`.

Also, the role setup the following facts during execution:

- docker_sandbox_images: contains the list of docker images provisioned on the sandbox.
- docker_sandbox_containers: contains the list of randomized docker containers provisioned on the sandbox.
- docker_sandbox_inventory: contains the path to a inventory file with the docker containers deployed in the sandbox.
- docker_sandbox_idempotence_result: contains the result of the idempotence tests.

## Dependencies

This role depends on 'docker_provisioner' and 'idempotence_tester' roles.

## Example Playbook

This is an example playbook:

```yaml
---
- name: sample docker_sandbox usage
  hosts: localhost
  roles:
    - role: docker_presets
    - role: docker_sandbox
      docker_sandbox_state: started
  tasks:
    - name: assert that idempotence test was ok
      assert:
        that: not docker_sandbox_idempotence_result | failed

- name: simple idempotence test
  hosts: docker_sandbox_containers
  tasks:
    - name: create an empty file
      copy:
        content: ""
        dest: /tmp/emptyfile
        force: no
  tags:
    - idempotence

- name: cleanup docker docker sandbox
  hosts: localhost
  roles:
    - role: docker_sandbox
      docker_sandbox_state: absent
```

If you want to create a temporary sandbox to work you can use the two sample playbooks provided in the `files` dir. First call the create sandbox playbook:

```
ansible-playbook files/create_sandbox.yml
```

Previous playbook should print the path to the inventory managed by the sandbox:

```
TASK [debug] **************************************************************************************************************************************************************************************************
ok: [localhost] => {
    "docker_sandbox_inventory": "/tmp/ansible.oAxX3B.inventory"
}
```

You can work with this sandbox passing this inventory path to ansible-playbook using "-i" flag:

```
ansible-playbook main.yml -i /tmp/ansible.oAxX3B.inventory
```

When you want to drop the sandbox use the provided cleanup playbook:

```
ansible-playbook files/cleanup_sandbox.yml -i /tmp/ansible.oAxX3B.inventory
```

## Testing

You can run the tests with the following commands:

```shell
$ cd docker_sandbox/test
$ ansible-playbook main.yml
```

## License

Not defined.

## Author Information

- Juan Antonio Valiño García ([juanval@edu.xunta.es](mailto:juanval@edu.xunta.es)). Amtega - Xunta de Galicia
