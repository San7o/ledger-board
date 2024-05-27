# nginx

## Explaination

Nginx server. Here is an example of a simple configuration:

```nginx
server {
    listen 80;  # Listen for incoming HTTP requests on port 80
    server_name your_domain.com;  # Respond to requests for this domain

    location /old-route {
        return 301 http://new_domain.com/new-route;  # Redirect to the new domain and route
    }

    # Additional server configuration if needed
}
```
In this configuration:

- `listen 80`: Specifies that NGINX should listen for incoming HTTP requests on port 80, the default port for HTTP traffic.

- `server_name your_domain.com;`: Indicates that this server block should respond to requests directed to your_domain.com.

- `location /old-route { ... }`: Defines a location block for requests to the /old-route path. Inside this block, the return directive is used to issue a 301 (permanent) redirect response, directing the client to the specified URL http://new_domain.com/new-route.


Additionally, if you have multiple redirection rules or need to configure other aspects of the NGINX server, such as SSL termination, load balancing, or caching, you can include additional directives within the server block or in separate configuration files.

Once the NGINX configuration is defined, you would build a Docker image containing NGINX with this configuration file and then run a Docker container based on that image. The container would then handle incoming HTTP requests, applying the redirection rules as specified in the NGINX configuration.


Useful docker commands:
```bash
sudo docker ps
sudo docker stop <container_id>
sudo docker rm <container_id>
docker exec -it <container_id> bash
```

