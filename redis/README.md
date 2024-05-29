# redis

To test the connection, you can use `redis-cli`

```bash
redis-cli -h 10.5.0.40
10.5.0.40:6379> AUTH admin
```
And execute some queries:
```bsh
SET myKey "Hello"
GET myKey
DEL myKey
```

The directory `redis/persistent_storage` will be use to preserve storage after the container is stopped or deleted

The current configuration applies the following changes to the default:
```
save 60 1
appendonly yes
bind * .::1
```

Note: the admin password is for dev only. In deploy, a redis DB cluster should be set up with AWS or another provider and manage authentication differently.
