import boto3

def scan_aws_waste():
    # Conectando ao recurso EC2
    ec2 = boto3.resource('ec2')
    
    print("\n" + "="*40)
    print("🔍 CLOUD GUARDIAN: AWS WASTE SCAN")
    print("="*40)

    # 1. Volumes EBS Disponíveis (não anexados = desperdício total)
    print("\nChecking for Unattached EBS Volumes...")
    volumes = ec2.volumes.filter(Filters=[{'Name': 'status', 'Values': ['available']}])
    vol_count = 0
    for vol in volumes:
        print(f"⚠️  [WASTE] Volume ID: {vol.id} | Size: {vol.size}GB | Status: {vol.state}")
        vol_count += 1
    
    if vol_count == 0:
        print("✅ No unattached volumes found.")

    # 2. Instâncias Paradas (ocupando IP e Storage)
    print("\nChecking for Stopped Instances...")
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])
    inst_count = 0
    for inst in instances:
        print(f"ℹ️  [ADVICE] Instance ID: {inst.id} is STOPPED. Consider terminating if not needed.")
        inst_count += 1

    if inst_count == 0:
        print("✅ No stopped instances to report.")
    
    print("\n" + "="*40)
    print("SCAN COMPLETE")

if __name__ == "__main__":
    scan_aws_waste()