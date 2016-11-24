Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 26 2016, 12:10:39) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
import hashlib
user_1_hashed_pass="1b6453892473a467d07372d45eb05abc2031647a"
n = 0
for i in range (10):
    level_1_pass = str(i)
    user_guess_hashed = hashlib.sha1(level_1_pass).hexdigest()
    if(user_1_hashed_pass.strip()==user_guess_hashed,strip()):
   	 break
    n = n+1
print level_1_pass
print n
