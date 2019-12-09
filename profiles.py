# project and region name keypair values.
# Project_Name: Region_name
regions_name_hash = {'<Project_Name>': '<Region_Name>', 'Jenkin-Prod': 'AS-H'}


def profile_maker(profile, username, password):
    """
    This method is similar to switch statement. It will render the dict with the given data and
    returns the matched profile name
    :param profile: Name of the profile to return.
    :param username: Username to authenticate OpenStack.
    :param password: Password to Authenticate Openstack.
    :return: Dict: Matched profile name.
    """
    return {
        'AS-D-RDK-Jenkins-PROD': {
            'auth_url': '',
            'username': username,
            'password': password,
            'project_id': '',
            'project_name': '',
            'user_domain_name': '',
        },
        'AS-D-RDK': {
            'auth_url': '',
            'username': username,
            'password': password,
            'project_id': '',
            'project_name': '',
            'user_domain_name': '',
        }
    }[profile]
