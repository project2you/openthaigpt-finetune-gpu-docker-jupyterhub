# User
c.Authenticator.allowed_users = {'user1','user2',}
# Admin
c.Authenticator.admin_users = {'ml','jhub'}
c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.admin_access = True
c.NotebookApp.allow_origin = '*' #allow all origins
c.NotebookApp.ip = '0.0.0.0' # listen on all IPs
c.NotebookApp.allow_remote_access = True
