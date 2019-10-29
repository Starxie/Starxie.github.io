#!/usr/bin/perl
use CGI ':standard';
print  "Content-type:text/html\n\n";
$first=param('first');
$last=param('last');
$age=param('age');
$team=param('team');
print "<head>\n";
print "<link rel='stylesheet' type='text/css' href='test.css'>\n";
print "</head>\n";
print  "<body>\n";
print "<div class='border'>\n";
print "<h1 class='center'>Your Results</h1>\n";
print  "<p class='center'>Your name: $first $last</p>\n";
print "<p class='center'>Age: $age</p>\n";
print "<p class='center'>You are cheering for $team this NBA Championship</p>\n";
print "</div>\n";
print "<div class='border'>\n";
print "<img class='center' src='https://raw.githubusercontent.com/Starxie/Starxie.github.io/master/CPS530/Lab04/$team.png' 
alt='no image' height='550' width='42'>\n";
print "</div>\n";
print  "</body>";