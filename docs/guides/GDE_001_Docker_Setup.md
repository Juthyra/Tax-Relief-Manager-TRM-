# GDE-001: Docker setup: install Docker and pull the images of the stack

| Item | Value |
| --- | --- |
| Document ID | GDE-001 |
| Document type | GDE (guide: how to set something up) |
| Product | Tax Relief Manager (TRM), Malaysia tax relief system (PWA) |
| Version | 0.1 |
| Status | Proposed (waits for review by the other developer and approval by the owner) |
| Date | 2026-11-24 (first written 2026-11-24) |
| Owner | Champs (product owner) |
| PRD reference | PRD-TRM section 7 (technical constraints); no functional requirement |
| Source | ADR-001 to ADR-004 (approved 23/11/2026); owner prompts P-72 to P-75, P-87 to P-90; Docker documentation and Docker Hub read on 24/11/2026 |
| Change tracking | [REG-01 History log](../registers/REG_01_History_Log.md); detail in [REG-02](../registers/REG_02_URS_SRS_Change_Log.md) |
| Decided by | Docker-only development: owner, 23/11/2026 (P-72 to P-75). The images and tags in section 4: proposed, they wait for the owner |

## 1. What this guide does

It shows how to install Docker on macOS, Windows or Linux, and how to pull and check the six images that the stack needs. It is for the two developers and for anyone who joins later.

**What it does not do.** It does not start the project. Whether the project uses Laravel Sail or our own compose file is still open ([ADR-003](../decisions/ADR_003_Docker.md)), and the project does not exist yet. The project's own Dockerfile and compose file are written when the project is created. Hosting ([ADR-005](../decisions/ADR_005_Hosting.md)) and email ([ADR-006](../decisions/ADR_006_Email_Service.md)) are held.

**What was tested.** Everything marked "run" was run on 24/11/2026 on a Mac with Apple silicon, macOS 26.5, Docker Desktop with Docker 28.3.2 and Compose 2.38.2. The Windows and Linux steps are taken from Docker's own pages and **were not run** by the author. If a step fails on your system, say so in the pull request and fix this guide.

## 2. Install Docker

You need Docker and the Compose plugin (`docker compose`, with a space). You do not need to install PHP, Node, PostgreSQL or Python on your computer. They run in containers.

