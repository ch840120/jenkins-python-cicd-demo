# Dockerfile
FROM jenkins/jenkins:lts

USER root

# 1. 安裝 docker.io CLI，清理 apt 快取
RUN apt-get update \
 && apt-get install -y --no-install-recommends docker.io \
 && rm -rf /var/lib/apt/lists/*

# 2. 建立或修改 docker 群組，使其 GID 與宿主機 /var/run/docker.sock 的群組一致
RUN if getent group docker >/dev/null; then \
      groupmod --gid 1001 docker; \
    else \
      groupadd --gid 1001 docker; \
    fi \
 && usermod -aG docker jenkins

USER jenkins