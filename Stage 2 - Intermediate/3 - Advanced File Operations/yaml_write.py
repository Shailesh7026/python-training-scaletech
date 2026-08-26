import yaml

config_dict = {}
config_dict["author"] = {"name":"Shailesh","contact":"shailesh@gmail.com"}
config_dict["server"] = {"port":8000,"host":"127.0.0.1"}
config_dict["database"]={"url" : "postgres://user:password@host:port/database", "pool" : "100"}

details_dict = {"Project Name":"My yaml writer","version":"1.0.0"}

with open("server-config.yaml","w") as file:
    # yaml.dump(config_dict,file)
    yaml.dump_all([config_dict,details_dict],file)
    
