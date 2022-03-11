import glue_util

def main():
    print('\nStarting delete_glue_sessions.py ...')

    profile_name = 'default'
    target_region = 'us-west-2'
    glue_session_ids = glue_util.get_glue_session_ids(profile_name, target_region)
    num_glue_session_ids = len(glue_session_ids)

    print("glue_session_ids: ")
    print(glue_session_ids)
    print("Total # of Glue sessions: %d" % num_glue_session_ids)

    # confirm with user
    print('\nDelete for profile_name=%s in target_region=%s: %d sessions.' \
        % (profile_name, target_region, num_glue_session_ids))
    while True:
        user_input = input('Confirm? [Y/N] ')
        if user_input.lower() in ('y', 'yes'):
            break
        elif user_input.lower() in ('n', 'no'):
            print('Cancelled per user request.  Exit.')
            return
        else:
            print(f'Error: Input {user_input} unrecognised.  Please try again.')

    print("\nStarting deletion ...")
    success = glue_util.delete_glue_sessions(profile_name, target_region, glue_session_ids)
    if not success:
        print('delete_glue_sessions failed.  Exit.')
        return      
    print("\nDeletion completed.")


if __name__ == '__main__':
    main()