| System | What to install | Official page |
| --- | --- | --- |
| macOS | Docker Desktop | [Install Docker Desktop on Mac](https://docs.docker.com/desktop/setup/install/mac-install/) |
| Windows 10 or 11 | Docker Desktop with the WSL 2 backend | [Install Docker Desktop on Windows](https://docs.docker.com/desktop/setup/install/windows-install/) |
| Linux | Docker Engine and the Compose plugin (or Docker Desktop for Linux) | [Install Docker Engine](https://docs.docker.com/engine/install/) |

**Licence.** Docker's page says Docker Desktop is free for personal use, education, non-commercial open source and small businesses (fewer than 250 employees and less than 10 million USD a year), and needs a paid subscription for larger companies ([Docker's licence page](https://docs.docker.com/subscription-billing/desktop-license/)). Docker Engine on Linux is a separate package. The owner checks that the licence fits each developer.

### 2.1 macOS

- Requirements (Docker's page): the current macOS or one of the two previous major releases, at least 4 GB of RAM. Rosetta 2 is recommended on Apple silicon: `softwareupdate --install-rosetta`.
- Download the installer for your chip (Apple silicon or Intel) from the official page, open it, move Docker to Applications, start it, and accept the terms. Wait until the whale icon says Docker is running.
- Quit tools that call Docker in the background (editor, terminals) before an install or update.

### 2.2 Windows

- Requirements (Docker's page, WSL 2 backend): Windows 10 22H2 (build 19045) or Windows 11 23H2 (build 22631) or later, Pro, Enterprise or Education; WSL version 2.1.5 or later; 8 GB RAM; hardware virtualization turned on in the BIOS or UEFI. Check WSL with `wsl --version`. Update it with `wsl --update`.
- Install Docker Desktop and choose the WSL 2 backend.
- **Keep the project folder inside the Linux side of WSL** (for example `~/trm` in your Ubuntu distribution), not under `C:\`. Docker's best-practice page says files bind-mounted from the Linux file system are much faster, and file-change events (for automatic reload) only reach containers from there ([WSL 2 best practices](https://docs.docker.com/desktop/features/wsl/best-practices/)). Open the folder in your editor through its WSL extension.
- **Line endings.** Windows Git can turn line endings into CRLF, which breaks shell scripts in Linux containers. Work inside WSL with the Linux Git, or set `git config --global core.autocrlf input`. A `.gitattributes` file that fixes this for everyone is proposed in section 8, not done.
- Run every command in this guide in the WSL terminal. The commands are the same as on macOS.

### 2.3 Linux

Docker's page lists Ubuntu 26.04 LTS, 24.04 LTS and 22.04 LTS (and others) as supported for Docker Engine. Other distributions have their own pages on the same site.

For Ubuntu, from Docker's page of 24/11/2026 (check the page again before you run it):

```bash
# Remove unofficial packages that conflict
sudo apt remove docker.io docker-compose docker-compose-v2 docker-doc podman-docker

# Add Docker's official key and apt repository
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF
sudo apt update

# Install Docker Engine, the build plugin and the Compose plugin
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo systemctl status docker
```

Then run Docker without `sudo` ([Linux post-install steps](https://docs.docker.com/engine/install/linux-postinstall/)):

```bash
sudo groupadd docker          # the group may already exist
sudo usermod -aG docker $USER
newgrp docker                 # or log out and log in
```

Members of the `docker` group have root-level power over the computer. Docker's page points to rootless mode for a stricter setup ([rootless mode](https://docs.docker.com/engine/install/security/rootless/)). This guide does not cover it.

## 3. Check that Docker works

Run these in a terminal (WSL terminal on Windows). The first run of `hello-world` downloads a tiny test image. It is the only image in this guide that is not pinned, because it is only a test.

```bash
docker --version
docker compose version
docker run --rm hello-world
```

Expected: a version line each, then "Hello from Docker!". Run on 24/11/2026: Docker 28.3.2, Compose 2.38.2.

## 4. The images

Rules for every image in this project: a **full version tag**, never `latest` and never only a major number, plus the **digest** written down here so two developers can see they have the same image. Versions follow [ADR-001](../decisions/ADR_001_Language_And_Framework.md) (PHP 8.5, Node 26 LTS) and [ADR-004](../decisions/ADR_004_Database.md) (PostgreSQL 18). The tags were read from Docker Hub on 24/11/2026.

| # | Role | Image and pinned tag | Disk size (Apple silicon, run) | Status |
| --- | --- | --- | --- | --- |
| 1 | PHP for Laravel (command line) | `php:8.5.13-cli` | 181 MB | Approved version line (ADR-001) |
| 2 | Composer (PHP packages) | `composer:2.11.2` | 80 MB | Proposed |
| 3 | Node for the front-end build | `node:26.13.1` | 434 MB | Approved version line (ADR-001) |
| 4 | Database | `postgres:18.7` | 167 MB | Approved version line (ADR-004) |
| 5 | Document tools (build, checks) | `python:3.12.16` | 400 MB | Proposed |
| 6 | Mail catcher for local email | `axllent/mailpit:v1.34.0` | 14 MB | Proposed; email service is held (ADR-006) |
| 7 | ERD diagram export (optional) | `minlag/mermaid-cli:12.0.1` | 581 MB | Proposed |

All six main images together are about 1.3 GB on disk. The Docker Hub pages list both `amd64` (Intel, AMD, most Windows and Linux) and `arm64` (Apple silicon) builds for all seven, so the same tag works on every system named in section 2. Digests of the multi-platform index (the value `docker image inspect` shows as `RepoDigests`):

| Image | Digest |
| --- | --- |
| `php:8.5.13-cli` | `sha256:f324fcb4dc009ac0470a7d614cd122499dcee3ca47a9bab620fc14c0eb759ba2` |
| `composer:2.11.2` | `sha256:50ea4d33fdcde1adb0f045547295faa1548b33872e5f789dae5b02ce2fb5de93` |
| `node:26.13.1` | `sha256:e18c3ccdf7d71619990b0e85639f506e2028a95410999cab24cc373cbd10e0ac` |
| `postgres:18.7` | `sha256:eb63372c1e05c755f55fa30cbd07aecc443676fc6c0fa90b9002d01537841e1a` |
| `python:3.12.16` | `sha256:5411fa1b302c43f510324381162b5f5d0d93b9ee2af538f09d944f0d290ee3cb` |
| `axllent/mailpit:v1.34.0` | `sha256:23a2ef85bc50853ab3093645d1d64679afd8887e89da5e48a88940c172591a4e` |
| `minlag/mermaid-cli:12.0.1` | `sha256:18938e53497376d524e04b1fc0bf7b6d61a491ce9ff7032bb2855d57155acb10` |

A tag can move on the registry (a rebuild of the same version). If your digest differs from this table, the image was rebuilt: tell the other developer and update this table.

### 4.1 Pull them

Same commands on every system:

```bash
docker pull php:8.5.13-cli
docker pull composer:2.11.2
docker pull node:26.13.1
docker pull postgres:18.7
docker pull python:3.12.16
docker pull axllent/mailpit:v1.34.0
docker pull minlag/mermaid-cli:12.0.1
```

### 4.2 Check each one

Run on 24/11/2026, with this output:

| Command | Output |
| --- | --- |
| `docker run --rm php:8.5.13-cli php -v` | `PHP 8.5.13 (cli) ...` |
| `docker run --rm composer:2.11.2 composer --version` | `Composer version 2.11.2 ...` |
| `docker run --rm node:26.13.1 node -v` | `v26.13.1` |
| `docker run --rm node:26.13.1 npm -v` | `11.20.0` |
| `docker run --rm postgres:18.7 postgres --version` | `postgres (PostgreSQL) 18.7 (Debian 18.7-1.pgdg13+5)` |
| `docker run --rm python:3.12.16 python --version` | `Python 3.12.16` |
| `docker run --rm axllent/mailpit:v1.34.0 version` | `/mailpit v1.34.0 compiled with go1.27.4 on linux/arm64` |

To compare a digest: `docker image inspect --format '{{index .RepoDigests 0}}' php:8.5.13-cli`.

### 4.3 What each image is for, and what to know

| Image | Notes |
| --- | --- |
| PHP | Laravel runs here. **The plain image is not enough.** Its modules (checked with `php -m`) include `PDO` and `pdo_sqlite` but **not** `pdo_pgsql`, `intl`, `zip`, `bcmath` or `gd`. The project's Dockerfile must add what Laravel and PostgreSQL need (the image ships `docker-php-ext-install` for this). That Dockerfile is written when the project is created |
| Composer | Used to install PHP packages. It can be copied into the PHP image later |
| Node | Builds the Vue front end and runs the TypeScript tests. The image has a ready user `node` (uid 1000) |
| PostgreSQL | The database. Run on 24/11/2026: a container with a test password started, `pg_isready` said "accepting connections", and the server process ran as the user `postgres`, not root. The data folder must be a Docker volume, or the data is lost with the container |
| Python | Runs the document tools. Run on 24/11/2026: a copy of the repository was mounted into `python:3.12.16` as user 1000 and `build.py`, `check_standard.py` and `check_acronyms.py` all passed with no extra packages. `topdf.py` was not tested and is only needed for PDFs |
| Mailpit | Catches the emails that the app sends in development. Web page on port 8025, SMTP on port 1025 (from its documentation). It is an assumption that we use it; ADR-006 is held |
| Mermaid CLI | Turns the `.mmd` text of an ERD into an SVG. Optional |

**Non-root.** The image config of the PHP, Composer, Node, PostgreSQL, Python and Mailpit images does not set a user, so a container starts as root unless the project's compose file sets one (PostgreSQL then drops to its own user by itself). Our rule is non-root, so the project's Dockerfiles must set `USER`, and the compose file must give each service a user. This is for the project creation step ([ADR-003](../decisions/ADR_003_Docker.md)).

## 5. Common problems

| Message or sign | Cause and fix |
| --- | --- |
| `Cannot connect to the Docker daemon ... Is the docker daemon running?` | Docker Desktop is not started (seen on 24/11/2026 before the app was opened). Start Docker Desktop and wait. On Linux: `sudo systemctl start docker` |
| `permission denied ... docker.sock` (Linux) | Your user is not in the `docker` group: section 2.3 |
| Docker Desktop will not start on Windows | Virtualization is off in the BIOS or UEFI, or WSL is older than 2.1.5: `wsl --update` |
| Very slow file access, or no auto reload (Windows) | The project is on the Windows disk. Move it into the WSL file system: section 2.2 |
| `port is already allocated` | Another program uses the port (PostgreSQL 5432, Mailpit 8025 and 1025). Stop it or change the host port in the compose file |
| `no space left on device` | `docker system df` shows what Docker uses. `docker image prune` removes unused images. Do not prune volumes without asking: the database data lives there |
| A pull is very slow or stops | Retry. The images are about 1.3 GB in total |

## 6. Rules for keeping this guide true

1. A new image or a new version goes into section 4 with its digest, in the same pull request that changes the stack ([ADR-001](../decisions/ADR_001_Language_And_Framework.md)).
2. Never use `latest` for a project image.
3. The commands are checked on the system they claim. A step you have not run says so.

## 7. Where this leads

Next, when the project is created: the project's Dockerfile and compose file, the choice between Sail and our own file (ADR-003), and the first start of the application. The README is updated for the stack when the owner asks.

## 8. Open points

- A `.gitattributes` file to fix line endings for all systems (section 2.2) is proposed. It is a repository change, so it waits for the owner.
- The Windows and Linux steps need a run by a developer on those systems.
- Mailpit and the Python image are proposals. The PHP, Node and PostgreSQL version lines are approved, but their full tags here are not yet approved as the pinned tags.
- Whether the guide also needs a part for Docker Desktop settings (memory, disk) is decided after the first real project start.
