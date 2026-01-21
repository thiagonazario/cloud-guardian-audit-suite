import boto3
from utils.logger import logger

def scan_aws_waste():
    ec2 = boto3.resource('ec2')
    
    logger.info("Starting AWS Waste Scan...")

    # Volumes
    volumes = ec2.volumes.filter(Filters=[{'Name': 'status', 'Values': ['available']}])
    vol_count = 0
    for vol in volumes:
        logger.warning(f"Unattached Volume Found: {vol.id} ({vol.size}GB)")
        vol_count += 1
    
    if vol_count == 0:
        logger.info("No unattached volumes found.")

    # Instâncias
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])
    for inst in instances:
        logger.info(f"Optimization Candidate: Stopped instance {inst.id}")

    logger.info("AWS Scan Complete.")

if __name__ == "__main__":
    scan_aws_waste()