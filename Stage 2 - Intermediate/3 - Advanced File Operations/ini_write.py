import configparser

co = configparser.ConfigParser()
co["author"] = {"name":"Shailesh","contact":"shailesh@gmail.com"}
co["server"] = {"port":8000,"host":"127.0.0.1"}
co["database"]={"url" : "postgres://user:password@host:port/database", "pool" : "100"}

co.add_section("logging")
co.set("logging","level","info")
co.set("logging","file","/var/log/web-server.log")

with open("server-config.ini","w") as file:
    co.write(file)
    
