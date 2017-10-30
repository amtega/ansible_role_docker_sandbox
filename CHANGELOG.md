# Change Log

## 2017-05-31

- Initial release.

## 2016-06-01

- Improved documentation in README.md file.

## 2017-06-05

- Improved documentation in README.md file.

## 2017-06-07

- Fixed sandbox containers to use ssh instead of tty.

## 2017-06-17

- Added "docker_sandbox_ppid" to sandbox containers labels.

## 2017-06-21

- Added "docker_sandbox_user" to sandbox containers labels.
- Adddd mechanism to cleanup stalled containers based on ppid and user.
- Improved documentation.

## 2017-06-22

- Added mechanism to cleanup stalled containers based on playbook.

## 2017-06-23

- Fixed bug in cleanup of stalled docker containers.
- Refactored tasks in several files.

## 2017-07-03

- Added support to restart or not the docker containers after running idempotence tests.

## 2017-09-15

- Improved tests.

## 2017-09-25

- Improved dry run support.

## 2017-09-27

- Added two sample playbooks to create and cleanup a sandbox.

## 2017-09-29

- Refactored include directives by include_tasks / import_tasks.
- Updated documentation.

## 2017-10-02

- Fixed files/cleanup_sandbox.yml.
- Updated documentation.

## 2017-10-19

- Now inventory file can be specified as a role variable.
- Refactored "restarted" state to "recreated".
- Removed docker_sandbox_idempotence_test_tag variable.

## 2017-10-23

- Fixed big with idempotence test docker recreation.
- Fixed tests.
- Change defaults of 'docker_sandbox_cleanup_*' variables to disable them if and inventory is specified in 'docker_sandbox_inventory'.
- Added 'docker_sandbox_cleanup_by_playbook' role variable.

## 2017-10-24

- Fixed bugs.
- Fixed tests.

## 2017-10-30

- Improved tests.
- Improved create_sandbox.yml and cleanup_sandbox.yml playbooks.
