# Spark

Run the container:
```bash
sudo docker compose up --build
```

You can connect to the web interface in `http://localhost:8080/`

Let's interact from cli:
```bash
sudo docker exec -it ac800ea6e9fd bash
scala> spark.range(1000 * 1000 * 1000).count()
```
