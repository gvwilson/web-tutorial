-- modify table with encrypted passwords
{% for item in data %}
UPDATE staff
SET password = "{{item.password}}"
WHERE (staff.staff_id = {{item.staff_id}});
{% endfor %}
