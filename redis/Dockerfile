# Description: Dockerfile for Redis

FROM redis:alpine

# Copy the redis.conf file
COPY redis.conf /usr/local/etc/redis/redis.conf

# Expose the port
EXPOSE 6379

# Run the redis server
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]
