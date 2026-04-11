class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')
        final_list = []
        for individual_path in path_list:
            if len(individual_path) == 0:
                continue
            if individual_path not in ('..', '.'):
                final_list.append(individual_path)
            else:
                if individual_path == '..' and len(final_list) != 0:
                    final_list.pop()
        
        return '/' + '/'.join(x for x in final_list)