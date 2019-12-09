# openstack-volume-snapshot
Perform regular backup's of openstack volume and instance with the help of openstack SDK.

In order the script to work, VM should be populated with necessary metadata.
1. Backup_VM : Yes | yes 
2. Frequency : Daily | Monthly | Monthly_Twice
3. Backup_Time : HH
4. Image_Snapshot_Backup : Yes | yes 
4a. backup_type : Image_Snapshot
5. Volume_Snapshot_Backup : Yes | yes 
5a. backup_type : Volume_Snapshot
6. Volumes : Volume ID's for single instance
7. Retention_Count : Snapshot retention number

Requirements:
pip install openstackclient

Usage:
python openstack_create_image.py  --Username 'username' --Password 'password'

