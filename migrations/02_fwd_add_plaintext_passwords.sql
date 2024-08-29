BEGIN TRANSACTION;

-- Check if the username column exists, if not, add it
SELECT CASE
    WHEN COUNT(*) = 0 THEN
        'ALTER TABLE staff ADD COLUMN username TEXT NOT NULL DEFAULT ""'
    ELSE
        'SELECT 1' -- Do nothing
END
FROM pragma_table_info('staff')
WHERE name = 'username';

-- Check if the password column exists, if not, add it
SELECT CASE
    WHEN COUNT(*) = 0 THEN
        'ALTER TABLE staff ADD COLUMN password TEXT NOT NULL DEFAULT ""'
    ELSE
        'SELECT 1' -- Do nothing
END
FROM pragma_table_info('staff')
WHERE name = 'password';

-- Update data
WITH new_data(staff_id, username, password) AS (VALUES
  (1, "vello.p", "8375"),
  (2, "viktoria.h", "3410"),
  (3, "linda.m", "0680"),
  (4, "sergey.r", "7761"),
  (5, "anu.v", "5181"),
  (6, "maria.k", "0227"),
  (7, "laura.m", "3783")
)
UPDATE staff
SET username = new_data.username, password = new_data.password
FROM new_data
WHERE (staff.staff_id = new_data.staff_id);

COMMIT;

