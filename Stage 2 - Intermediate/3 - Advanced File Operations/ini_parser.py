import configparser

co = configparser.ConfigParser()

with open("server-config.ini","r") as file:
    
    # read full file
    # data = file.read()
    # print("server-config.ini")
    # print(data)
    
    # read specific field
    co.read_file(file)
    print(co.get("database","url")) 
    
    # update 
    co.set("database","url","postgres://user:updated-password@host:port/database")
    print(co.get("database","url")) 
    
    # remove field or section
    co.remove_option("logging","file")
    co.remove_section("logging")
    
    for section in co.sections():
        print(f"[{section}]")
        for key, value in co.items(section):
            print(f"{key} = {value}")
        print()    
    
