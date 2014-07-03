from boto.ec2 import connect_to_region
from boto.ec2.blockdevicemapping import BlockDeviceType, BlockDeviceMapping

conn = connect_to_region('us-west-2')
dev_sda1 = BlockDeviceType(delete_on_termination=True)
bdm = BlockDeviceMapping()
bdm['/dev/sda1'] = dev_sda1
reservation = conn.request_spot_instances(price='0.010', image_id='ami-6aad335a', count=1, key_name='data-extraction', security_groups=['sshable'], instance_type='t1.micro', block_device_map=bdm)

