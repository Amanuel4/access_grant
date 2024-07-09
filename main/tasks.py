from django.utils import timezone
from datetime import datetime
from celery import shared_task
import ansible_runner
import subprocess
from .models import AccessGrantTable 
import os
import yaml


playbook_path = '../ansible'
@shared_task
def grant_access_task(usernames, identifier):
    
    if identifier == 'user':   
        playbook_path = 'ansible/grant_access_user.yml'
        
    elif identifier == 'group':
        playbook_path = 'ansible/grant_access_group.yml'
        
        
    ansible_command = f"ansible-playbook {playbook_path} -e username={usernames} -i=inventory "
    result = subprocess.run(ansible_command, shell=True, check=True) 
    

@shared_task
def revoke_access_task():
    now = timezone.now()
    expired_users = AccessGrantTable.objects.filter(expiry_date__lte= now)
    

    
    usernames = [users.user for users in expired_users]
    if usernames:
        
        with open('vars.yml', 'w') as f:
            yaml.dump({'usernames': usernames}, f)
            
            
        playbook_path = 'ansible/revoke_access.yml'
        ansible_command = f"ansible-playbook {playbook_path} -i=ansible/inventory"
        result = subprocess.run(ansible_command, shell=True, check=True) 
    
    
        

        



