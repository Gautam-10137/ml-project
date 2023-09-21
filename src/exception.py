import sys
# error detail is tracked by sys
def error_message_detail(error,error_detail:sys):
    # exception info() returns 3 things
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name[{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

#  Inheriting the parent Exception 
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        # Initializing a parent class because the parent class might perform essential initialization tasks
        #  that are required for the child class to function correctly.
        super.__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    def __str__(self):
        return self.error_message