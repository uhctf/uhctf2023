FROM node:alpine
WORKDIR /app
COPY . /app
RUN npm install
# Set an ENV flag=whatever to have the challenge be ready for deployment
ENV PORT=80
CMD npm run start