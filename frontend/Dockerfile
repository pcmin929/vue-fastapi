# Stage 1: Build
FROM node:16 AS build
WORKDIR /app
# Copy package.json and package-lock.json (or yarn.lock) files
COPY package*.json ./
# Install dependencies
RUN npm install
# Copy the rest of the app’s code
COPY . .
# Build the Vue.js app for production
RUN npm run build

# Stage 2: Serve
FROM nginx:alpine
# Copy built files from Stage 1
COPY --from=build /app/dist /usr/share/nginx/html
COPY --from=build /app/default.conf /etc/nginx/conf.d/default.conf