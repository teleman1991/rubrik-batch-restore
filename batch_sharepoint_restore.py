import rubrik_cdm

rubrik = rubrik_cdm.Connect(node_ip='my.rubrik.cluster')

sharepoint_sites = rubrik.get('v1', '/sharepoint/site')

for site in sharepoint_sites['data']:
    print('Restoring SharePoint site: {}'.format(site['name']))
    restore_job = rubrik.post('v1', '/sharepoint/site/{}/restore'.format(site['id'])) 
    print('Restore job started for {}, status: {}'.format(site['name'], restore_job['status']))
