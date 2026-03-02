# # Real Playwright-like logic
# rows = [{"name": "Mikhail", "status": "New"}, {"name": "John", "status": "Rejected"}]
#
# for row in rows:
#     if row["status"] == "Rejected":
#         # Logic to click delete button for this specific person
#         print(f"Clicking delete for {row['name']}")


# candidate_id = response["data"]["candidate_id"]
# assert isinstance(candidate_id, int)
# assert candidate_id is not None

# expected_status = "Active"
# actual_status = "Inactive"
#
# assert actual_status != expected_status
# # print("passed")

expected_status = "Active"
actual_status = "Active"

if actual_status == expected_status:
    print(f"PASSED: Status is correctly set to {actual_status}")

assert actual_status != expected_status


