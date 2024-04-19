import argparse
import os

import uvicorn
from dotenv import load_dotenv

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Run the server in different modes.")
    parser.add_argument(
        "--prod",action="store_true", 
        help="Run the server in production mode.")
    parser.add_argument(
        "--test",action="store_true", 
        help="Run the server in test mode.")
    parser.add_argument(
        "--dev",action="store_true", 
        help="Run the server in development mode.")
    
    args = parser.parse_args()

    if args.prod:
        load_dotenv(".env.prod")
    elif args.test:
        load_dotenv(".env.test")
    else:
        load_dotenv(".env.dev")


    uvicorn.run(
        "app.main:app", 
        host="0.0.0.0" , 
        port=int(os.getenv("PORT")) , 
        reload=bool(os.getenv("RELOAD")) 
    )
