import requests
import json
import csv

url = 'https://nkb-backend-ccbp-prod-apis.ccbp.in/api/nkb_resources/user/course_details/v2/'

headers = {
    "authority": "nkb-backend-ccbp-prod-apis.ccbp.in",
    "accept": "application/json",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "authorization": "Bearer gEBLxQ9lUBuTXC0iav0FPgM1XRW6MA",
    "content-type": "application/json",
    "origin": "https://learning.ccbp.in",
    "referer": "https://learning.ccbp.in/",
    "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Linux\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "x-app-version": "173",
    "x-browser-session-id": "035870d8-0bf4-4d6d-9022-f2c2934d8ed9",
}

# data = {"data":"\"{\\\"course_id\\\":\\\"6d41f350-76d5-4337-9be0-3fe0b26b1b26\\\",\\\"is_session_plan_details_required\\\":false,\\\"is_certification_details_required\\\":false}\"","clientKeyDetailsId":1}

# data = {"data":"\"{\\\"course_id\\\":\\\"62e43c70-ee74-4afe-8d1c-26ca9c22947a\\\",\\\"is_session_plan_details_required\\\":false,\\\"is_certification_details_required\\\":false}\"","clientKeyDetailsId":1}

# data = {"data":"\"{\\\"course_id\\\":\\\"c6008f8d-cd91-4843-bb3f-b75d4beca046\\\",\\\"is_session_plan_details_required\\\":false,\\\"is_certification_details_required\\\":false}\"","clientKeyDetailsId":1}

# data = {"data":"\"{\\\"course_id\\\":\\\"e26f4aad-99d4-4a72-b3d8-b66d3fef182a\\\",\\\"is_session_plan_details_required\\\":false,\\\"is_certification_details_required\\\":false}\"","clientKeyDetailsId":1}

# data = {"data":"\"{\\\"course_id\\\":\\\"41d81d4f-5c52-4a0a-a2a4-84c02f8f333b\\\",\\\"is_session_plan_details_required\\\":false,\\\"is_certification_details_required\\\":false}\"","clientKeyDetailsId":1}

# data = {"data":"\"{\\\"course_id\\\":\\\"ad3fd68a-4e7e-4fa3-97bf-1b41dbabb88c\\\",\\\"is_session_plan_details_required\\\":false,\\\"is_certification_details_required\\\":false}\"","clientKeyDetailsId":1}

data = {"data":"\"{\\\"course_id\\\":\\\"02d2b040-5272-40c8-aa44-83896b54643b\\\",\\\"is_session_plan_details_required\\\":false,\\\"is_certification_details_required\\\":false}\"","clientKeyDetailsId":1}

response = requests.post(url, headers=headers, data=json.dumps(data))

# Initialize an empty list to hold unit dictionaries
unit_details_list = []

# Check if the response is OK and if it contains the topics key
if response.status_code == 200:
    response_json = response.json()

    # Extract the course title from the response
    course_name = response_json.get('course_title', "Your Course Name")  # Update to extract course title

    # Check if 'topics' exists and is not empty
    if 'topics' in response_json and len(response_json['topics']) > 0:
        # Loop through all topics in the course
        for topic in response_json['topics']:
            topic_name = topic.get('topic_name')  # Get the topic name for the current topic
            units = topic.get('units', [])

            print(f"Processing Topic: {topic_name}")

            # Initialize session count for the current topic
            current_part = 0  # To track the current part number

            # Loop through all units for the current topic
            for unit in units:
                unit_id = unit.get('unit_id')
                unit_type = unit.get('unit_type')
                unit_name = None

                # Check for various unit types and extract names accordingly
                if unit.get('learning_resource_set_unit_details'):
                    unit_name = unit['learning_resource_set_unit_details'].get('name')
                    # Determine Type for LEARNING_SET
                    if any(keyword in unit_name.lower() for keyword in ["cheatsheet", "cheat sheet", "reading material", "readingmaterial"]):
                        unit_type_value = "Reading Material"
                    else:
                        unit_type_value = "Session"
                elif unit.get('exam_unit_details'):
                    unit_name = unit['exam_unit_details'].get('name')
                    # Determine Type for EXAM
                    if any(quiz_name in unit_name for quiz_name in ["Class Room Quiz", "Classroom Quiz"]):
                        unit_type_value = "Quiz"
                    else:
                        unit_type_value = "Exam"
                elif unit.get('practice_unit_details'):
                    unit_name = unit['practice_unit_details'].get('name')
                    unit_type_value = "Practice"
                elif unit.get('question_set_unit_details'):
                    unit_name = unit['question_set_unit_details'].get('title')
                    unit_type_value = "Practice"
                elif unit.get('project_unit_details'):
                    unit_name = unit['project_unit_details'].get('name')
                    unit_type_value = "Project"
                elif unit.get('assignment_unit_details'):
                    unit_name = unit['assignment_unit_details'].get('name')
                    unit_type_value = "Assignment"
                elif unit.get('coding_contest_unit_details'):
                    unit_name = unit['coding_contest_unit_details'].get('name')
                    unit_type_value = "Coding Contest"
                elif unit.get('adaptive_video_question_set_details'):
                    unit_name = unit['adaptive_video_question_set_unit_details'].get('name')
                    unit_type_value = "Adaptive Video"
                elif unit.get('assessment_unit_details'):  # Added check for ASSESSMENT
                    unit_name = unit['assessment_unit_details'].get('name', "Unnamed Assessment")
                    unit_type_value = "Quiz"

                # Determine Class / Practice based on Type and Unit Name
                if unit_type_value in ["Session", "Reading Material"]:
                    class_practice_value = "Class"
                    if unit_type_value == "Session":
                        current_part += 1  # Increment part count for new session
                elif unit_type_value == "Quiz" and any(quiz_name in unit_name for quiz_name in ["Class Room Quiz", "Classroom Quiz"]):
                    class_practice_value = "Class"
                elif unit_type_value == "Practice":
                    class_practice_value = "Practice"
                elif unit_type_value == "Quiz" and "Daily Quiz" in unit_name:
                    class_practice_value = "N/A"
                else:
                    class_practice_value = ""  # Default to empty if none of the conditions match

                # Add the unit details as a dictionary to the list
                unit_details_list.append({
                    "unit_id": unit_id,
                    "unit_type": unit_type_value,  # Use the determined type
                    "title": unit_name if unit_name else "Unnamed Unit",  # Use a default value if unit_name is None
                    "class_practice": class_practice_value,  # Include Class / Practice value
                    "part": current_part,  # Include the current part number
                    "topic": topic_name  # Include the topic name for each unit
                })

        # Write to CSV file
        with open('course_details.csv', mode='w', newline='') as csv_file:
            fieldnames = ['Track', 'Course', 'Topic', 'Part', 'Class / Practice', 'Session Name', 'Type', 'Unit IDs']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()  # Write the header

            for unit in unit_details_list:
                writer.writerow({
                    'Track': '',  # Keep empty
                    'Course': course_name,  # Use extracted course title
                    'Topic': unit['topic'],  # Use the correct topic name for each unit
                    'Part': unit['part'],  # Use the current part number
                    'Class / Practice': unit['class_practice'],  # Use the determined Class / Practice value
                    'Session Name': unit['title'],  # Keep the unit names one by one
                    'Type': unit['unit_type'],  # Include unit type
                    'Unit IDs': unit['unit_id'],  # Keep unit IDs
                })

    else:
        print("No topics available in the response.")
else:
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")

# Output the gathered unit details in the required format
print(json.dumps(unit_details_list, indent=2))