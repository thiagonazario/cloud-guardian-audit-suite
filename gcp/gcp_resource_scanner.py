from google.cloud import compute_v1
from google.cloud import run_v2

def scan_gcp_waste(project_id):
    print("\n" + "="*40)
    print(f"🔍 CLOUD GUARDIAN: GCP AUDIT - Project: {project_id}")
    print("="*40)

    # 1. Auditoria de Instâncias Compute Engine (VMs)
    print("\nChecking for Idle VMs...")
    instance_client = compute_v1.InstancesClient()
    # Lista todas as instâncias em todas as zonas
    request = compute_v1.AggregatedListInstancesRequest(project=project_id)
    
    vm_count = 0
    for zone, response in instance_client.aggregated_list(request=request):
        if response.instances:
            for instance in response.instances:
                # Se a instância não estiver 'RUNNING', ela pode estar custando storage desnecessário
                if instance.status != "RUNNING":
                    print(f"⚠️  [WASTE] VM: {instance.name} | Status: {instance.status} | Zone: {zone.split('/')[-1]}")
                    vm_count += 1
    
    if vm_count == 0:
        print("✅ All VMs are active or none found.")

    # 2. Auditoria de Cloud Run Jobs
    print("\nChecking Cloud Run Jobs Status...")
    run_client = run_v2.JobsClient()
    parent = f"projects/{project_id}/locations/-" # '-' busca em todas as regiões
    
    try:
        jobs = run_client.list_jobs(parent=parent)
        job_count = 0
        for job in jobs:
            print(f"ℹ️  [MONITOR] Job: {job.name.split('/')[-1]} | Last Update: {job.update_time}")
            job_count += 1
        
        if job_count == 0:
            print("✅ No Cloud Run jobs found.")
    except Exception as e:
        print(f"❌ Could not audit Cloud Run: {e}")

    print("\n" + "="*40)
    print("GCP SCAN COMPLETE")

if __name__ == "__main__":
    # Substitua pelo seu Project ID ou use via variável de ambiente
    import os
    MY_PROJECT = os.getenv("GCP_PROJECT_ID", "your-project-id-here")
    scan_gcp_waste(MY_PROJECT)