from core.constants import Constants

def get_node_parent(folder_path):
    if(folder_path and folder_path.strip()):
        slash_index = -1
        try:
            slash_index = folder_path.rindex(Constants.SEPARATOR)
        except:
            slash_index = -1

        if(slash_index !=-1):
            return folder_path[0:slash_index]

    else:
        return ""

def append_unix_slash(path):
    path_length = len(path)
    slash_index = -1
    try:
        slash_index = path.rindex(Constants.SEPARATOR)
    except:
        slash_index = -1
    if(slash_index !=-1 and slash_index!=(path_length-1)):
        return path[0:] + str(Constants.SEPARATOR)
    else:
        return path

def append_path(path, path_to_append):
    if(path_to_append.startswith(Constants.SEPARATOR)):
        path_to_append = path_to_append[1:]
    return str(append_unix_slash(path)) + str(path_to_append)

