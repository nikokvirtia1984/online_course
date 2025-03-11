from pydantic import BaseModel

class UserBase(BaseModel):
    username:str
    role:str
    
class UserCreate(UserBase):
    password:str
    
class User(UserBase):
    id:int
    
    class Cofig:
        orm_mode = True
        
class CourseBase(BaseModel):
    title: str
    description: str
    duration: int
    
class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int
    instructor_id: int
    
    class Cofig:
        orm_mode = True
        
class LessonBase(BaseModel):
    title: str
    content: str
    
class LessonCreate(LessonBase):
    course_id: int
    
    
class Lesson(LessonBase):
    id: int
    course_id: int
    
    class Cofig:
        orm_mode = True
        
class EnrelmentBase(BaseModel):
    user_id: int
    course_id: int
    progress: int
    
class EnrollmentCreate(EnrelmentBase):
    pass

class Enrollment(EnrelmentBase):
    id: int
    
    class Cofig:
        orm_mode = True