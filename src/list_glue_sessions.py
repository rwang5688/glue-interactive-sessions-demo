import glue_util

def main():
    print('\nStarting list_glue_sessions.py ...')

    profile_name = 'default'
    region_name = 'us-west-2'
    glue_session_ids = glue_util.get_glue_session_ids(profile_name, region_name)
    num_glue_session_ids = len(glue_session_ids)

    print("glue_session_ids: ")
    print(glue_session_ids)
    print("Total # of Glue sessions: %d" % num_glue_session_ids)


if __name__ == '__main__':
    main()
