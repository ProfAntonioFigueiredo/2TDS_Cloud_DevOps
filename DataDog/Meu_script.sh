docker run -d --cgroupns host \
              --pid host \
              -v /var/run/docker.sock:/var/run/docker.sock:ro \
              -v /proc/:/host/proc/:ro \
              -v /sys/fs/cgroup/:/host/sys/fs/cgroup:ro \
              -p 127.0.0.1:8126:8126/tcp \
              -e DD_API_KEY=74b73ff0e930f51adb0a5ef3e217d91d \
              -e DD_APM_ENABLED=true \
              -e DD_SITE=datadoghq.com \
              gcr.io/datadoghq/agent:latest