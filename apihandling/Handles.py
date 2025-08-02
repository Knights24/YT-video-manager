import requests

def random_url_request():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    
    else:
        raise Exeption("FAiled to fetch user data") 
    

def main():
    try:
        username,country = random_url_request()
        print(f"Username :  {username} \n Country : {country}")
    except Exeption as e:
        print(str(e))



if __name__ == "__main__":
    main()