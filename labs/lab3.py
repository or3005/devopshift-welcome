from fastapi import FastAPI
import httpx
import json
import requests
import time
import os

# app=FastAPI()

API_KEY=os.environ["API_KEY"]
# @app.get("/users")
def get_users():
    try:
        user_input=input("Enter a user name:")
        response=httpx.get("https://jsonplaceholder.typicode.com/users")
        code=response.status_code
        users=response.json()
        for user in users:
            if user["name"]==user_input:
                print("User Data:\n"+ "User Name: " + user["name"] + "\n"+ "Email: " + user["email"] + "\n"+ "Address: " + str(user["address"]))

                
                return code
        
     
    except httpx.HTTPError as e:
        
        if code==404:    
            print("User not found")
            # return response=httpx.post("https://jsonplaceholder/typicode.com/users",json=users)
            
        if code==500:
             print("Server error, plese try again later")
         
    except Exception:        
        e.add_note("error in get users function")
        print(e)        
    
    return code


def get_metrics():
    url = "https://api.example.com/system/metrics?metrics=cpu,memory"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    retries = 3

    for attempt in range(1, retries + 1):
        try:
            print(f"Fetching system metrics... (Attempt {attempt})")
            response = requests.get(url, headers=headers, timeout=5)
            response.raise_for_status()  # Raise an error for non-200 responses
            print("System Metrics:", response.json())
            break
        except requests.exceptions.HTTPError as errh:
            if response.status_code == 401:
                print("Invalid API Key.")
                break
            elif response.status_code == 500:
                print("Server is currently down.")
            else:
                print(f"HTTP error occurred: {errh}")
        except requests.exceptions.ConnectionError:
            print("Error: Unable to connect to the API.")
        except requests.exceptions.Timeout:
            print("Error: The request timed out.")
        except requests.exceptions.RequestException as e:
            print(f"General error occurred: {e}")
        
        if attempt < retries:
            print(f"Retrying in 2 seconds...")
            time.sleep(2)
        else:
            print("All retry attempts failed.")


