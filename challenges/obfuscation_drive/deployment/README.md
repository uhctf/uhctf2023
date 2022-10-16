# Deployment
1. Change params in `src/build.sh`.
2. `docker build -t <image_name> .`
3. `docker run -p <port>:80 --rm <image_name>`
