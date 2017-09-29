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
