# This file exist solely for Pydentic validation. 
# So user's input verification while singing in and signing up should be here

from pydantic import BaseModel, EmailStr, Field, model_validator


# Class-helper which would do all the work of checking during signing up
class UserCreate(BaseModel):

    # This will automatically check wether user typed data is correctly formated
    # TODO: create some kind of handler so it displays normally on website
    #! Min and Max Values might and SHOULD be changed later, especially password's
    full_name: str = Field(..., min_length=3, max_length=100)
    username: str = Field(..., min_length=3, max_length=30, pattern=r"^[a-zA-Z0-9_]+$")
    email: EmailStr 
    password: str = Field(..., min_length=3, max_length=72)
    confirm_password: str


    # Checks if password and confirm_password are same
    @model_validator(mode='after')
    def check_passwords_match(self) -> 'UserCreate':

        if self.password != self.confirm_password:
            raise ValueError('Passwords do not match')
        
        return self
    
# Class-helper which would do all the work of checking during signing in
class UserLogin(BaseModel):



#* This might be usefule for TODO task above, but change the type of an error
# return RedirectResponse(
#             url="/signup?error=password_is_too_short",
#             status_code=status.HTTP_303_SEE_OTHER,
#         )