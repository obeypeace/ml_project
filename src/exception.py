import sys
# sys library is used to manipulate the diff parts of the python runtime env.
from src.logger import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occured at {file_name} line number {exc_tb.tb_lineno} error message {str(error)}"
    
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        
    def __str__(self):
        return self.error_message
    
# if __name__=="__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Divion by Zero, change the denominator")
#         raise CustomException(e, sys)
        
        
"""
error: This is the error object itself (e.g., a TypeError or FileNotFoundError).

error_detail:sys: This is a type hint. It indicates that the error_detail argument is expected to be the sys module, 
which contains information about the current state of the interpreter, including active exceptions.

sys.exc_info() is a function that, when called inside an except block, returns a tuple of three values:
The exception type, the exception value and the traceback object (exc_tb).
The _ (underscore) is a Python convention for a variable that you're not going to use. 
In this case, we only care about the traceback object.

------Extracting Information from the Traceback:
file_name = exc_tb.tb_frame.f_code.co_filename
error_message = f"Error occured at {file_name} line number {exc_tb.tb_lineno} error message {str(error)}"
-The traceback object (exc_tb) contains the entire call stack at the time the exception occurred.
-exc_tb.tb_frame gets the frame object where the exception happened.
-f_code gets the code object for that frame.
-co_filename gets the name of the file where the code is located.
-exc_tb.tb_lineno gets the specific line number where the error was raised.
The function then uses an f-string to create a human-readable message combining the filename, line number, and the original error message.

-------error_message Custom Exception Class
This is where the custom exception is defined. It inherits from Python's built-in Exception class, which is the standard practice for all custom exceptions.
Constructor (__init__):
def __init__(self, error_message, error_detail:sys):
super().__init__(error_message): This calls the constructor of the parent class (Exception), passing the error message up the chain.
self.error_message = error_message_detail(error_message, error_detail=error_detail): 
This is where the magic from the first function is used. 
It calls error_message_detail to generate the custom, detailed message and stores it in the self.error_message attribute.

String Representation (__str__):
def __str__(self):
-return self.error_message: This method is automatically called whenever you try to print() an object of this class or convert it to a string. 
It returns the detailed error message that we stored in the __init__ method.
"""