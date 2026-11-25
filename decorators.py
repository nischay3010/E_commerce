from functools import wraps
from datetime import datetime
from pathlib import Path
import time
from custom_exceptions import (UserNotSignInError,UnAuthorizedAccessError)


def authorize(required_role):
    def decorator(function):
        @wraps(function)
        def wrapper(current_user,*args,**kwargs):
            try:
                if current_user is None:
                    raise UserNotSignInError("login first")  
                if current_user[5]!=required_role:
                    raise UnAuthorizedAccessError("Unauthorized:access denied")
            except UserNotSignInError as err:
                print("Error - You are not sign in:",err)
                return
            except UnAuthorizedAccessError as err:
                print("Error-Only Admin has Access",err)
                return
            else:
                return function(current_user,*args,**kwargs)
        return wrapper
    return decorator

activity_file=Path("logs/activity.log")

def logging(function):
    @wraps(function)
    def wrapper(current_user,*args,**kwargs):
        start_time=datetime.now()

        with activity_file.open(mode="a",encoding="utf-8") as file:
            file.write(
                f"{start_time}|"
                f"user:{current_user[2]}|"
                f"function:{function.__name__}|"
                f"Action started\n"
            )
        end_time=datetime.now()

        result = function(current_user, *args, **kwargs)

        with activity_file.open(mode="a",encoding="utf-8") as file:
                    file.write(
                        f"{end_time}|"
                        f"user:{current_user[2]}|"
                        f"function:{function.__name__}|"
                        f"Action completed\n"
        
                    )
        return result
    return wrapper


def execution_time(function):
     @wraps(function)
     def wrapper(*args,**kwargs):
          start_time=time.perf_counter()

          result=function(*args,**kwargs)

          end_time=time.perf_counter()

          execution_time=end_time-start_time

          print(f"{function.__name__} executed in {execution_time:.6f} seconds")
          
          return result
     return wrapper

