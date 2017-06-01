# docker_sandbox

This is an [Ansible](http://www.ansible.com) role that wraps docker_provisioner and idempotence_tester roles to make easy to run unit tests.

The role will provisione a docker based sandbox and run idempotence tests on the deployed containers.

## Requirements

- Ansible >= 2.3

## Role Variables

A list of all the default variables for this role is available in `defaults/main.yml`.

Also, the role setup the following facts during execution:

- docker_sandbox_inventory: contains the path to a inventory file with the docker containers deployed in the sandbox.
- docker_sandbox_test_result: contains the result of the idempotence tests.

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
        that: not docker_sandbox_test_result | failed

- name: simple idempotence test
  hosts: docker_sandbox_containers
  tasks:
    - name: create an empty file
      copy:
        src: /etc/issue
        dest: /tmp/
        force: no
  tags:
    - idempotence

- name: cleanup docker docker sandbox
  hosts: localhost
  roles:
    - role: docker_sandbox
      docker_sandbox_state: absent
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
