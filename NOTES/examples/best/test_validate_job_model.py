from pydantic import BaseModel, Field

# Define a Data Model for validation
class JobPostModel(BaseModel):
    id: int
    title: str = Field(min_length=1)  # Validation logic included in the model
    is_active: bool

# Raw data to validate
job_post_data = {
    "id": 105,
    "title": "QA Automation Engineer",
    "is_active": True
}

# Validation occurs during object instantiation
job = JobPostModel(**job_post_data)

# Now you can use 'job' as an object with autocompletion
print(f"Validated job: {job.title}")