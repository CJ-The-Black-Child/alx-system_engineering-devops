This is continuation of shell permissions readme file
This is continuation of shell permissions readme file
0-iam_betty==> the script switches the current user to the user betty
1-who_am_i ==> the script prints the effective usernmae of the current user
2-groups==> the script prints all the groups the current user is part of
3-new_owner==> the script changes the owner of the file hello to the user betty
4-empty==> the script creates an empty file called hello
5-execute ==> the script adds execute permission to the owner of the file hello
6-multiple_permissions==> the script adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
7-everybody ==> the script adds execution permission to the owner, the group owner and the other users, to the file hello
8-James_Bond ==> the script sets the permission to the file hello as;
        owner: no permission at all
        group: no permission at all
        other users: all the permissions
9-John_Doe ==> the script sets the mode of the file hello to=rwxr -x-wx 1 julien julien 23 sep 20 14:25 hello
10-mirror_permissions ==> script that sets the mode of the file hello the same as olleh's mode
11-directories_permissions ==> the script adds execute permissions to all subdirectories of the current directory for the owner, the group owner and all other users
12-directory_permissions ==> the script creates a directory called my_dir with permissions 751 in the working directory
13-change_group ==> the script that changes the group owner to school for the file hello
100-change_owner_and_group ==> script that changes the owner to vincent and the group owner to staff for all the files and directories in the working directory
101-symbolic_link_permissions ==> the script that changes the owner and the group owner of _hello to vincent and staff respectively
102-if_only ==> the script that changes the owner of the file hello to betty oly if it is owned by the user guillaume
103-Star_Wars ==> the script that will play the starwars iv episode in the terminal

