FROM node:alpine
WORKDIR /app
COPY . /app
RUN npm install
# Set an ENV flag=whatever to have the challenge be ready for deployment
ENV FLAG="uhctf{js_more_like_jf*ck_7b453d6}"
ENV PORT=80
CMD npm run start