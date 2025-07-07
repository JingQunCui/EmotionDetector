# frontend/Dockerfile
FROM node:18

WORKDIR /app

COPY . .

RUN npm install

RUN npm install --save-dev vite@vitejs/plugin-react

EXPOSE 3000

CMD ["node", "app.js"]