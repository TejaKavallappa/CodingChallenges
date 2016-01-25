import re
filename = "/Users/teja2/Documents/teja_coding/CodingChallenges/UserPermission/test_userPermission.txt"

rights = {0:"x",1:"g", 2:"w", 3:"gw", 4:"r", 5:"gr", 6:"rw",7:"grw"}
rights_single = {"g":1,"w":2,"r":4}
with open(filename) as f:
    for test in f:
        if test == "\n":
            continue
        file_permissions = [[7,3,0],[6,2,4],[5,1,5],[3,7,1],[6,0,3],[4,2,6]]
        commands = test.split()
        result = True
        for command in commands:
            command = command.split('=>')
            user = int(command[0][-1])
            file_num = int(command[1][-1])
            action = command[2]
            action_num = file_permissions[user-1][file_num-1]
            if (action_num in rights):
                if action[0] not in rights[action_num]:
                    result = (result and False)
                    break
            if (result == True and len(command)>3):
                user2 = int(command[4][-1])
                if (command[3][0] in rights[file_permissions[user2-1][file_num-1]]):
                    print "Already have permission"
                else:
                    new_perm = (command[3][0] + rights[file_permissions[user2-1][file_num-1]])
                    new_perm = re.sub(r"x","",new_perm)
                    file_permissions[user2-1][file_num-1] += rights_single[command[3][0]]
        print result
