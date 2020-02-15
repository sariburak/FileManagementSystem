# File Management System
<p>A mere imitation of the file interaction system of Linux. This project has been made for a school homework and includes imitations of the cd, cp, rm, rmdir, mkdir, exec commmands in Linux.</p>

<p>File system has been represented by a tree and this tree has been implemented lists in Python. <strong>check_commands</strong> function acts as the main function in C and takes two parameters: FS and C.</p>
<ul>
  <li><p><strong>FS:</strong> The existing directory tree in the system. For example,<br> ["/"] represents a fully empty system which           contains only the root("/") or
    <br> ["/", ["home", "D"]] represents a file system which contains a folder("D" or "d" for folder) named "home" under the root. 
    <br><em><h6>From now on, the following directory system is going to be used to explain other functions:<br>
    ["/", "d", ["home", "D", ["the4", "D", ["the4", "D"], ["the.py", "F"]]], ["etc", "d"], ["tmp", "D", ["tmp.sh", "F"], ["del.txt", "F"]]]     </h6></em></p></li>

  <li>
    <strong>C:</strong> Commands that want to be executed. C is a list so commands should be given in a Python type list where each element is a string. For example, 
  <br>["cd home", "rmdir the4/the4"] dictates that working directory should be transformed to "home" and <strong>then</strong> delete the folder of the given path.
  </li>
</ul>

Morever, <strong>check_commands</strong> function returns <strong>"SUCCESS"</strong>, <strong>FS(file system)</strong> after the required changes(for example, after executing copy, rm, rmdir commands etc.) and <strong>the last working direcory</strong> if every given command execuded succesfully. Otherwise, it throws an error and <strong>returns the command line which caused the error</strong> and shows the last working directory before the error.
