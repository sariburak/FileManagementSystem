# File Management System
<p>A mere imitation of the file interaction system of Linux. This project has been made for a school homework and includes imitations of the cd, cp, rm, rmdir, mkdir, exec commmands in Linux.</p>

<p>File system has been represented by a tree and this tree has been implemented lists in Python. <strong>check_commands</strong> function acts as the main function in C and takes two parameters: FS and C.</p>

<ul>
  <li>
    <p><strong>FS:</strong> The existing directory tree in the system. For example,<br> ["/"] represents a fully empty system which           contains only the root("/") or<br>
      ["/", ["home", "D"]] represents a file system which contains a folder("D" or "d" for folder) named "home" under the root.<br>
      <em></em></p></li>

  <li>
    <strong>C:</strong> Commands that want to be executed. C is a list so commands should be given in a Python type list where each element is a string. For example, 
  <br>["cd home", "rmdir the4/the4"] dictates that working directory should be transformed to "home" and <strong>then</strong> delete the folder of the given path.
  </li>
</ul>

<p>Morever, <strong>check_commands</strong> function returns <strong>"SUCCESS"</strong>, <strong>FS(file system)</strong> after the required changes(for example, after executing copy, rm, rmdir commands etc.) and <strong>the last working direcory</strong> if every given command execuded succesfully. Otherwise, it throws an error and <strong>returns the command line which caused the error</strong> and shows the last working directory before the error.</p>

Here is the functions for commands in Linux and their explanations:<br>
<ul>
  
<li><strong>cd: </strong>Takes two parameters, FS and CD. FS is the file system provided to the function <strong>check_commands </strong>and CD is the path given to the command. Does the same operation as the "cd" command in Linux. Returns <strong>True</strong>  if the operation has been succesfull. Returns <strong>False</strong> otherwise.</li>
  <li>
    <p>
      <strong>rmdir: </strong> Takes two parameters: FS and RM. FS is the file system provided to the function <strong>check_commands </strong>and RM is the path given to the command. Removes the directory of the given path. Returns <strong>True</strong> if path is valid and the directory has been removed succesfully. Returns <strong>False</strong> otherwise.
    </p>
  </li>
  <li>
    <p>
      <strong>rm: </strong> Takes two parameters: FS and RM. FS is the file system provided to the function <strong>check_commands </strong>and RM is the path given to the command. Returns <strong>True</strong> if the path is valid and the file has been removed succesfully. Returns <strong>False</strong> otherwise.
    </p>
  </li>
  <li>
    <p>
      <strong>mkdir: </strong>Takes two parameters: FS and MD. FS is the file system provided to the function <strong>check_commands </strong>and RM is the path given to the command. Creates a directory with the given path. Returns <strong>True</strong> if the path is valid and directory has been created succesfully. Returns <strong>False</strong> otherwise.
    </p>
  </li>
  <li>
    <p>
      <strong>execute: </strong>Takes two parameters: FS and MD. FS is the file system provided to the function <strong>check_commands </strong>and EX is the path given to the command. Executes the file of the given path. Returns <strong>True</strong> if the path is valid and the file has been executed succesfully. Returns <strong>False</strong> otherwise.
    </p>
  </li>
  <li>
    <p>
      <strong>copy: </strong>Takes two parameters: FS and MD. FS is the file system provided to the function <strong>check_commands </strong>and CP is the path given to the command. Copies the file of the given path to required position. Returns <strong>True</strong> if the paths are valid and the file has been copeid succesfully. Returns <strong>False</strong> otherwise.
    </p>
  </li>
</ul>

<h3>Path Types</h1>
<ul>
  <li>
    <p>
      <strong>Absolute Path: </strong>Paths that are starting from the root. In this system, they are differentiated by a preceding slash "/". For example, "/home/etc" is an absolute path while "home/the4" is a relative path.
    </p>
  </li>
  <li>
    <p>
      <strong>Relative Path: </strong>Paths that are starting from the working directory. In this system, if a path is <strong>NOT</strong> preceded by a slash "/", that path is relative. For example, "/home/etc" is an absolute path while "home/the4" is a relative path.
    </p>
  </li>
</ul>

<h3>Example Function Calls</h3>
<p>
  For readibility, let's assume <br>
  <em>FS = ["/", "d", ["home", "D", ["user", "D", ["user", "D"], ["admin.txt", "F"]]], ["etc", "d"], ["tmp", "D", ["tmp.sh", "F"], ["del.txt", "F"]]]</em>
</p>
<p>
  <strong>check_commands(FS, ["cd home"]): </strong>This call will update the working directorty to "/home" and keep FS as it is. Here is the output: <br>
  </p>
  <p>
  <code>
    ('SUCCESS', ['/', 'd', ['home', 'D', ['user', 'D', ['user', 'D'], ['admin.txt', 'F']]], ['etc', 'd'], ['tmp', 'D', ['tmp.sh', 'F'], ['del.txt', 'F']]], '/home')
  </code>
 </p>
 <p>
  <strong>check_commands(FS, ["cd home", "rmdir user/user", "mkdir /etc/test2"]): </strong> This call will update to workind directory to "/home" and update the FS based on the given commands. Note that "user/user" is a relative path while "/etc/test2" is an absolute       path. (Also note that "rmdir user" would yield an error since non-empty folders can not be deleted.) Output:</p><br>
 <p>
 <code>
    ('SUCCESS', ['/', 'd', ['home', 'D', ['user', 'D', ['admin.txt', 'F']]], ['etc', 'd', ['test2', 'D']], ['tmp', 'D', ['tmp.sh', 'F'], ['del.txt', 'F']]], '/home')
  </code>
  </p>
  <p>
  <strong>check_commands(FS, ["cd home", "rm user/admin.txt"]): </strong> This call will update to workind directory to "/home" and update the FS based on the given commands. (admin.txt will be deleted.)
  </p>
  <p>
 <code>
    ('SUCCESS', ['/', 'd', ['home', 'D', ['user', 'D', ['user', 'D']]], ['etc', 'd'], ['tmp', 'D', ['tmp.sh', 'F'], ['del.txt', 'F']]], '/home')
  </code>
  </p>
  <p>
  <strong>check_commands(FS, ["cd tmp", "mkdir /home/user/user"]): </strong> This call will update the working directory to "tmp" and try to create a new folder named "user" under the path "/home/user". Since there is alreay such a folder, funcstion call will fail.
  </p>
  <p>
 <code>
    ('ERROR', 'mkdir /home/user/user', '/tmp')
  </code>
  </p>
