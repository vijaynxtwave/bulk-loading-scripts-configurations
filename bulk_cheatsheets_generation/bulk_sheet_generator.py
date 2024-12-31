import json
import uuid
import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
import glob

def authenticate_and_create_sheet(sheet_name):
    credentials_path = os.path.join(os.path.dirname(__file__), 'credentials.json')
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
    client = gspread.authorize(creds)
    sheet = client.create(sheet_name)
    sheet.share(None, perm_type='anyone', role='writer')
    return sheet

def update_resourcesdata_subsheet(sheet, learning_resource_ids, common_parent_id):
    try:
        resourcesdata_subsheet = sheet.worksheet("ResourcesData")
    except gspread.exceptions.WorksheetNotFound:
        resourcesdata_subsheet = sheet.add_worksheet(title="ResourcesData", rows="1000", cols="20")
    
    resourcesdata_subsheet.clear()
    
    # Add headers in row 1
    headers = [
        "resource_id", "resource_type", "dependent_resource_count", 
        "dependent_resources", "dependent_reason_display_text",
        "parent_resource_count", "child_order", "parent_resources",
        "auto_unlock"
    ]
    resourcesdata_subsheet.update('A1:I1', [headers])
    
    # Prepare batch updates
    all_values = []
    for index, resource_id in enumerate(learning_resource_ids, 1):
        # Main resource data row
        main_row = [resource_id, 'UNIT', '0', '', '', '1', '', '', 'TRUE']
        # Child order and parent resources row
        child_row = ['', '', '', '', '', '', str(index), common_parent_id, '']
        all_values.extend([main_row, child_row])
    
    if all_values:
        # Update all rows at once starting from A2
        resourcesdata_subsheet.update(f'A2:I{len(all_values)+1}', all_values)

def update_units_subsheet(sheet, learning_resource_ids):
    try:
        units_subsheet = sheet.worksheet("Units")
    except gspread.exceptions.WorksheetNotFound:
        units_subsheet = sheet.add_worksheet(title="Units", rows="1000", cols="20")
    
    units_subsheet.clear()
    
    # Add headers in row 1
    headers = ["unit_id", "common_unit_id", "unit_type", "duration_in_sec", "tags"]
    units_subsheet.update('A1:E1', [headers])
    
    # Prepare batch updates
    all_values = []
    for resource_id in learning_resource_ids:
        row = [
            resource_id,                # unit_id (same as ResourcesData)
            str(uuid.uuid4()),         # common_unit_id (new UUID)
            'LEARNING_SET',            # unit_type
            '1200',                    # duration_in_sec
            'MOCK_TEST_EVALUATION'     # tags
        ]
        all_values.append(row)
    
    if all_values:
        # Update all rows at once starting from A2
        units_subsheet.update(f'A2:E{len(all_values)+1}', all_values)

def convert_to_pascal_case(filename):
    # Remove the .md extension if present
    filename = filename.replace('.md', '')
    
    # Replace hyphens with spaces and split
    words = filename.replace('-', ' ').split()
    
    # Capitalize each word and join them with spaces
    pascal_case = ' '.join(word.capitalize() for word in words)
    
    return pascal_case

def read_md_files(input_folder):
    projects_data = []
    md_files = glob.glob(os.path.join(input_folder, "*.md"))
    
    # Debug: Print the list of markdown files found
    print("Markdown files found:", md_files)
    
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            title = content.split('\n')[0].replace('#', '').strip()
            file_name = os.path.basename(md_file)  # Get the file name
            pascal_name = convert_to_pascal_case(file_name)  # Convert to Pascal case
            projects_data.append({
                "title": title,
                "content": content,
                "file_name": pascal_name  # Use the Pascal case version
            })
    
    return projects_data

