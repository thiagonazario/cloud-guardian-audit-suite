import os
from google.cloud import compute_v1
from google.cloud import run_v2
from utils.logger import logger

def scan_gcp_waste(project_id):
    logger.info(f"Starting GCP Audit for Project: {project_id}")

    # 1. Auditoria de Instâncias Compute Engine (VMs)
    try:
        logger.info("Checking for Idle or Stopped VMs...")
        instance_client = compute_v1.InstancesClient()
        request = compute_v1.AggregatedListInstancesRequest(project=project_id)
        
        vm_count = 0
        for zone, response in instance_client.aggregated_list(request=request):
            if response.instances:
                for instance in response.instances:
                    if instance.status != "RUNNING":
                        logger.warning(f"Idle VM Detected: {instance.name} | Status: {instance.status} | Zone: {zone.split('/')[-1]}")
                        vm_count += 1
        
        if vm_count == 0:
            logger.info("No idle VMs found.")
    except Exception as e:
        logger.error(f"Failed to audit Compute Engine: {e}")

    # 2. Auditoria de Cloud Run Jobs
    try:
        logger.info("Analyzing Cloud Run Jobs...")
        run_client = run_v2.JobsClient()
        parent = f"projects/{project_id}/locations/-"
        
        jobs = run_client.list_jobs(parent=parent)
        job_count = 0
        for job in jobs:
            # Lógica para ver se o job falhou ultimamente
            logger.info(f"Monitoring Job: {job.name.split('/')[-1]} | Last Update: {job.update_time}")
            job_count += 1
        
        if job_count == 0:
            logger.info("No Cloud Run jobs identified.")
    except Exception as e:
        logger.error(f"Failed to audit Cloud Run: {e}")

    logger.info("GCP Scan Complete.")

if __name__ == "__main__":
    # Pega o ID do projeto via variável de ambiente para ser seguro
    PROJECT = os.getenv("GCP_PROJECT_ID", "your-project-id-here")
    scan_gcp_waste(PROJECT)