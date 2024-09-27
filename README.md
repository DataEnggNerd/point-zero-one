# .01

```py title="me.py"
from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr, HttpUrl

class SelfIntroduction(BaseModel):
    full_name: str = Field(..., default="Santhosh Solomon")
    current_work: str = Field(..., default="Data Engineering @ Advarisk")
    location: Optional[str] = Field(None, default="Pune, India")
    email: Optional[EmailStr] = Field(None, default="solomon.santhosh@gmail.com")
    website: Optional[HttpUrl] = Field(None, default="https://thedataengineer.substack.com")
    skills: List[str] = Field(..., default=["Python", "requests", "Pydantic", "Polars", "SQL", "Git"])
    current_interest: List[str] = Field(..., default=["Rustification of Python", "Data Engineering", "Developer tools"])
    interests: List[str] = Field(description="Topics I am interested in exploring and working on",
                            default=["Web Scraping", "Backend Engineering", "Databases", "Developer tools"])
```