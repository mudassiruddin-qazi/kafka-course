nano generate_semi_structured.sh
chmod +x generate_semi_structured.sh
./generate_semi_structured.sh
-----------------------------Error-----------------
Traceback (most recent call last):
  File "<stdin>", line 22, in <module>
PermissionError: [Errno 13] Permission denied: '/data/semi-structure/student_data_1.json'
Current size: 1 MB
Traceback (most recent call last):
  File "<stdin>", line 22, in <module>
PermissionError: [Errno 13] Permission denied: '/data/semi-structure/student_data_2.json'
Current size: 1 MB
Traceback (most recent call last):
  File "<stdin>", line 22, in <module>
PermissionError: [Errno 13] Permission denied: '/data/semi-structure/student_data_3.json'
Current size: 1 MB
Traceback (most recent call last):
-----------------------------Error-----------------
sudo mkdir -p /data/semi-structure
sudo chown $USER:$USER /data/semi-structure
