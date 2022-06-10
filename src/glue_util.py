import logging
import boto3
from botocore.exceptions import ClientError


def get_glue_client(profile_name, region_name):
    print('get_glue_client: profile_name=%s, region_name=%s' % (profile_name, region_name))

    session = boto3.Session(profile_name=profile_name)
    glue = session.client('glue',
        region_name=region_name)
    return glue


def get_glue_session_ids(profile_name, region_name):
    glue_session_ids = []

    glue = get_glue_client(profile_name, region_name)
    if glue is None:
        print('get_glue_session_ids: Failed to get glue client.')
        return glue_session_ids

    try:
        response = glue.list_sessions()
        print('DEBUG: get_glue_session_ids: glue.list_sessions() response: %s' % (response))
        glue_session_ids = response['Ids']
        
    except ClientError as e:
        logging.error("get_glue_session_ids: unexpected error: ")
        logging.exception(e)
        return glue_session_ids

    return glue_session_ids


def delete_glue_sessions(profile_name, region_name, glue_session_ids_to_delete):
    glue = get_glue_client(profile_name, region_name)
    if glue is None:
        print('delete_glue_sessions: Failed to get glue client.')
        return False

    try:
        for glue_session_id_to_delete in glue_session_ids_to_delete:
            print('DEBUG: delete_glue_sessions: delete glue session: %s', glue_session_id_to_delete)
            glue.delete_session(Id=glue_session_id_to_delete)
    except ClientError as e:
        logging.error("delete_glue_sessions: unexpected error: ")
        logging.exception(e)
        return False

    return True

