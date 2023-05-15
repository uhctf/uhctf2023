# Deployment
1. Edit flag in `Dockerfile`
2. `docker build -t <image_name> .`
3. `docker run -p <port>:8000 -v $(pwd)/attachments/:/attachments/ --rm <image_name>`
    - This also compiles the binary for deployment. See `attachments`.
