import sys

# custom exception function
def error_message_details(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()  # gets information about the exception from the interpreter
    file_name = exc_tb.tb_frame.f_code.co_filename
    lineNo = exc_tb.tb_lineno
    error_message = "error occured in script [{0}] on line number [{1}]; error message [{2}]".format(
        file_name,
        lineNo,
        str(error)
    )
    
    return error_message
    
# defining a custom exception class which inherits from the base exception class
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)  # calling the parent class constructor
        self.error_message = error_message_details(error_message,error_detail)
        
    def __str__(self):
        return self.error_message