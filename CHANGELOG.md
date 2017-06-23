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
