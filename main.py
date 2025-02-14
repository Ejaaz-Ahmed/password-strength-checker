from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware  # Add this import
from pydantic import BaseModel, Field, validator
import re
from typing import Dict
from enum import Enum
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Password Strength Checker API",
    description="An API to check password strength based on multiple criteria, created by Ejaz Ahmed",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class PasswordStrength(str, Enum):
    STRONG = "Strong"
    MODERATE = "Moderate"
    WEAK = "Weak"

class PasswordRequest(BaseModel):
    password: str = Field(..., min_length=1, max_length=100)

    @validator('password')
    def password_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Password cannot be empty or whitespace')
        return v

class PasswordResponse(BaseModel):
    strength: PasswordStrength
    details: Dict[str, bool]

class PasswordChecker:
    def __init__(self):
        self.MIN_LENGTH = 8
        self.SPECIAL_CHARS = r"[!@#$%^&*(),.?\":{}|<>]"

    def check_criteria(self, password: str) -> Dict[str, bool]:
        return {
            "length": len(password) >= self.MIN_LENGTH,
            "digits": any(char.isdigit() for char in password),
            "uppercase": any(char.isupper() for char in password),
            "lowercase": any(char.islower() for char in password),
            "special_chars": bool(re.search(self.SPECIAL_CHARS, password))
        }

    def calculate_strength(self, criteria: Dict[str, bool]) -> PasswordStrength:
        score = sum(criteria.values())
        if score == 5:
            return PasswordStrength.STRONG
        elif score >= 3:
            return PasswordStrength.MODERATE
        return PasswordStrength.WEAK

password_checker = PasswordChecker()

@app.get("/api/v1/check-password/", response_model=PasswordResponse)
async def check_password(
    password: str = Query(
        ...,
        min_length=1,
        max_length=100,
        description="Password to check strength"
    )
) -> PasswordResponse:
    """
    Check the strength of a password based on multiple criteria:
    - Minimum length of 8 characters
    - Contains at least one digit
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one special character
    """
    try:
        # Log the request (excluding the actual password)
        logger.info("Processing password strength check request")

        # Check password criteria
        criteria = password_checker.check_criteria(password)
        strength = password_checker.calculate_strength(criteria)

        # Log the result (excluding the actual password)
        logger.info(f"Password strength check completed: {strength}")

        return PasswordResponse(
            strength=strength,
            details=criteria
        )

    except Exception as e:
        logger.error(f"Error processing password strength check: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Error processing password strength check"
        )

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)