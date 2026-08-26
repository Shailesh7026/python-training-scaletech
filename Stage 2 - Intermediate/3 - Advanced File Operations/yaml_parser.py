import yaml

with open("server-config.yaml","r") as file:
    # generator_obj=yaml.load_all(file,Loader=yaml.SafeLoader)
    
    # for data in generator_obj:
    #     print(data)
    
    
    config_dict=yaml.load(file,Loader=yaml.SafeLoader)
    config_dict["credentials"]={"id":"admin123","password":"password123"}
    
    print(config_dict)
    
    
    config_dict.pop("credentials")

    print(config_dict)
    
    
    