def update_learningresourceset_subsheet(sheet, learning_resource_ids, projects_data):
    try:
        lrs_subsheet = sheet.worksheet("LearningResourceSet")
    except gspread.exceptions.WorksheetNotFound:
        lrs_subsheet = sheet.add_worksheet(title="LearningResourceSet", rows="1000", cols="20")
    
    lrs_subsheet.clear()
    
    # Add headers in row 1
    headers = [
        "learning resource set id", "learning resource set name",
        "learning resources count", "learning resource ids", "order"
    ]
    lrs_subsheet.update(values=[headers], range_name='A1:E1')
    
    # Prepare batch updates and store UUIDs
    all_values = []
    learning_resource_uuids = []  # Store UUIDs for LearningResources
    
    for resource_id, project in zip(learning_resource_ids, projects_data):
        # Generate UUID for this resource
        resource_uuid = str(uuid.uuid4())
        learning_resource_uuids.append(resource_uuid)
        
        # Main row with resource ID and file name
        main_row = [
            resource_id,              # Same UUID as ResourceData
            project["file_name"],     # Use file name instead of title
            '1',                      # learning resources count
            '',                       # learning resource ids (empty)
            ''                        # order (empty)
        ]
        # Secondary row with UUID and order starting from 70
        secondary_row = [
            '',                       # empty
            '',                       # empty
            '',                       # empty
            resource_uuid,           # Store UUID for reference
            1                  # order starts from 70
        ]
        all_values.extend([main_row, secondary_row])
    
    if all_values:
        # Update all rows at once starting from A2
        lrs_subsheet.update(values=all_values, range_name=f'A2:E{len(all_values)+1}')
    
    return learning_resource_uuids  # Return UUIDs for LearningResources

def update_learningresources_subsheet(sheet, learning_resource_uuids, projects_data):
    try:
        lr_subsheet = sheet.worksheet("LearningResources")
    except gspread.exceptions.WorksheetNotFound:
        lr_subsheet = sheet.add_worksheet(title="LearningResources", rows="1000", cols="20")
    
    lr_subsheet.clear()
    
    # Add headers in row 1
    headers = [
        "learning_resource_uuid", "Title", "Content", "content_format",
        "content_language", "multimedia_count", "multimedia_format",
        "total_duration", "multimedia_url", "thumbnail_url", "highlights_count",
        "duration in sec", "content", "title", "learning_resource_type"
    ]
    lr_subsheet.update(values=[headers], range_name='A1:O1')
    
    # Prepare batch updates using UUIDs from LearningResourceSet
    all_values = []
    for uuid, project in zip(learning_resource_uuids, projects_data):
        row = [
            uuid,               # Use UUID from LearningResourceSet D column
            '',                 # Title
            project["content"], # Content from project
            'MARKDOWN',         # content_format
            'ENGLISH',         # content_language
            '0',               # multimedia_count
            '',                # multimedia_format
            '',                # total_duration
            '',                # multimedia_url
            '',                # thumbnail_url
            '0',               # highlights_count
            '1200',            # duration in sec
            '',                # content
            '',                # title
            'DEFAULT'          # learning_resource_type
        ]
        all_values.append(row)
    
    if all_values:
        # Update all rows at once starting from A2
        lr_subsheet.update(values=all_values, range_name=f'A2:O{len(all_values)+1}')

def main():
    input_folder = "Cheatsheets_data"
    projects_data = read_md_files(input_folder)
    
    # Debug: Print projects data
    print("Projects Data:", projects_data)
    
    # Change chunk size from 5 to 9
    chunk_size = 6  # Updated from 5 to 9
    project_chunks = [projects_data[i:i + chunk_size] for i in range(0, len(projects_data), chunk_size)]
    
    sheet_links = []
    
    for index, project_chunk in enumerate(project_chunks):
        sheet_name = f"Tutorial_Sheet_Bulk_{index + 1}_{str(uuid.uuid4())}"
        sheet = authenticate_and_create_sheet(sheet_name)
        
        # Generate resource IDs for each project in the chunk
        learning_resource_ids = [str(uuid.uuid4()) for _ in project_chunk]
        
        # Debug: Print learning resource IDs
        print("Learning Resource IDs:", learning_resource_ids)
        
        # Generate common parent ID
        common_parent_id = '5ea7bdb5-f9b5-4860-8a82-0be97e381758'
        
        # Update sheets and get the learning resource UUIDs
        update_resourcesdata_subsheet(sheet, learning_resource_ids, common_parent_id)
        update_units_subsheet(sheet, learning_resource_ids)
        learning_resource_uuids = update_learningresourceset_subsheet(sheet, learning_resource_ids, project_chunk)
        
        # Use the returned UUIDs for LearningResources
        update_learningresources_subsheet(sheet, learning_resource_uuids, project_chunk)
        
        # Share the sheet
        email_list = [
            'learningresource@nkblearningbackend.iam.gserviceaccount.com',
            'varaprasad.vajrapu@nxtwave.co.in',
            'vijay.padala@nxtwave.co.in'
        ]
        for email in email_list:
            sheet.share(email, perm_type='user', role='writer')
        
        # Collect the sheet link
        sheet_links.append(sheet.url)
    
    # Print all sheet links
    for link in sheet_links:
        print(f"Google Sheet created: {link}")

if __name__ == "__main__":
    main() 