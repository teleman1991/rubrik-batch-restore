import rubrik_cdm

rubrik = rubrik_cdm.Connect(node_ip='my.rubrik.cluster')

SHAREPOINT_TENANT = 'compassdatacenter.sharepoint.com'

sharepoint_sites = rubrik.get('v1', '/sharepoint/site', params={'detail': 'true'})

for site in sharepoint_sites['data']:
    if SHAREPOINT_TENANT in site['url']:
        print('Restoring SharePoint site: {}'.format(site['name']))
        restore_job = rubrik.post('v1', '/sharepoint/site/{}/restore'.format(site['id'])) 
        print('Restore job started for {}, status: {}'.format(site['name'], restore_job['status']))
    else:
        print('Skipping site not in tenant: {}'.format(site['name']))
