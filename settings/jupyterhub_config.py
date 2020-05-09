import os

# Grant admin users permission to access single-user servers.
#
#  Users should be properly informed if this is enabled.
c.JupyterHub.admin_access = False

# Allow named single-user servers per user
c.JupyterHub.allow_named_servers = False

# Class for authenticating users.
c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'

# The base URL of the entire application
#c.JupyterHub.base_url = '/'

# Whether to shutdown the proxy when the Hub shuts down.
c.JupyterHub.cleanup_proxy = True

# Whether to shutdown single-user servers when the Hub shuts down.
c.JupyterHub.cleanup_servers = True

# The public facing ip of the whole application (the proxy)
c.JupyterHub.ip = '0.0.0.0'

# The public facing port of the proxy
c.JupyterHub.port = 8000

# Purge and reset the database.
#c.JupyterHub.reset_db = False
c.JupyterHub.reset_db = True

# The URL the single-user server should start in.
c.Spawner.default_url = '/lab'

# Whitelist of environment variables for the single-user server to inherit from
#  the JupyterHub process.
c.Spawner.env_keep = [
    'PATH',
    'PYTHONPATH',
    'CONDA_ROOT',
    'CONDA_DEFAULT_ENV',
    'VIRTUAL_ENV',
    'LANG',
    'LC_ALL',
    'JAVA_HOME',
    'M2_HOME',
]

# Path to the notebook directory for the single-user server.
c.Spawner.notebook_dir = '~'

c.LDAPAuthenticator.server_address = os.getenv('OPENLDAP_HOST', '127.0.0.1')
c.LDAPAuthenticator.server_port = int(os.getenv('OPENLDAP_PORT', '389'))
c.LDAPAuthenticator.lookup_dn = bool(os.getenv('OPENLDAP_LOOKUP_DN', 'True'))
c.LDAPAuthenticator.use_ssl = bool(os.getenv('OPENLDAP_SSL', 'False'))
c.LDAPAuthenticator.lookup_dn_search_filter = '({login_attr}={login})'
c.LDAPAuthenticator.lookup_dn_user_dn_attribute = 'cn'
c.LDAPAuthenticator.lookup_dn_search_user = os.getenv(
    'OPENLDAP_SEARCH_USER', 'cn=admin,ou=users,dc=example,dc=com')
c.LDAPAuthenticator.lookup_dn_search_password = os.getenv(
    'OPENLDAP_SEARCH_PASSWORD', 'admin')
c.LDAPAuthenticator.bind_dn_template = os.getenv(
    'OPENLDAP_DN_TEMPLATE', 'uid={username},ou=users,dc=example,dc=com')
c.LDAPAuthenticator.allowed_groups = [
    os.getenv('OPENLDAP_GROUP', 'cn=jupyterhub,ou=groups,dc=mycompany,dc=net')]
c.LDAPAuthenticator.user_search_base = os.getenv(
    'OPENLDAP_BASE', 'ou=users,dc=example,dc=com')
c.LDAPAuthenticator.user_attribute = os.getenv('OPENLDAP_USER_ATTR', 'uid')
