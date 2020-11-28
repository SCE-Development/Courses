# Nginx
- It is used to manage or simplify servers
![nginx](https://user-images.githubusercontent.com/18486562/100410425-86e3d980-3023-11eb-9936-9166dd86039a.png)

## Dependencies
1. [Nginx](https://nginx.org/en/)
2. NodeJS
3. In a folder: make `nginx.conf`
```bash
http {
    # actual nginx server, doesn't do anything yet
    server {
        listen 8080;
    }
}
#require whether used or not
events { }   
```
4. In the same folder: 
```
npm install express
```
5. In the same folder: make `server.js`, with
```js
var express = require('express');

//server1
var app = express();
var port = 8081
app.get('/', function (req, res) {
    res.status(200).send("Server on "+port)
})
app.listen(port, ()=>{console.log(port)})

//server 2
var app2 = express();
var port2 = 8082
app2.get('/', function (req, res) {
    res.status(200).send("Server on "+port2)
})
app2.listen(port2, ()=>{console.log(port2)})

//server 3
var app3 = express();
var port3 = 8083
app3.get('/', function (req, res) {
    res.status(200).send("Server on "+port3)
})
app3.listen(port3, ()=>{console.log(port3)})
```
5. Create some folders and insert a stick html file for each, My folder will look something like this:
   
![image](https://user-images.githubusercontent.com/18486562/100489116-46d63280-30c7-11eb-8b88-a9aeb4aa6803.png)

where html files can be anything:
```html
    <h1>Home</h1>
```
```html
    <h1>Site 1</h1>
```
```html
    <h1>Site 2</h1>
```

<br><br><br>

## Basic commands
- You will have to restart nginx for every changes in `nginx.conf`
1. Start
   ```bash
    #where -c follows by a path to your nginx.conf file (you can use 'pwd' in terminal to get current path)
    sudo nginx -c /home/thai/Courses/Microservices/Nginx/app/nginx.conf 

    #or from root conf
    sudo nginx -s start
   ```
2. Stop
    ```bash
    # where -s is "signal"
    sudo nginx -s stop
    ```
3. Reload
   ```bash
   sudo nginx -s reload
   ```

<br><br><br>

## Let's write them codes
- In `nginx.conf`:

## Serve folders
- I will serve my app folder, `remember to start/reload nginx after each changes`:

![image](https://user-images.githubusercontent.com/18486562/100489116-46d63280-30c7-11eb-8b88-a9aeb4aa6803.png)
```bash
http {
    # actual nginx server, doesn't do anything yet
    server {
        listen 8080;
        
        #root + path to folder
        root /home/thai/Courses/Microservices/Nginx/app;

        location /error {
            return 403;
        }
    }
}
#require whether used or not
events { }   
```
![image](https://user-images.githubusercontent.com/18486562/100489371-b00a7580-30c8-11eb-9f62-1506ac78fed5.png)

![image](https://user-images.githubusercontent.com/18486562/100489429-f19b2080-30c8-11eb-8ad0-39c1749f54bf.png)

![image](https://user-images.githubusercontent.com/18486562/100489536-8aca3700-30c9-11eb-897a-7706a7e67592.png)

Even images!

![image](https://user-images.githubusercontent.com/18486562/100489436-02e42d00-30c9-11eb-9524-16813899d679.png)

<br><br><br>

## Lets manage some nodejs (or any) servers
Run the demo `server.js` for demo purposes, you can write your own:
```
node server.js
```
- In `nginx.conf`:
```bash
http {
    #upstream connection to node servers from npm run server
    upstream myServer1 {
        server localhost:8081;
    }
    upstream myServer2 {
        server localhost:8082;
    }
    upstream myServer3 {
        server localhost:8083;
    }

    # actual nginx server
    server {
        listen 8080;

        location /api1 {
            proxy_pass http://myServer1/;
        }
        location /api2 {
            proxy_pass http://myServer2/;
        }
        location /api3 {
            proxy_pass http://myServer3/;
        }
    }
}

#require whether used or not
events { }
```
- Each route is responsible for each server

![image](https://user-images.githubusercontent.com/18486562/100489559-a2a1bb00-30c9-11eb-854e-3cda3f274121.png)

![image](https://user-images.githubusercontent.com/18486562/100489568-b0574080-30c9-11eb-94cd-4cfcdbffd551.png)

![image](https://user-images.githubusercontent.com/18486562/100489578-c2d17a00-30c9-11eb-8d8e-5de164f1cbcd.png)

<br><br><br>

## Basic Load balancers 

### Round-Robin
- Direct client to each server on calls
```bash 
http {
    #sample load balancers
    upstream roundrobin {
        #round robin
        server localhost:8081;
        server localhost:8082;
        server localhost:8083;
    }

    # actual nginx server
    server {
        listen 8080;

        location /roundrobin {
            proxy_pass http://roundrobin/;
        }
    }
}

#require whether used or not
events { }
```
- So now every time you `reload`:

![image](https://user-images.githubusercontent.com/18486562/100489734-04aef000-30cb-11eb-9f7c-b65d355ff0e6.png)

![image](https://user-images.githubusercontent.com/18486562/100489742-11cbdf00-30cb-11eb-811f-8dc3fd066dca.png)

![image](https://user-images.githubusercontent.com/18486562/100489754-28723600-30cb-11eb-9cda-63e31c9d904a.png)

<br>

### Sticky connection (for stateful purposes)
- Each client is designated to one server
```
http {
    upstream stickyconnection {
        ip_hash; #client stick to 1 server
        server localhost:8081;
        server localhost:8082;
        server localhost:8083;
    }

    # actual nginx server
    server {
        listen 8080;

        location /stickyconnection {
            proxy_pass http://stickyconnection/;
        }
    }
}

#require whether used or not
events { }
```
- Nginx assigned me to only 1 server
  
![image](https://user-images.githubusercontent.com/18486562/100489772-3de76000-30cb-11eb-9c2f-235cf9bf50b2.png)

<br><br>

## Done!
Congratz! you are now Nginx.