# Postmortem Report - Alx system Engineering & Devops Project 0x19

## Introduction
Following the release of the Alx's System Engineering  & Devops project 0x19, an unexpected outage occurred on an isolated Ubuntu 20.04 container running an Nginx Web server. This issue resulted in GET requests returning a '500 Internal Server Error' response instead of the expected HTML file for a simple site. This postmortem provides a detailed account of the incident, the debugging provess, and measures taken to prevent similar occurences in the future.

## Incident Summary
- project: ALX System Engineering  & Devops project 0x19
- Server Environment: Ubuntu 20.04, Nginx web server

## Debugging Process
### 1. initial Assessment
Upon discovering the issue, I initiated the resolution proess. I began inspecting the system's processes using the `ps aux` command, which revealed two Nginx processes running as `root` and `www-data`.

### 2. Directory Examination
Next, I examined the configuration of the Nginx web server, specifically the `sites-availbale` folder in the `/etc/nginx/` directory. It was determined that the web server was configured to serve content from the `var/www/html/` directory.

### 3. Tracing System calls
In an attempt to gain more insights, I used the `strace` tool on the `root` Nginx process and simultaneously snt a `curl` request to the server. Unfortunately, the `strace` output yielded no valubale information.

### 4. Tracing the `www-data` Process
The next step involved running `strace` on the `www-data` Nginx process. This time, the output revelead an error: `-1 ENOENT (No such file or directory)` when attempting to access the file `/var/www/html/wp-includes/class-wp-loacle.phpp`.

### 5. Identifying the Issue
I meticulously examined files in the `/var/www/html/` directort, using Vim's pattern matching to locate the erroneous `.phpp` file extension. The issue was identified in the `wp-settings.php` file, specifically on line 137, where a trailing `p` was present.

### 6. Issue Resolution
The straightforward solution invloved removing the trailing `p` from the line in the `wp-settings.php` file.

### 7. Verification
After implementing the fix, I conducted another `curl` test on the server, which returned a successful `200 A-ok` response.

### 8. Automation
To prevent similar incidents in the future, I created a Puppet manifest that automates the correction of this type of error. The manifest replaces any instances of `phpp` extensions in the file `var/www/html/wp-settings.php` with `php`.

## Root Cause Analysis
In summary, the outage was caused by a typographica error in the `wp-settings.php` file. The error resulted in the application attempting to load the non-existent file `class-wp-locale.phpp` instead of the correct file, `class-wp-locale.php` located in the `wp-content` directory of the application.

## Prevention Measures
To mitigate such incidents in the future, the following preventive measures are recommended:
1. Rigorous Testing: Ensure thorough testing of the application before deployment to catch and address errors early in the development process.
2. Status Monitoring: Implements a reliable uptime-monitoring service, such as [UptimeRobot](https://uptimerobot.com/), to instantly alert admnistrators to website outages.

In response to the incident, I created a Puppet manifest, [0-strace_is_ypur_friend.pp](https://github.com/CJ-The-Black-Child/alx-system_engineering-devops/tree/009c8b3a6d12c03fc3faf501fda5ab7aeefb0993/0x17-web_stack_debugging_3/0-strace_is_your_friend.pp), which automates ther correction of `phpp` extensions in the `wp-settings.php` file. However, it is my aspiration as a programmer to continually improve and prevent errors. :wink:

